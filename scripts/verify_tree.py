"""Compare release inventory, checksums, document links and safe publication formats."""

import gzip
import hashlib
import io
from pathlib import Path, PurePosixPath
import re
import struct
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ALLOWLIST = "PUBLIC_ALLOWLIST.txt"
SUMS = "SHA256SUMS.txt"
PDF = "paper/manuscript.pdf"
TYPES = {"", ".bib", ".c", ".cff", ".g6", ".gif", ".gz", ".html", ".json", ".md", ".ots", ".pdf",
         ".py", ".sh", ".svg", ".tex", ".txt", ".yml"}
CREDIT = re.compile(rb"\b(?:" + b"|".join([b"G" + b"ia", b"Cl" + b"aude", b"Anthro" + b"pic",
                                          b"Open" + b"AI", b"Ast" + b"ra"]) + rb")\b", re.I)
EMAIL = re.compile(rb"(?i)(?<![\w.+%-])[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,15}\b")
PERSONAL_PATH = re.compile(rb"(?:/Us" + rb"ers/|/ho" + rb"me/|[A-Z]:\\Us" + rb"ers\\)[^/\\\s]+[/\\]")
SESSION = re.compile(rb"(?i)(?:chatgpt[.]com/(?:c|share)/|" + rb"cl" + rb"aude[.]ai/(?:chat/|code/session))"
                     rb"[a-z0-9_/-]{10,}")
CREDENTIAL = re.compile(rb"(?:gh[pousr]_[A-Za-z0-9_]{30,}|github_pat_[A-Za-z0-9_]{45,}|"
                        rb"(?:(?:AKIA|ASIA)[A-Z0-9]{16})|-----BEGIN (?:[A-Z0-9]+ )*PRIVATE KEY-----)")
LINK = re.compile(r"\[[^\]\n]*\]\(([^\s)]+)\)")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_inventory():
    names = (ROOT / ALLOWLIST).read_text().splitlines()
    require(names == sorted(set(names)) and PDF in names and SUMS in names,
            "Inventory must be sorted, unique and complete")
    actual = set()
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if ".git" in rel.parts:
            continue
        require(not path.is_symlink(), f"Unapproved symbolic link: {rel}")
        if path.is_file():
            actual.add(rel.as_posix())
    require(actual == set(names), "Allowlist mismatch: " + ", ".join(sorted(actual ^ set(names))))
    if (ROOT / ".git").exists():
        entries = subprocess.check_output(["git", "-C", str(ROOT), "ls-files", "-z"])
        tracked = set(entries.decode().split("\0")) - {""}
        require(tracked == actual, "Git index differs from the allowlist")
    digests = {}
    for line in (ROOT / SUMS).read_text().splitlines():
        match = re.fullmatch(r"([a-f0-9]{64})  ([^\r\n]+)", line)
        require(match is not None, "Malformed checksum entry")
        digest, name = match.groups()
        require(name not in digests, f"Duplicate checksum: {name}")
        digests[name] = digest
    require(set(digests) == actual - {SUMS}, "Checksum inventory mismatch")
    for name, digest in digests.items():
        require(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, f"Digest mismatch: {name}")
    return names


def check_links(name, data):
    for target in LINK.findall(data.decode("utf-8")):
        parsed = urlsplit(target)
        if parsed.scheme or not parsed.path:
            continue
        path = ((ROOT / name).parent / unquote(parsed.path)).resolve()
        require(path.is_relative_to(ROOT) and path.exists(), f"Missing repository link in {name}: {target}")


def check_animation(data):
    """Check all GIF records, allowing only pixels, frame timing and the loop setting."""
    stream = io.BytesIO(data)

    def take(size):
        value = stream.read(size)
        require(len(value) == size, "Truncated animation")
        return value

    def color_table(flags):
        if flags & 128:
            take(3 * (2 << (flags & 7)))

    require(take(6) == b"GIF89a", "Expected an animated GIF")
    width, height, flags, _, _ = struct.unpack("<HHBBB", take(7))
    require((width, height) == (760, 292), "Unexpected figure dimensions")
    color_table(flags)
    frames = controls = loops = 0
    while True:
        block = take(1)
        if block == b";":
            require(not stream.read(1), "Trailing animation data")
            break
        if block == b",":
            x, y, w, h, flags = struct.unpack("<HHHHB", take(9))
            require(w and h and x+w <= width and y+h <= height, "Frame outside the canvas")
            color_table(flags)
            require(2 <= take(1)[0] <= 8, "Invalid GIF code size")
            while size := take(1)[0]:
                take(size)
            frames += 1
        else:
            require(block == b"!", "Unknown GIF record")
            kind = take(1)
            if kind == b"\xff":
                loop_record = b"\x0bNETSCAPE2.0\x03\x01\x00\x00\x00"
                require(take(len(loop_record)) == loop_record, "Unexpected GIF application data")
                loops += 1
            else:
                require(kind == b"\xf9", "Unexpected GIF text or metadata")
                fields = take(6)
                require(fields[0] == 4 and fields[2:4] == b"\x0a\x00" and fields[-1] == 0,
                        "Unexpected animation timing")
                controls += 1
    require(frames == controls == 48 and loops == 1, "Expected a repeating 48-frame rotation")


def check_payload(name):
    path = ROOT / name
    ext = path.suffix
    require(ext in TYPES, f"Unapproved file type: {name}")
    require(not PurePosixPath(name).is_absolute() and ".." not in PurePosixPath(name).parts,
            f"Unsafe path: {name}")
    data = path.read_bytes()
    if ext == ".gz":
        data = gzip.decompress(data)
    if ext == ".pdf" or data.startswith(b"%PDF-"):
        require(name == PDF and data.startswith(b"%PDF-"), f"Unexpected PDF: {name}")
        return
    if ext == ".gif":
        require(name == "visuals/high-fans-rotation.gif", f"Unexpected animation: {name}")
        check_animation(data)
        return
    if ext == ".ots":
        require(name.startswith("evidence/timestamps/") and b"OpenTimestamps" in data[:80],
                f"Unexpected timestamp: {name}")
    else:
        require(b"\x00" not in data, f"Unexpected binary: {name}")
    for label, pattern in (("email", EMAIL), ("personal path", PERSONAL_PATH),
                           ("session link", SESSION), ("credential", CREDENTIAL)):
        require(not pattern.search(data), f"{label} pattern in {name}")
    if name != "AI_DISCLOSURE.md":
        outside_note = data
        if name == "paper/manuscript.tex":
            heading = rb"\section*{AI disclosure}" + b"\n"
            require(data.count(heading) == 1, "Expected one unnumbered manuscript disclosure")
            before, _, rest = data.partition(heading)
            note, boundary, after = rest.partition(b"\n\n")
            require(boundary and CREDIT.search(note), "Missing manuscript disclosure paragraph")
            outside_note = before + after
        require(not CREDIT.search(outside_note), f"Attribution outside disclosure: {name}")
    if ext == ".html":
        if name == "index.html":
            require(b'content="0; url=visuals/high-fans.html"' in data and
                    b'href="visuals/high-fans.html"' in data and b"<script" not in data.lower(),
                    "The site entrance must open the checked figure")
        else:
            require(name == "visuals/high-fans.html", f"Unexpected HTML document: {name}")
    if ext == ".md":
        check_links(name, data)
    if ext == ".svg":
        require(not re.search(rb"<(?:metadata|script)\b|data:(?:image|application)/|<image\b|\sexif:", data, re.I),
                f"Unexpected metadata or embedded payload in {name}")
    if name.startswith(".github/workflows/"):
        filetext = data.decode()
        require("runs-on: ubuntu-24.04" in filetext and "contents: read" in filetext,
                f"Runner or workflow permission mismatch in {name}")
        uses = re.findall(r"^\s*uses:\s*(\S+)", filetext, re.M)
        require(uses and all(re.fullmatch(r"[^\s@]+@[0-9a-f]{40}", action) for action in uses),
                f"Unpinned action in {name}")


def main():
    names = check_inventory()
    for name in names:
        check_payload(name)
    print(f"PASS inventory of {len(names)} files, all {len(names)-1} digests, links and release formats")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        sys.exit(f"Integrity check failed: {exc}")
