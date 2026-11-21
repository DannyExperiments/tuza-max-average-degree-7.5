# Reproducibility

All mathematical verifiers use the data included in this repository. For the full local replay use Python 3.11 or later, a Clang C compiler, Bash, Git and either the Poppler commands `pdfinfo` and `pdftotext` or an interpreter with `pypdfium2`. The hosted jobs use Ghostscript to read PDF metadata and extract page text inside the same pinned TeX distribution used to build the manuscript. The order-ten catalogue digest is also checked using `shasum`. Use an ordinary Python interpreter with assertions enabled. The verifier rejects `-O` and `-OO`.

## Quick checks and exact replay

Run from the repository root:

```sh
bash scripts/verify.sh --integrity-only
bash scripts/verify.sh
```

The first command checks every allowed path and SHA-256 digest and inspects the PDF. It also checks the edges and triangular faces of the interactive figure against both static projections. The second also runs the local proofs’ finite checks and the census through order nine. The default replay copies inputs to a temporary directory and compares fresh results against the values in the reference file. The independently reproducible steps and exact data sources are listed alongside the verifiers. [Reference values](verification/reference.json) · [Data credits](verification/DATA_SOURCES.md)

| Check | Expected evidence |
| --- | --- |
| A. Donor counts and recipient transfer | Exact rational arithmetic for the earlier counting rows and the final endpoint |
| B. Links and pairs | The full seven-link domain; 3,286 codegree-four pair classes, 3,283 covered on each of 16 completions, three exceptional signatures; separate input replay for codegrees five and six |
| C. High fans | Complete finite link markings, tetrahedron reductions, and the numerical or finite parts of the two-fan proof |
| Finite census | Independently generated and checked small-order witnesses, followed by one-vertex augmentation through the requested order |

The finite checks verify specific hypotheses or local calculations in the proofs. The structural deductions and the arguments for arbitrary graph order are in the manuscript and proof records. [Manuscript](paper/manuscript.pdf) · [Proof guide](PROBLEM_AND_PROOF.md)

## Manual order-ten replay

```sh
python3 -B verification/run.py --max-order 10
```

This regenerates the nine-vertex catalogue from the pinned eight-vertex catalogue, checks its 274,706 rows and SHA-256 `114059e7803a0d5ab0b347819475df889a852b85adc90d491b8d18b10d1aa65d`, and runs the unpartitioned order-ten check. The catalogue contains 274,642 canonical representatives plus 64 fallback presentations. The replay checks the entire resulting extension domain.

| Order | Raw one-vertex extensions | Spanning triangle-connected candidates | Exact packing checks | Exact cover checks | Tight hits |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 9 | 3,160,576 | 1,111,668 | 6,692 | 0 | 0 |
| 10 | 140,649,472 | 63,572,957 | 111,898 | 0 | 0 |

The counts are augmentation instances. Isomorphic supports may recur. The historical manual run spent 389.208 seconds (about 6.5 minutes) on the order-ten stage; catalogue preparation, other checks and hardware affect total runtime. A zero in the exact-cover column means earlier bounds already decided every candidate. The small-order certificates provide the $K_4,K_5$ cases. The November verification confirms the July result through ten vertices.

## PDF and hosted checks

The PDF workflow copies only the manuscript source and bibliography into an empty directory and compiles them using the same pinned TeX distribution as the repository template. It checks the typeset title, author metadata and references and makes the rebuilt PDF available as a run artifact. Different TeX engines can produce different PDF bytes from identical sources. The release checksum identifies the exact stored PDF. [Paper build](paper/BUILD.md)

The three workflows target Ubuntu 24.04, use actions pinned by commit, and grant read-only access to repository contents. Each badge links to the actual run history. [Evidence check](.github/workflows/verify.yml) · [Exact replay](.github/workflows/replay-exact-verifier.yml) · [PDF build](.github/workflows/pdf.yml)
