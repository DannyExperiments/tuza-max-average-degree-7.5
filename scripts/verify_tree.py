"""Compare release inventory, checksums, document links and safe publication formats."""

import gzip
import hashlib
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ALLOWLIST = "PUBLIC_ALLOWLIST.txt"
SUMS = "SHA256SUMS.txt"
PDF = "paper/manuscript.pdf"
TYPES = {"", ".bib", ".c", ".cff", ".g6", ".gz", ".html", ".json", ".md", ".ots", ".pdf",
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
    if ext == ".ots":
        require(name.startswith("evidence/timestamps/") and b"OpenTimestamps" in data[:80],
                f"Unexpected timestamp: {name}")
    else:
        require(b"\x00" not in data, f"Unexpected binary: {name}")
    for label, pattern in (("email", EMAIL), ("personal path", PERSONAL_PATH),
                           ("session link", SESSION), ("credential", CREDENTIAL)):
        require(not pattern.search(data), f"{label} pattern in {name}")
    if name != "AI_DISCLOSURE.md":
        require(not CREDIT.search(data), f"Attribution outside disclosure: {name}")
    if ext == ".html":
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
