# Pairs of degree-seven vertices

<a id="pair"></a>

## A degree-eight tip at the common edge of two sevens

~~~text
                  four common vertices C
                     h, c₁, c₂, c₃
   a₁,a₂ ───── u ───────────────────── v ───── b₁,b₂
                ╲                         ╱
                 ╲_____ each of C _______╱
                           h
       six of {c₁,c₂,c₃,a₁,a₂,b₁,b₂} join h; one misses h
~~~

Here $d(u)=d(v)=7$, $uv$ is an edge, $d(h)=8$, and $h$ has six other neighbors inside this ten-vertex local graph. Each $a_i$ joins $u$ and misses $v$, and each $b_i$ joins $v$ and misses $u$. All other contacts are conditional. The four $a_i b_j$ cannot complete a triangle at either endpoint, but could participate in triangles at $h$.

### Result

**Every subgraph-minimal Tuza violation has at least three neighbors of degree at least eight at each degree-seven vertex.** In particular it cannot contain the proposed degree-eight hub with any exclusive degree-seven neighbor. This is a necessary condition on a minimal violation. It strengthens the previous one-neighbor guarantee. [Earlier density proof](low-vertex-reductions.md#local)

The exact local statement uses both endpoint links. Suppose $u,v$ are adjacent degree-seven vertices, $|N(u)\cap N(v)|=4$, and their induced links are connected and non-WKE. For each common tip $x$ let $s(x)$ count its neighbors in $C\cup A\cup B$, excluding $u,v$. Call a tip over budget if $s(x)>5$. **When at most three tips are over budget, the pair $\{u,v\}$ has a packing and cover giving a Puleo reduction in every ambient graph.** The supplied witnesses work for all private cross-edge choices. Of the 83 classes with four over-budget tips, 80 also have such a uniform witness. The remaining three have the exact local decisions below. The positive statement uses direct verification of stored certificates and coverage of the finite domain.

| Number of over-budget tips | All isomorphism classes | Classes with a single witness valid for every choice of private cross edges |
|---:|---:|---:|
| 0 | 1,144 | 1,144 |
| 1 | 1,134 | 1,134 |
| 2 | 715 | 715 |
| 3 | 210 | 210 |
| 4 | 83 | 80 |

The original target with exactly one tip of local degree $2+6=8$ comprises **986** classes, or 157,312 fully labeled graphs before adding private cross edges. The other 148 single-tip classes have $s(x)=7$ at their one over-budget tip. All 1,134 single-tip classes already work by transporting Gupta’s published certificates. [Certificate data](../verification/data/PAIR_ONE_DEFECT.json.gz) · [Certificate data](../verification/data/PAIR_RECEIPT.json)

#### Why the three-neighbor conclusion follows

A degree-seven vertex $u$ adjacent to a low vertex already sees three or more high vertices by the subsumption argument in the earlier proof. Otherwise suppose it has at most two high neighbors. Gupta’s seven-vertex link census gives at least three incidences $uv$ of codegree at least four, so choose such a $v$ of degree seven. Both endpoint links are connected and non-WKE in a minimal violation. Codegree five or six gives a reduction by Gupta’s endpoint reductions. At codegree four, all four common tips belong to $N(u)$. Any tip with $s(x)>5$ has degree at least eight, so at most two can be over budget here. The listed certificates give a pair reduction, again a contradiction. This rules out a single exclusive rim vertex without restrictions on the other neighbors of its high neighbor. The argument itself only needs the rows with at most two over-budget tips. [Gupta, link census and local reductions](https://arxiv.org/html/2608.06538v1#S4) · [Independent five- and six-tip replay](paired-sevens.md#gupta)

### Exhaustive domain and actual witnesses

Use $u=0,\ v=1,\ C=(2,3,4,5),\ A=(6,7),\ B=(8,9)$. The 13 endpoint spokes are fixed. A 24-bit key specifies the six unordered pairs in $C$, then the eight $C$-to-$A$ contacts and the one pair in $A$, then the analogous nine edges on the $B$ side. Each side is tested for connectivity and WKE on its actual seven-vertex link. The WKE test enumerates vertex sets $Q$. Edges outside $Q$ must form a matching, and that forced matching can be extended to size $|Q|$ exactly when the maximum matching on its unused vertices supplies the remaining edges. The two side encodings are combined only when they share the same $C$ graph. This yields 451,235 labeled graphs satisfying the two link conditions. Quotienting by the 24 permutations of $C$, both swaps within the private pairs and exchange of the endpoints gives exactly 3,286 classes. These agree with Gupta's unrestricted (A1) total. [Verification](../verification/pair_domain.py) · [Gupta, Section 9](https://arxiv.org/html/2608.06538v1#S9)

A certificate $(S,X)$ consists of actual edge-disjoint triangles and selected graph edges. It pays when $|X|\le2|S|$, every triangle at $u$ or $v$ meets $X$, and every edge of a packed triangle lying outside these two vertices belongs to $X$. Then deleting $u,v$ and $X$ leaves an edge-disjoint residual problem.

Gupta published certificates for the 1,144 classes satisfying (A2). One such certificate works on any new key that contains all the rim edges required by its packing and creates no uncovered endpoint triangle. For each optional rim edge, check each endpoint that can see both ends. If neither incident spoke nor the rim edge is bought, forbid that rim edge. Intersect the bought set with the actual graph. These conditions recover 3,245 of the 3,286 classes after relabeling. A separate search returned 38 further certificates. Its choice of trial packings affects only discovery. Their literal packing and cover lists are stored and can be checked without repeating the search. [Certificate data](../verification/data/PAIR_TRANSFER.json.gz) · [Certificate data](../verification/data/PAIR_DIRECT.json.gz)

The separate verification program reconstructs every edge list and tests each of the 3,283 positive representatives on all 16 choices of the four edges in $A\times B$, for **52,528 literal graph checks**. It checks that all certificate edges exist, all packed edges are distinct, every endpoint triangle is covered and all packed rim edges are bought. Extra ambient vertices cannot create additional triangles at $u$ or $v$, since their full neighborhoods are known. The unrestricted degree, number and adjacency of outside vertices therefore preserve each certificate. [Verification](../verification/verify_pairs.py) · [Certificate data](../verification/data/PAIR_FINAL.json)

### The three exceptional local graphs

For each of the following three keys, **every** $C$-to-private contact is present. The drawing specifies all optional edges once its row and its four cross bits are supplied.

~~~text
          A = {6,7}             C = {2,3,4,5}             B = {8,9}
           optional     all 8 ───── core H ───── all 8     optional
            edge 67       to C                   to C      edge 89
           u adjacent to A,C and v      v adjacent to B,C and u
                       A–B cross edges independently optional
~~~

| Key | Core $H$ | $67,\ 89$ | Designated pair reduces on the ten-vertex graph |
|---:|---|---|---|
| 8,372,190 | $C_4$, missing $23,45$ | both absent | Exactly when at least one cross edge is present (15 choices) |
| 8,372,223 | $K_4$ | both absent | No choice of cross edges (16 tested) |
| 8,388,607 | $K_4$ | $67$ present, $89$ absent | No choice of cross edges (16 tested) |

Here is the proof of completeness for those last decisions. Fix exactly which of the 13 spokes are bought, a set $Z$. If an uncovered triangle using $uv$ remains, reject $Z$; every edge of that triangle is a spoke. Each other uncovered endpoint triangle has a unique rim edge that must be bought. Let $F$ be the set of those forced rim edges. For any packing $S$ the least possible cover with precisely these spokes and this packing is

$$
Z\cup F\cup\{e:e\in E(S),\ e\text{ is a rim edge}\}.
$$

The contribution of each packed triangle $T$ to the remaining budget is $2-|E_{\rm rim}(T)\setminus F|$. These costs add because the triangles are edge-disjoint. Thus $Z$ succeeds exactly when a maximum-weight edge-disjoint collection has weight at least $|Z|+|F|$. The exact checker partitions all spoke masks by automorphisms preserving the actual graph and endpoint pair. For each eligible orbit it solves this inequality on the compatibility graph of actual triangles. In its branch bound, every color class consists of pairwise incompatible triangles, contributing at most its largest positive weight. Branching over the vertices in reverse color order enumerates every clique still capable of paying. Nonpositive triangles may be omitted. Private cross patterns are quotiented only by automorphisms preserving that specific key, and positive certificates are transported back and checked on every cross pattern. The 48 decisions include 15 affirmative and 33 negative cases. The three finite graphs with zero cross edges are genuine counterexamples to always reducing the designated endpoint pair under (A1) alone. Extra triangles elsewhere in a larger ambient graph can provide additional reductions. [Verification](../verification/check_pair_exceptions.py) · [Certificate data](../verification/data/PAIR_EXACT.json)

### A direct six-triangle proof for the multipartite rim

Suppose the remaining rim candidate is $K_{2,3,3}$ and $h$ sees the entire rim. Write $s,t$ for the two-vertex part and $L=\{\ell_0,\ell_1,\ell_2\}$, $R=\{r_0,r_1,r_2\}$ for the others. The actual degrees $d(s)=d(t)=7$ mean
$N(s)=N(t)=\{h\}\cup L\cup R$.

~~~text
    at s     ℓ₀ ─ r₀      ℓ₁ ─ r₁      ℓ₂ ─ r₂
    at t     ℓ₀ ─ r₁      ℓ₁ ─ r₂      ℓ₂ ─ r₀
    cover    all nine L–R edges together with sh and th
~~~

Choose the nonadjacent pair $\{s,t\}$. The six indicated triangles are edge-disjoint. Their only edges outside $\{s,t\}$ are the six distinct displayed $L$-to-$R$ edges. Every triangle at either chosen vertex uses its spoke to $h$ or an $L$-to-$R$ edge. Consequently the 11 stated edges cover all these triangles and buy all six required rim edges, with $11<2\cdot6$. This argument leaves outside contacts at all other vertices arbitrary. [Certificate data](../verification/data/PAIR_FINAL.json)

### Verification

The checks reconstruct the actual rooted graphs and verify the packing and cover witnesses on all allowed private-edge completions. [Pair verifier](../verification/verify_pairs.py) · [Certificate provenance](../verification/DATA_SOURCES.md)

<a id="gupta"></a>

## Gupta’s two endpoint reductions at codegree five or six

~~~text
        only if c=5                  common core H                 only if c=5
       a ───────── u ──────────────────────── v ───────── b
        ╲          │   ╲                     ╱   │         ╱
        Dₐ ⊆ C     └─── 0, 1, …, c−1 = C ───────┘     Dᵦ ⊆ C
                           selected core edges R
                    one color packed at u, one at v
~~~

The two endpoints each have degree seven, and every vertex of $C$ is adjacent to both. $H=G[C]$ is arbitrary. When $c=5$, $a,b$ are distinct, with $av,bu$ absent. Their two contact sets are arbitrary. An optional edge $ab$ belongs to no triangle containing $u$ or $v$. When $c=6$ there are no private vertices.

**Proposition.** Both inherited finite reductions passed an independent replay. At codegree six the two endpoints of degree seven always form a reducible pair. At codegree five this conclusion follows when one endpoint has a connected non-WKE link, as it does in the minimal-violation application. The degrees of the common and private neighbors and the rest of the graph are unrestricted. This verifies Gupta’s Propositions 7.1, 7.3, 8.1, 8.3 and 8.5 at their local scope. [Gupta, Sections 6–8](https://arxiv.org/html/2608.06538v1#S6) · [Verification](../verification/check_gupta_56.py) · [Certificate data](../verification/data/GUPTA_56_REPLAY.json)

| Common neighbors | Labeled cores | Isomorphism classes | Classes with a verified template | Labeled cores where the template fails |
|---|---:|---:|---:|---:|
| Five | 1,024 | 34 | 29 | 32 |
| Six | 32,768 | 156 | 155 | 1 |

#### How all template choices were checked

For $R\subseteq E(H)$, let $q$ be the minimum vertex cover size of $H-R$, computed by trying every subset of $C$ in increasing order of size. For $p$, take a matching $M_u$ and a matching $M_v$ in $R$. Their edge sets must be disjoint but their vertices may overlap. Pack the triangles $uxy$ for $xy\in M_u$ and $vxy$ for $xy\in M_v$. If $C$ has a vertex $z$ incident to neither matching, add $uvz$. At most one triangle can use $uv$. Every allowed template packing has exactly this form, so maximizing its size gives $p$. The checker enumerates the two matchings independently, retains an optimal packing for each exact union, then takes the maximum over the unions contained in each $R$.

With $t=3$ for $c=5$ and $t=1$ for $c=6$, the tested slack is $2p-t-|R|-2q$. The cover consists of $uv$, the selected rim edges $R$, both spokes to every vertex of a minimum cover of $H-R$, and the two private spokes $ua,vb$ when present. For a successful $H$, the checker reconstructs a maximizing packing and this cover. It enumerates all triangles at the endpoints, verifies that each is hit, checks pairwise disjointness of the packing edges, and checks that all packed edges outside the endpoints belong to the cover. For $c=5$ it does this on the graph with every private contact and $ab$ present. The packing and cover use none of those optional edges, so deleting any combination preserves the certificate.

Every simple labeled core is an edge mask on the $\binom c2$ pairs. The checker partitions all masks by applying adjacent transpositions of the vertex labels until each orbit closes. Those transpositions generate the symmetric group. For each orbit representative, it tests every submask $R$ of the core. All the quantities and the three reduction conditions are invariant under relabeling. This covers every core and every possible choice of $R$, including for failed cores. The output gives the complete best-slack distributions. For example, 155 labeled six-vertex cores have optimum slack zero, representing four isomorphism classes. The only negative six-vertex class is $K_6$, with slack $-1$. [Gupta, Proposition 7.1](https://arxiv.org/html/2608.06538v1#S7) · [Certificate data](../verification/data/GUPTA_56_REPLAY.json)

#### Exceptional five-vertex cores

The five failed isomorphism classes are the empty graph, $K_{1,4}$, $K_3\sqcup K_2$, the bowtie $K_1\vee 2K_2$, and $K_5$. Their labeled multiplicities are $1,5,10,15,1$, respectively. All five have best slack $-1$.

For each of the 32 failed labeled cores, the checker builds the complete link of $u$ for each of the 32 choices $D=N(a)\cap C$. Here $v$ joins every core vertex and misses $a$. When $D$ is empty, $a$ is isolated, giving 32 disconnected links. Otherwise the link is connected. To test WKE the checker tries every matching $M$ of this seven-vertex link and all vertex subsets $Q$ of size at most three. It asks whether $|Q|\le|M|$ and every edge with neither endpoint in $Q$ belongs to $M$. A larger $Q$ cannot witness WKE because a matching has at most three edges. The 31 noncomplete labeled cores and 31 nonempty contact choices give **961 connected WKE links**. The complete core gives **31 connected non-WKE links** for the nonempty choices. Thus under the required link hypothesis only the complete five-vertex core remains. [Gupta, Propositions 8.1 and 8.3](https://arxiv.org/html/2608.06538v1#S8)

#### Complete cores

Both use the seven Fano lines on $\{u,v,0,1,2,3,4\}$. The checker generates their 21 edges and verifies that each occurs once. It then checks the 13-edge cover. Its ten core edges are the pairs among $0,\ldots,4$. The other three edges are $uv,ua,vb$ for $c=5$ and $uv,u5,v5$ for $c=6$. All 2,048 choices of the two five-bit private contact sets and the optional edge $ab$ were checked at codegree five. The complete six-core gives one local $K_8$. All these cases satisfy all three conditions with seven packed triangles and 13 selected edges. Every ambient triangle through the chosen endpoints is in the corresponding local graph because their complete neighborhoods are specified. [Gupta, Lemma 7.2](https://arxiv.org/html/2608.06538v1#S7) · [Gupta, Lemma 8.4](https://arxiv.org/html/2608.06538v1#S8)

The codegree-five and codegree-six checks use the published definitions and Fano lists. The codegree-four catalogue and the complete seven-link bridge enter separately. [Five- and six-tip verification](../verification/check_gupta_56.py) · [Codegree-four verification](../verification/check_gupta.py)
