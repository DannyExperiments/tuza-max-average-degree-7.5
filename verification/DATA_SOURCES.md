# Data sources and permissions

The public files below were compared byte for byte with their upstream downloads. The SHA-256 digests identify the exact inputs to this release. The verifier reads the copies included here and runs offline.

| Local file | Creator and original file | SHA-256 |
| --- | --- | --- |
| [gupta-c4-v1.json](data/gupta-c4-v1.json) | Anish Gupta, [codegree-four certificates](https://raw.githubusercontent.com/agupta/tuza-maximum-degree-seven/main/data/B_codegree4_certificates.json) | `c51ad4aded53ca0ef7b20536a4008345d0f6f84e453441433e105d290319375f` |
| [graph7.g6](data/graph7.g6) | Brendan McKay, [all 1,044 simple graphs of order seven](https://users.cecs.anu.edu.au/~bdm/data/graph7.g6) | `5a878f1a46606da4733df250bf9a412d6ae0b3c73c2112e25d66ba00ae565b56` |
| [graph8.g6](data/graph8.g6) | Brendan McKay, [all 12,346 simple graphs of order eight](https://users.cecs.anu.edu.au/~bdm/data/graph8.g6) | `546a249902101c97d3aa590f93e53366854bd0a6f405aa59bdb32d25c57f845a` |

The numerical tables accompanying *Tuza's conjecture for graphs of maximum degree at most seven* are copyright © 2026 Anish Gupta and are supplied under Creative Commons Attribution 4.0 International. The table here has a shorter filename and retains the original bytes. [Paper](https://arxiv.org/abs/2608.06538) · [Upstream licensing statement](https://raw.githubusercontent.com/agupta/tuza-maximum-degree-seven/main/LICENSES.md) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

Brendan McKay publishes the two unchanged graph6 files in his *Combinatorial Data* collection under Creative Commons Attribution 4.0 International. [Catalogue listing](https://users.cecs.anu.edu.au/~bdm/data/graphs.html) · [Collection and license notice](https://users.cecs.anu.edu.au/~bdm/data/) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

The project adapted Gupta's codegree-four witnesses by permuting vertex labels, reusing packings on additional admissible graphs and restricting bought edges to each resulting graph. The 3,245 transferred witnesses in `PAIR_TRANSFER.json.gz` and their 986-row subset in `PAIR_ONE_DEFECT.json.gz` credit Anish Gupta and retain CC BY 4.0. Their `via` entries identify the source row and its relabelling. The 38 additional witnesses in `PAIR_DIRECT.json.gz` are separate project computations. [Data license](https://creativecommons.org/licenses/by/4.0/) · [Pair checker](verify_pairs.py)

The remaining JSON files contain project-generated certificates, numeric summaries or graph examples. `SEVEN_CENSUS.json` supplies 40 cone witnesses. The eight-link verifiers use `STAR_ATLAS.json`, `MARKED_CUT.json` and `MIXED_LOW.json` for the link exclusions, cone packings and marked reductions. `MIXED_NINE.json` and `COUNT_WITNESSES.json` give the explicit mixed-donor and union-eight witnesses. The files `path_pair_1.json` and `path_pair_2.json` give two path-pair constructions. Each graph catalogue key uses the published graph6 labelling. The source files for the order-nine and order-ten programs are project code. The complete list of input digests accompanies the replay. [Input digests](reference.json) · [Project license status](../LICENSE_STATUS.md)
