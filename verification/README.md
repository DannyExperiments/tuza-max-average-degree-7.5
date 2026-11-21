# Replaying the finite checks

From the repository root, run the standard check through order nine.

```sh
python3 -B verification/run.py --max-order 9
```

For the full manual check through order ten, use the same entry point.

```sh
python3 -B verification/run.py --max-order 10
```

Use Python 3.9 or later and an installed Clang C compiler. Order ten also uses the standard `shasum` utility. The Python checks use only the standard library. Both modes verify the input digests, work in a fresh temporary directory and print each pass with elapsed time. A failed assertion, missing input, changed reference result or unexpected C output gives a nonzero exit. The entry point and all check programs reject Python's `-O` and `-OO` modes.

## What each computation establishes

| Argument | Computation | Reproduced values |
| --- | --- | --- |
| Adjacent sevens | [Gupta's codegree-four table](check_gupta.py), [five- and six-tip cores](check_gupta_56.py) | 1,144 original certificates, 18,304 cross-edge completions, 34 and 156 respective core isomorphism classes |
| Pair reductions | [Independent domain enumeration](audit_pairs.py), [exact decisions on the residual classes](check_pair_exceptions.py), [physical certificate reader](verify_pairs.py) | 451,235 labelled pairs, 3,286 orbits, 3,283 uniform witnesses, 52,528 completed graphs, three exceptional classes and 19 exact cross-pattern orbits |
| Degree-seven links and the triangle-free high subgraph | [Cone, pair and group certificates](four_high_audit.py), [quartet check](check_quartet.py), [five-neighbour and component check](check_triangle_free.py) | 1,044 classes of seven-links, orbit mass $2^{21}$, 40 positive cones, 543 root triangles, 388 labelled triangle-free five-vertex graphs and a 9-triangle packing with 16 bought edges on the square component |
| Degree-eight donors | [Entire eight-link domain](check_eight_domain.py), [all five-mark placements](check_eight_placements.py) | 203 of 12,346 link classes remain after positive exclusions. The 11,368 five-mark placements give 363,776 subset prices. Of these placements 3,308 contradict the degree bound and 8,060 have a verified reduction. |
| Degree-nine donors | [Two subsumed fives](check_union_eight.py), [a subsumed five and six](check_mixed_nine.py) | Six witnesses cover all 49 labelled hole choices and 512 cross-edge choices in the union-eight case, for 25,088 graphs. The 64 mixed-nine adjacency masks give 507 packed triangles, 925 internal purchases, 56 exterior purchases and 3,010 internal root triangles across the witnesses. |
| Maximum average degree | [Predecessor budget](check_count.py), [endpoint weights and partitions](check_endpoint.py) | The predecessor coefficient gives $989/132$. The final ledger attains coefficient $2$, hence $7+1/2=15/2$. The $1/30$ transfer cases test 5, 15, 15 and 52 set partitions and three admissible families with a unique outsider. Every residual affine gap is strictly positive at $k=4$ and has positive slope. |
| Distinct high fans | [Seven-link markings](seven_links.py), [special sevens](check_special_seven.py), [path-pair certificates](check_path_pair.py), [ordinary fan edge sets](check_two_fans.py) | 77 residual seven-links, 159 eligible markings, five zero-fan markings, no marking with exactly one, two or three fans. The special-seven check covers 200 labelled assignments, including 194 certified reductions. The path-pair check tests 4,096 assignments. |
| Small tight supports | [Constructive census](small_census/census.py), [independent physical-witness reader](small_census/verify.py), [C augmentation](fast.c) | At order eight, 12,346 isomorphism classes represent all $2^{28}$ labelled graphs. The independent reader checks 14,088 strict component certificates and 1,008 requested-edge minimum covers across 142 positive tight graphs. |

The global deductions in A–C use the structural lemmas in the paper. In particular, strictness when the average degree equals $15/2$ uses the maximum-degree-ten theorem. The arithmetic and finite graph checks can be inspected independently. [Claims and dependencies](../CLAIMS_EVIDENCE_MATRIX.md)

The data directory includes small reference tables so the named scripts also have their direct inputs. The full runner removes derived tables from its scratch copy before reproducing them. For example, the exact search regenerates all three exceptional pair decisions, the witness reader regenerates the 3,283-orbit summary and the four-high check regenerates the atlas used by the budget program. The complete endpoint ledger, fan control graphs, expected census distributions, per-stage result hashes and input pins are available as JSON. [Reference outputs](reference.json) · [Data provenance](DATA_SOURCES.md)

## How the census covers its domain

At orders one through eight, the Python census groups the ordinary triangles into components that share edges. Each component either has a literal strict packing/cover certificate or is a complete graph on four or five vertices. Removing isolated vertices relates the eight-vertex catalogue to every lower order. The verifier decodes the graph6 rows and physical witnesses a second time with sets of edges.

Every nine-vertex graph has an eight-vertex parent obtained by deleting a vertex. The C program attaches a new vertex to each possible subset of a parent. Each spanning, triangle-connected support that survives the first filters receives a packing lower bound and a cut-complement cover upper bound. Exact packing and cover decisions are used when needed. The counts below refer to augmentation instances, so an isomorphism class can occur more than once.

| Order | Parent rows | Extensions tested | Spanning candidates | Exact packing calls | Exact cover calls | Tight hits |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 9 | 12,346 | 3,160,576 | 1,111,668 | 6,692 | 0 | 0 |
| 10 | 274,706 | 140,649,472 | 63,572,957 | 111,898 | 0 | 0 |

For order ten, `canon.c` first revisits all 3,160,576 order-nine extensions. It emits 274,642 canonical representatives and retains 64 additional rows under their original labellings when refinement is expensive. This preserves coverage and admits duplicate isomorphism classes. The full 274,706-row output has SHA-256 `114059e7803a0d5ab0b347819475df889a852b85adc90d491b8d18b10d1aa65d`.

To reproduce just the native steps manually, start in a fresh working directory containing copies of `canon.c`, `fast.c` and `data/graph8.g6` under the name `graph8.g6`. The full sequence on hosts with these system utilities is

```sh
/usr/bin/clang -O3 -std=c11 canon.c -o canon
/usr/bin/clang -O3 -std=c11 fast.c -o fast
./canon < graph8.g6 > c9.g6
/usr/bin/shasum -a 256 c9.g6
./fast < graph8.g6
./fast < c9.g6
```

Both invocations of `fast` read the entire input in one process. The through-nine mode only compiles `fast.c` and feeds it the eight-vertex catalogue. These native steps supplement the independent checks of the lower orders.
