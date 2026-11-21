"""Check the published PDF with Poppler, Ghostscript or PDFium."""

from pathlib import Path
import re
import shutil
import subprocess
import sys
import unicodedata


def normalized(text):
    return " ".join(unicodedata.normalize("NFKC", text).replace("’", "'").split()).casefold()


def read_paper(path):
    if shutil.which("pdfinfo") and shutil.which("pdftotext"):
        info = subprocess.check_output(["pdfinfo", str(path)], text=True)
        props = dict(line.split(":", 1) for line in info.splitlines() if ":" in line)
        first = subprocess.check_output(["pdftotext", "-f", "1", "-l", "1", str(path), "-"], text=True)
        body = subprocess.check_output(["pdftotext", str(path), "-"], text=True)
        return props, first, body
    if shutil.which("gs"):
        # The stock Ghostscript helper converts both PDFDocEncoding and UTF-16 metadata to UTF-8.
        name = str(path.resolve())
        query = ["gs", "-q", "-dBATCH", "-dNOPAUSE", "-dNODISPLAY", "-dSAFER",
                 "--permit-file-read=" + name, "-sFile=" + name, "-dDumpMediaSizes=false",
                 "-dDumpFontsNeeded=false", "pdf_info.ps"]
        info = subprocess.check_output(query, text=True, encoding="utf-8")
        props = dict(re.findall(r"^(Title|Author):[ \t]*(.*)$", info, re.M))
        count = re.search(r" has (\d+) pages?\.?\s*$", info, re.M)
        if not count:
            raise ValueError("Ghostscript could not read the manuscript page count")
        props["Pages"] = count.group(1)
        args = ["gs", "-q", "-dSAFER", "-dBATCH", "-dNOPAUSE", "-sDEVICE=txtwrite",
                "-dTextFormat=3", "-sOutputFile=-"]
        first = subprocess.check_output([*args, "-dFirstPage=1", "-dLastPage=1", name], text=True)
        body = subprocess.check_output([*args, name], text=True)
        return props, first, body
    try:
        import pypdfium2
    except ImportError:
        raise ValueError("PDF review requires Poppler, the pinned TeX toolchain, or pypdfium2")
    with pypdfium2.PdfDocument(path) as document:
        props = document.get_metadata_dict()
        props["Pages"] = str(len(document))
        pages = [page.get_textpage().get_text_bounded() for page in document]
    return props, pages[0], "\n".join(pages)


def check(path):
    if not path.is_file() or not path.read_bytes().startswith(b"%PDF-"):
        raise ValueError("Missing or invalid PDF")
    properties, first, body = read_paper(path)
    expected_title = "tuza's inequality at maximum average degree 15/2"
    if normalized(properties.get("Title", "")) != expected_title:
        raise ValueError("Incorrect PDF title metadata")
    if properties.get("Author", "").strip():
        raise ValueError("PDF Author metadata must be empty")
    if expected_title not in normalized(first):
        raise ValueError("Manuscript title missing from first page")
    if int(properties.get("Pages", "0")) < 2 or "references" not in normalized(body):
        raise ValueError("Expected a multipage mathematical paper with references")
    markers = ["Danny" + "Experiments", "Cl" + "aude", "Open" + "AI", "Ast" + "ra", "G" + "ia"]
    for marker in markers:
        if re.search(r"\b" + re.escape(marker) + r"\b", body, re.I):
            raise ValueError("The manuscript contains an attribution reserved for release metadata")
    print(f"PASS authorless PDF, title, body and bibliography ({properties['Pages'].strip()} pages)")


if __name__ == "__main__":
    try:
        check(Path(sys.argv[1]))
    except (IndexError, ValueError, OSError, subprocess.CalledProcessError) as exc:
        sys.exit(f"PDF check failed: {exc}")
