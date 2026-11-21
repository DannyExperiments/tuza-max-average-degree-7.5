# Building the manuscript

[manuscript.tex](manuscript.tex) and [references.bib](references.bib) are the complete typesetting inputs for [manuscript.pdf](manuscript.pdf). The fan figure is drawn directly in the source. The paper uses the AMS article class, standard mathematical fonts, inline cross-references and a BibTeX bibliography.

## With TeX Live

Run from this directory with a TeX Live installation containing the AMS article class, AMS bibliographic styles, geometry, mathtools, microtype, iftex and hyperref.

~~~sh
latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex
~~~

The equivalent explicit sequence is

~~~sh
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex manuscript
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
~~~

## With an offline TeX cache

The distributed PDF was produced from the two files above using Tectonic 0.17.0 with an already populated cache. Two independent output directories produced identical PDF bytes using the release date at 00:00 UTC as the reproducible timestamp.

~~~sh
outdir="$(mktemp -d)"
SOURCE_DATE_EPOCH=1795219200 tectonic --only-cached --untrusted --keep-logs --outdir "$outdir" manuscript.tex
~~~

The engine ran TeX, BibTeX, the cross-reference passes and the PDF writer. A rebuild with a different engine, font release, or creation timestamp can change the PDF digest. The source, visible title, mathematical statements and resolved references are the relevant comparison across engines.

## Checked release copy

The PDF has 11 A4 pages with selectable text. The visible title and PDF Title both read **Tuza's inequality at maximum average degree 15/2**. The PDF Author is empty. Six bibliography entries resolve, with nine public article or DOI links. Every page was rendered and inspected, including the seven-edge fan, the donor tables, the strict endpoint argument, the four-edge proposition and the census table. The final TeX log contained no unresolved references, missing characters or box warnings. This verifies typesetting and source parity. The manuscript is internally reviewed, not peer reviewed.

| File | SHA-256 |
| --- | --- |
| manuscript.tex | 4ab81834a2591b3b7f2c1ae28efa70e32d2f97354a4f2c7bfa7af2b6929bfb41 |
| references.bib | 8a9c1c58b5a5fb6a6a8226560e5e9334c615c11aeba52d092686e1920a2512c8 |
| manuscript.pdf | 11eb1645a209ef06e746dffb3d8eccbd51be2c21e02f59d58f20fce056aa5f85 |

The [verification guide](../verification/README.md) describes the finite graph and arithmetic checks. The proofs using those checks and the dependence on Kandasamy's maximum-degree-ten preprint appear in the manuscript.
