# Seven-neighbor links and common tips

<a id="quartet"></a>

## Four high neighbors and the degree-eight equality case

~~~text
   Full neighborhood of h                  A candidate large-codegree edge yz

             a     b                               y ─ z
              \   /                              / │   │ \
                h                            P_y   C   C   P_z
           / / / \ \ \                             ╰─ ─╯
          y₀ y₁ y₂ y₃ y₄ y₅                   C is the same set in both links

   Only the eight spokes at h are assumed.    The type and location of z are open.
   a,b are high. Each yᵢ has four highs.     Edges involving private tips are to be checked.
~~~

**Proposition.** Let $h$ have degree eight and exactly two high neighbors in a finite simple subgraph-minimal violation of Tuza, where *high* means degree at least eight. At least one of the six nonhigh neighbors of $h$ has five or more high neighbors. Indeed, the preceding bound gives four or more for each of the six, and the equality case in which all six have four is excluded below. Thus the degree-eight weight $5/2$ cannot occur. The finite graph $K_{2,2,3,3}$ realizes the stated degree and adjacency conditions on these ten vertices. A simultaneous triangle reduction excludes it from a minimal violation. Each of its six degree-seven vertices provably resists every singleton reduction. [Degree-eight weight and prerequisites](seven-links.md#two-high)

### Five incident edges of codegree at least four

The complete link of a seven in a minimal violation is connected by robustness. A weak König–Egerváry (WKE) matching and vertex-cover witness would reduce that seven. The recorded check decoded the 1,044 seven-vertex graph6 representatives. Within each degree partition, the recorded check canonically relabeled the graph and computed its automorphism count. The representatives are distinct and their orbit sizes sum to $2^{21}$, the number of all labeled graphs. the recorded check tested WKE by enumerating all 232 matchings in $K_7$ and all vertex sets of size equal to the matching size. Padding the smaller side includes every WKE witness. [Puleo, Lemmas 2.6 and 4.4](https://arxiv.org/pdf/1308.2211v3)

| Number of link vertices of degree at least four | 3 | 4 | 5 | 6 | 7 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Connected non-WKE link types | 3 | 12 | 34 | 42 | 26 |
| Received singleton certificates checked | 3 | 12 | 19 | 5 | 1 |

For every positive record the recorded check formed the actual cone. the check verified edge membership, disjointness of the packed triangles, payment for every packed rim edge, the twice-packing budget, and coverage of all triangles through the hub. There were 543 root triangles across the 40 records. All 15 types with at most four large link degrees have a positive certificate. Hence every seven in a minimal violation has at least five incident edges of ambient triangle codegree at least four. The claimed implication requires no decision about the optimality of the missing 77 certificates. Gupta's Lemma 4.5 gives three for connected non-WKE links and records equality examples. The five bound uses singleton irreducibility as an additional hypothesis. [Gupta, Lemma 4.5](https://arxiv.org/html/2608.06538v1#S4) · [Certificate data](../verification/data/SEVEN_CENSUS.json) · [Verification](../verification/four_high_audit.py) · [Certificate data](../verification/data/FOUR_HIGH_AUDIT.json)

### The four high neighbors of a seven

Let $d(y)=7$, and assume its high neighborhood $C_y=N(y)\cap H$ has size four. At least one edge $yz$ of codegree at least four goes to a nonhigh vertex. The following cases account for every ambient possibility. Every subsumer of a low vertex is adjacent to its entire open neighborhood apart from itself, so distinct subsumers are pairwise adjacent.

- If $d(z)=5$, then codegree four forces $N[z]\subseteq N[y]$, which Puleo's Lemma 2.7(e) forbids.
- If $d(z)=6$, then $z$ is nonthin by Puleo's Lemma 2.7(d). It has at least four high subsumers, all distinct from $y$ and adjacent to $y$. They are precisely $C_y$, so $G[C_y]=K_4$.
- If $d(z)=7$, the verified five- and six-tip pair reductions exclude codegree five or six. At codegree four, 3,283 of the 3,286 symmetry classes with connected non-WKE endpoint links already have certificates for every private cross-edge pattern. In each of the other three classes all four common tips have degree at least eight, so they constitute $C_y$. Their graph is $K_4$ in two classes and $C_4$ in the third. All four endpoint-private vertices are adjacent to all four common tips. In the cycle class both private pairs are independent.

Consequently $G[C_y]$ is $K_4$ or $C_4$. This deduction allows five- and six-neighbors in the full link before applying the stated restrictions. The three exceptional keys are recorded in the earlier independent pair audit. the recorded check decoded their core and private incidences again and verified positive two-root witnesses for all fifteen nonempty private cross-edge choices in the cycle class. [Puleo, Lemma 2.7 and proof of Lemma 2.8, pp. 5–6](https://arxiv.org/pdf/1308.2211v3#page=5) · [Five- and six-tip certificates](paired-sevens.md#gupta) · [Four-tip domain and exceptions](paired-sevens.md#pair) · [Certificate data](../verification/data/PAIR_AUDIT.json)

### Simultaneous occurrence at the eight

Suppose now that $h$ has degree eight, its only high neighbors are $a,b$, and its other six neighbors form a set $Y$ whose members each have four high neighbors.

Every member of $Y$ has degree seven. A five has at least three degree-nine-or-higher subsumers. They are all adjacent to $h$, contradicting the two-high-neighbor hypothesis. A nonthin six has at least four high subsumers, of whom at least three are different from $h$ and adjacent to $h$. A thin six has six high neighbors, so it cannot belong to $Y$. Robustness excludes smaller degrees.

Fix $y\in Y$ and choose $z$ as above. Since $h\in C_y$, a clique on $C_y$ would give a third high neighbor of $h$. Thus $z$ is a seven and the cycle class applies. Its common tips form the four-cycle with independent parts $\{h,k_y\}$ and $\{a,b\}$, since the two cycle neighbors of $h$ must be its two high peers. A priori $k_y$ depends on $y$.

The vertex $z$ and the two neighbors $p,q$ private to $y$ on this edge are all nonhigh neighbors of $h$, so all lie in $Y$. These are the three neighbors of $y$ outside $C_y$. Each sees every member of $C_y$ and has four high neighbors by assumption, so all three share $y$'s full quartet. The vertex $z$ misses $p,q$ by their definition. The cycle exception gives the further absence of $pq$. Thus the three neighbors of $y$ in $Y$ form an independent set. Applying the same argument to each $y$ gives a cubic, triangle-free graph on the six vertices of $Y$.

Choose one vertex $y$. Its three neighbors are independent, and each needs two incident edges beyond its edge to $y$. Only the two vertices of $Y$ outside that neighborhood and $y$ remain. All six required edges are present, so $G[Y]=K_{3,3}$. Along every edge of this connected graph the high quartets coincide. Write their common value as $C=\{h,k,a,b\}$. If $R=\{u_0,u_1,u_2\}$ and $B=\{v_0,v_1,v_2\}$ are the parts of $Y$, then every $u\in R$ has the exact full neighborhood $C\cup B$, and each $v\in B$ has the exact full neighborhood $C\cup R$. Hence the induced graph on these ten vertices is $K_{2,2,3,3}$ with parts $\{h,k\},\{a,b\},R,B$. Possible neighbors of the high vertices outside these ten do not enter either of the six root links.

The earlier pair result also closes this case directly. For the chosen edge $yz$ all four private cross edges exist in $K_{3,3}$, while any one suffices for the exceptional cycle pair certificate. This gives a second contradiction using the checked two-root bank. [Certificate data](../verification/data/PAIR_EXACT.json)

### A group reduction with individually irreducible roots

**Group rule.** Let $U=\{u_1,\dots,u_s\}$ be independent with one common full open neighborhood $W$, and put $J=G[W]$. Suppose matchings $M_1,\ldots,M_s$ in $J$ are pairwise disjoint as edge sets, and $2\sum_i |M_i|\ge |E(J)|$. Pack $u_i pq$ for each $pq\in M_i$ and buy $E(J)$. A matching prevents repeated spokes at its own root. Distinct roots have disjoint spoke sets. All packed rim edges are bought, and every triangle through $U$ uses a bought rim edge. Therefore any packing and cover in $(G-U)-E(J)$ extend at the stated cost. A sufficient test is $\chi'(J)\le2s$, since the $s$ largest color classes of a proper $2s$-edge-coloring contain at least half the rim edges. Vizing's theorem gives this whenever $\Delta(J)\le2s-1$. Puleo's Theorem 4.5 uses precisely the lifting of edge-color classes to independent roots in its proof of the packing formula for a join with a triangle-free graph. Here $J$ may have triangles. Buying the used rim edges also permits arbitrary surrounding triangles. [Puleo, Theorems 1.1 and 4.5, pp. 1 and 7–8](https://arxiv.org/pdf/1510.07017#page=7)

For the forced instance, $J=K_{2,2,3}$ has $4+6+6=16$ edges. Take $(c_0,c_1,c_2)=(h,k,a)$. Pack the nine triangles
$$
u_i v_j c_{i+j\pmod3}\qquad (0\le i,j<3)
$$
and buy the sixteen rim edges. All nine rim edges used in the packing are distinct. They are three disjoint edges within each matching, one matching per root. All $3\cdot16=48$ triangles meeting the roots are covered. An exterior triangle using a packed rim edge already meets a purchase, and an exterior vertex cannot be incident to a root since its full neighborhood is given. Thus $R$ is reducible in every ambient extension. For the ten-vertex graph itself, deleting $R$ and the purchases leaves an edgeless graph. [Certificate data](../verification/data/FOUR_HIGH_AUDIT.json)

**Each of these individual roots is irreducible in every graph with that full link.** First normalize any singleton certificate at $u$. A packed triangle containing a vertex outside $N[u]$ uses two purchased edges incident to that vertex. Neither edge can lie on a triangle through $u$, and neither belongs to another packed triangle. Remove the triangle and those two purchases. Repeat. Let the remaining root triangles use the rim matching $M$, and let $T$ be the packed triangles wholly in $J$. All edges in $M\cup E(T)$ are bought. Replace any additional bought rim edge by a spoke to one endpoint. Unnecessary exterior purchases can be discarded. If $Q$ is the set of bought spokes' other endpoints, $m=|M|$, $t=|T|$, $q=|Q|$, then
$$
E(J-Q)\subseteq M\cup E(T),\qquad m+3t+q\le2(m+t),\qquad q+t\le m\le3 .
$$

- If $t=0$, at least four vertices of $J$ remain after deleting $Q$. Any four vertices of $K_{2,2,3}$ include a vertex of induced degree at least two, contradicting the matching requirement.
- If $t=1$, at least five vertices remain. They span at least six edges, since the smallest five-vertex induced graph is $K_{2,3}$. More than six edges exceed the total $m+3\le6$. At equality the remaining $K_{2,3}$ contains at most two edges of $M$ and at most one edge of the rim triangle, again insufficient. Indeed a rim triangle uses one vertex from each of the three parts of $J$.
- If $t=2$, at most one vertex is deleted and at least $16-5=11$ rim edges remain, exceeding $m+6\le9$. If $t=3$, all sixteen remain, exceeding $m+9\le12$.

These exhaust the possibilities. Gupta's Proposition 4.9 uses the same root-matching and rim-triangle budget for $K_8$. The calculation here treats a different, explicitly occurring link and proves the group versus singleton distinction in the complete ambient sense. The reviewed structural conclusion concerns the degree-eight equality case. [Gupta, Proposition 4.9](https://arxiv.org/html/2608.06538v1#S4.SS1) · [Verification](../verification/four_high_audit.py)

<a id="domain"></a>

## The one-five nine, viewed from its known endpoints

~~~text
      full rim of x                       full rim of h

             h                              h sees all nine below
          ╱  │  ╲
         a ─ x ─ b                        x, a, b | p, q | s₁, s₂, s₃, s₄
          ╲  │  ╱                        x sees a,b,p,q; x sees no sᵢ
           p   q                         p,q see a,b; p and q are nonadjacent
              pq absent

      Inside the six labels D = {p,q,s₁,s₂,s₃,s₄}
         p,q have ≤2 other neighbors in D, each sᵢ has ≤3.
      Every chosen low t in a deletion has all its exits to outside N[h] bought.
~~~

The first view abbreviates the edges of $G[N(x)]=K_5-pq$ on $\{h,a,b,p,q\}$. The three sets in the second view distinguish vertex roles. Graph edges within $D$ and from $\{a,b\}$ to the four $s_i$ are variable. The drawing specifies two complete neighborhoods and leaves the ambient graph open.

**Proposition.** If the nine $h$ has exactly two high neighbors and subsumes the single five $x$, each of $p,q,s_1,\ldots,s_4$ is a seven with at least five high neighbors. Here a high vertex has degree at least eight. The full nine-link census is unnecessary for this conclusion.

#### Which seven-link theorem applies

In every finite simple subgraph-minimal violation, a seven $y$ with exactly four high neighbors has an induced $K_4$ or an induced $C_4$ on precisely those four vertices. The result applies when $y$ has a five- or six-neighbor. The hypothesis excluding such neighbors belongs to the subsequent theorem about groups of sevens sharing the same four highs. [Four-high-neighbor theorem](seven-links.md#quartet)

For the independent finite check, the verified catalogue accounts for all $2^{21}$ labeled seven-vertex graphs in 1,044 disjoint orbits. On each representative the recorded check tested WKE by fixing the spoke-vertex set $Q$. All edges avoiding $Q$ must form a matching extendible to a matching of size at least $|Q|$; this is sufficient as well as necessary. The connected non-WKE types have respectively 3, 12, 34, 42 and 26 isomorphism classes with 3, 4, 5, 6 and 7 rim vertices of degree at least four. For all 15 types with at most four such vertices, and for 25 further positive types, the check verified the actual singleton packing and purchases. Across these 40 records the 543 rooted triangles are all hit, and every packed edge avoiding the root is bought. Therefore every surviving seven has at least five spokes of ambient triangle codegree at least four. [Certificate data](../verification/data/SEVEN_CENSUS.json)

At least one of these five spokes leads to a nonhigh $z$ if $r(y)=4$. At a five, codegree four would make $y$ a subsumer of $z$, forbidden at degree seven. A six adjacent to a seven is nonthin. Its at least four high subsumers are adjacent to $y$, are pairwise adjacent, and hence exhaust the four highs and form an induced $K_4$. At a seven $z$, codegrees five and six have the ambient-safe pair reductions. the check reconstructed the five-tip and six-tip checks on all 1,024 and 32,768 labeled cores with their stated connected non-WKE and private-edge hypotheses. [Five- and six-tip cases](paired-sevens.md#gupta)

At codegree four the check reconstructed the enumeration over both connected non-WKE endpoint links. It includes 451,235 labeled pairs in 3,286 orbits under common-label permutations, both private-pair swaps, and root interchange. The 3,283 positive orbits passed on all 52,528 private-edge completions. The remaining three bit signatures are 8372190, 8372223 and 8388607. In the first the four common vertices have forced degrees $8,8,8,8$ in the pair union and have induced degrees $2,2,2,2$ on the common set, giving precisely $C_4$. In each other signature they have forced degrees $9,9,9,9$ and induced degrees $3,3,3,3$, giving $K_4$. These four actual common vertices therefore constitute all four high neighbors of $y$. All certificates address triangles at the two roots for every exterior completion, since both root neighborhoods are specified. [Verification](../verification/check_quartet.py)

#### The six neighbors at the nine

Let $N(h)\cap H=\{a,b\}$. The five $x$ has at least three high subsumers, one of which is $h$. The other two must be $a,b$; subsumers of the same vertex see one another, so $ab$ is an edge. The other six neighbors of $h$ are all nonhigh. A second five would either be subsumed, contrary to the single-five hypothesis, or have three high subsumers distinct from and adjacent to $h$, contrary to its two high peers. A nonthin six would have at least three high subsumers distinct from and adjacent to $h$, with the same contradiction. A thin six adjacent to $h$ would collect a payment; moreover, the four neighbors of $h$ in its octahedral link are all high peers of $h$. Robustness excludes smaller degrees. Thus all six are sevens. [Subsumption and low-neighbor rules](low-vertex-reductions.md#local)

Fix any of these six, say $t$. The earlier seven-link reductions give $r(t)\ge4$. If equality held, $h$ would belong to its four-high induced graph. In $K_4$ it would see three high peers. In $C_4$ its two cycle neighbors would be $a,b$, and those two vertices would be nonadjacent. Both cases contradict the actual neighborhood of $h$. This proves $r(t)\ge5$ for each of the six separately.

For this row the ratio is therefore at most
$$
 \frac{1+1/3+6/5}{\,2-2/3\,}=\frac{19}{10}.
$$
The numerator counts $h$, the one five, and the six sevens. At a nine subsuming only one five with $j\ge3$ high peers, the existing weight bound $1+(9-j)/4+1/12$ gives $w/s'\le31/16$. The finite checks used above concern only the seven-link and seven–seven pair inputs. The conclusion holds for arbitrary adjacencies among the six and arbitrary exterior vertices.

<a id="two-high"></a>

## Every degree-eight vertex has at least two high neighbors

~~~text
       viewed from the center h                    viewed from a selected seven y

                a ─ b                                     a ─ b
                 ╲ ╱                                       ╲ ╱
             y ── h ── z                                   h
                  ╲                                       ╱ ╲
                 other rim vertices                      u   v        s   t

       a,b are the other highs of y.              u,v are the two lower contacts in N(h).
       The high pair of z may differ.             s,t are outside the closed neighborhood of h.
~~~

The labels in the right-hand view belong to the full link of $y$. The adjacencies between its four lower vertices depend on which of the three exact link types is realized.

**Theorem.** Let $G$ be a finite simple subgraph-minimal violation of Tuza's triangle packing–covering inequality, and call a vertex high if its degree is at least eight. Every degree-eight vertex $h$ has at least two high neighbors. Furthermore, each nonhigh neighbor of $h$ has at least four high neighbors. Consequently
$$
w(h)=1+\sum_{y\in N(h),\ d(y)\le7}\frac1{|N(y)\cap H|}\ \le\ \frac52 .
$$
This rules out the entire one-high-neighbor case, including assignments in which some of the seven remaining neighbors have more than four high neighbors. Attainment of $5/2$ would require exactly two high neighbors of $h$ and exactly four high neighbors of each of its six other neighbors.

### The one-high-neighbor case

Write $L=G[N(h)]$ for the complete link. Suppose $b$ is the only high neighbor of $h$. Every vertex $y\in V(L)-b$ has at least three high neighbors. If it had exactly three then, by the previously proved triangle property, its two high neighbors other than $h$ would both be adjacent to $h$. Thus $y$ has at least four high neighbors and at most $7-4=3$ nonhigh neighbors in the whole graph. In particular $\Delta(L-b)\le3$. When $h$ has zero high neighbors the identical argument gives $\Delta(L)\le3$, so deleting any label $b$ gives the same necessary condition. The argument so far uses the previous triangle property alone. [High-neighbor theorem](seven-links.md#two-high)

Each component of a link in $G$ has order at least five by Puleo's reduction, so $L$ is connected. Also $\delta(L)\ge2$. An edge in zero triangles can be discarded. If $hy$ is in exactly one triangle $hyt$, delete all three edges of that triangle, pack $hyt$, and buy $ht,yt$. Every triangle lost in the deletion meets the purchases, including the only one using $hy$. This reduces any graph having such an edge. [Puleo, Lemmas 2.2, 2.6 and 4.3–4.4](https://arxiv.org/pdf/1308.2211v3)

If $L$ has a matching $M$ and a set $Q$ of at most $|M|$ vertices meeting each edge outside $M$, then $L$ is weak König–Egerváry (WKE). Packing $hij$ for $ij\in M$ and buying $M\cup\{hq:q\in Q\}$ removes $h$ at cost at most two per packed triangle. It follows that $L$ is non-WKE. [Puleo, Definition 4.1 and Lemma 4.4](https://arxiv.org/pdf/1308.2211v3#page=10)

Here are all isomorphism types of an eight-vertex link left by these requirements.

| Condition | Unlabelled graphs |
| --- | ---: |
| Connected, with some vertex $b$ such that $\Delta(L-b)\le3$ | 3,833 |
| Same conditions and $\delta(L)\ge2$ | 1,769 |
| Same conditions, $\delta(L)\ge2$, and WKE | 1,768 |
| Same conditions, $\delta(L)\ge2$, and non-WKE | 1 |

The sole graph in the last row is graph6 `GEhuVc`. Use labels $0,\ldots,7$ and $h=8$. Only $b=7$ qualifies in these labels. Its full edge list is

~~~text
03  04  06  07    13  15  16  17    24  25  27    35  37    46    67
~~~

Pack the rim triangle $046$ and the four hub triangles $038,158,248,678$. The latter use a perfect rim matching, and all five triangles are edge-disjoint. Buy the seven packed rim edges
$$
03,04,06,15,24,46,67
$$
and the three spokes $18,58,78$. The remaining eight rim edges are $07,13,16,17,25,27,35,37$. Each is incident to $1,5$ or $7$, so its triangle with $h$ meets a bought spoke. The left view records all 15 possible triangles at $h$, one per rim edge. The right view verifies that the four hub triangles use every spoke exactly once.

Let $X$ denote these ten purchases and $G'=(G-h)-X$. Every packing in $G'$ extends by all five listed triangles, since each used edge avoiding $h$ belongs to $X$. Every cover of $G'$ extends by $X$, since the root triangles have all been met. This argument permits arbitrary exterior edges and triangles, including triangles using a packed rim edge. Applying the inequality to $G'$ contradicts the choice of $G$.

### Fractional weight and contacts

Every degree-seven vertex has at least four high neighbors by the three verified singleton reductions and the earlier seven–seven codegree certificates. The ordinary exact-three set $A_h$ is therefore empty for every high $h$, giving $2|E(G[A_h])|=|A_h|=0$ in the original question. For a degree-eight $h$, every adjacent degree-five vertex has at least three degree-nine-or-higher subsumers, in addition to its high neighbor $h$. A nonthin six has at least four high subsumers and a thin six has six high neighbors. As vertices of degree at most four are excluded, every nonhigh neighbor of this $h$ contributes at most $1/4$. There are at most six such neighbors by the theorem, giving $w(h)\le5/2$. [Singleton certificates and seven–seven transfer](seven-links.md#three-high) · [Puleo's low-vertex restrictions](donor-lemmas.md#high-donors)

### Completeness and falsification

The existing eight-vertex graph6 catalogue has 12,346 distinct isomorphism types. Its checked sum of labeled orbit sizes is $268435456=2^{28}$, the number of labeled simple graphs on eight vertices. The replay fixes its SHA-256 and examines every vertex $b$ of every representative. Our first WKE test forces every edge outside a candidate $Q$ into the matching and then extends it. An independent test enumerates all 764 matchings of $K_8$, including the empty matching. For a matching $M$ contained in $L$ it tries each vertex set of size $|M|$ for $Q$. Padding $Q$ proves that this includes every WKE witness. The two counts agree. The independent replay also checks the five actual packed triangles, the bought edges and all fifteen root triangles directly.

Dropping $\delta(L)\ge2$ leaves nine non-WKE graphs among the 3,833. An exhaustive test restricted to packed triangles in the closed neighborhood of $h$ finds a singleton reduction for five of these nine graphs. Four resist this particular test. Each of those four has two leaf spokes and admits the direct single-edge reduction above. Across all nine, eight have leaves.

The preliminary contact test compared marked eight-vertex rims with the possible induced four-vertex subgraphs in each selected seven's full link. Under its listed filters, 88 of 34,792 labeled assignments on catalogue representatives gave $2|E(G[A_h])|>|A_h|$, across 22 rim isomorphism types. These assignments describe compatible projections one vertex at a time. The three ambient singleton reductions eliminate every actual member of $A_h$.

Kandasamy's Lemma 3.1 covers a connected subcubic link of minimum degree at least two and order at most ten, with two exceptions of order ten. It directly handles the degree-eight zero-high case. The exceptional link above has maximum degree five and becomes subcubic upon deletion of vertex seven. Puleo's general reduction permits the extra rim triangle used in its certificate.   The present calculation leaves the occurrence of equality at $5/2$ open. [Kandasamy, Lemma 3.1](https://arxiv.org/html/2610.15269v1#S3.SS1) · [Puleo, Definition 2.1](https://arxiv.org/pdf/1308.2211v3#page=4)

<a id="eight-spokes"></a>

## A degree-eight vertex subsuming a nonthin degree-six vertex

~~~text
           C = {0,1,2,3,4}: all pairs, possibly except 34
                    ╱  ╲
                   x ── h ── a
                  d6    d8 ╲ b
~~~

Both roots join every member of $C$. Of the two roots, only $h$ joins $a,b$. All ten private-to-common contacts and $ab$ are optional. Other vertices may attach to $C,a,b$, while $N(x)=C\cup\{h\}$ and $N(h)=C\cup\{x,a,b\}$ are the complete ambient neighborhoods.

**Proposition.** If $G[C]$ is $K_5$ or $K_5$ with one edge removed, then $\{x,h\}$ is reducible for every choice of private contacts. In a subgraph-minimal violation, subsumption of a nonthin six guarantees these core hypotheses by Puleo’s Lemma 2.7(a). [Puleo, Lemmas 2.7 and 2.8](https://arxiv.org/pdf/1308.2211#page=6)

**Certificate.** On the seven labels $x,h,0,1,2,3,4$, take the triangles

$$
xh0,\quad x12,\quad x34,\quad h13,\quad h24,\quad 014,\quad 023.
$$

Their 21 edges are exactly the 21 distinct pairs of labels. With the complete core this packs all seven triangles. With a missing core edge $e$, omit the unique triangle containing $e$. For the pictured missing edge $34$ the omitted triangle is $x34$.

Buy $X=E(G[C])\cup\{xh,ha,hb\}$. A triangle through both roots meets $xh$. A triangle through just one root and a private vertex meets $ha$ or $hb$. Every other triangle through a root uses an edge of $G[C]$. All off-root edges of the packed triangles also lie in $E(G[C])$. The resulting sizes $(\lvert S\rvert,\lvert X\rvert)$ are $(7,13)$ for $K_5$ and $(6,12)$ for $K_5-e$. Thus the two roots satisfy all three conditions of a Puleo reduction in the full ambient graph. In particular, an eight cannot pay a nonthin six in the discharging argument. Combined with the previously checked exclusions for fives and thin sixes, every eight has final surplus one. [Previous discharging dependencies](low-vertex-reductions.md#local)

Gupta’s Lemma 8.4 uses these Fano lines for the complete five-core with one private spoke at each endpoint. Paying the two private spokes at $h$ gives the corresponding degree-six/degree-eight case. Kandasamy’s Lemma 3.8 also deletes the Fano line through a missing core edge in its codegree-five argument. The argument here permits every contact at the two private vertices. [Gupta, Lemma 8.4](https://arxiv.org/html/2608.06538v1#S8) · [Kandasamy, Lemma 3.8](https://arxiv.org/html/2610.15269v1#S3.SS2)

**Independent finite check.** For each core the verifier enumerates every one of the $2^{11}=2,048$ private-edge patterns. It also runs the one-edge deletion on each of the ten labeled core edges, producing 22,528 graphs altogether. Every packed edge existed, all packed triangles were edge-disjoint, every off-root packed edge was bought, and all 646,144 occurrences of triangles meeting a root were hit. External contacts cannot add a triangle through a root because both root neighborhoods have been specified in full.

<a id="three-high"></a>

## A four-triangle reduction of one degree-seven vertex

~~~text
                              root 7
                     / / /     |     \ \ \
                    0 1 2      3      4 5 6        complete list of neighbors

                 first two links                  third link
                 rim triangle 034                 rim triangle 136
                 spoke pairs 05,13,24             spoke pairs 02,14,35
                 buy spokes 75,76                 buy spokes 70,72
~~~

“Spoke pair $ij$” means pack the triangle $7ij$. The rim triangle uses three edges of the actual induced link. Buying all six packed rim edges and the indicated two spokes costs eight. The unbought rim edges in the table show exactly where the two spokes are needed.

**Local theorem.** Let $v$ be any vertex of a finite simple graph whose complete link is one of the following three seven-vertex graphs. Then $\{v\}$ is a reducible set. Consequently, every vertex of degree seven in a subgraph-minimal violation has at least four incident edges of triangle codegree at least four.

| Complete link of $7$ | Packed triangles | Bought rim edges | Remaining rim edges | Bought spokes |
| --- | --- | --- | --- | --- |
| FEnbo | 034, 057, 137, 247 | 03, 04, 05, 13, 24, 34 | 15, 16, 25, 26, 36, 46 | 57, 67 |
| FEnf_ | 034, 057, 137, 247 | 03, 04, 05, 13, 24, 34 | 06, 15, 16, 25, 26, 36 | 57, 67 |
| FQyv_ | 027, 136, 147, 357 | 02, 13, 14, 16, 35, 36 | 04, 05, 06, 24, 25, 26 | 07, 27 |

The two rim columns give the complete edge lists. In each row the four triangles have twelve distinct edges. Every edge used by the packing away from $7$ occurs in the bought rim column. Each of the six remaining edges has an endpoint whose spoke is bought. Hence the purchased set $X$ meets every one of the twelve triangles through $7$.

For an arbitrary ambient graph $G$, put $G'=(G-v)-X$. All four packed triangles are edge-disjoint from every packing in $G'$. Any triangle of $G$ avoiding $X$ also avoids $v$, so is a triangle of $G'$. Thus $\nu(G)\geq\nu(G')+4$ and $\tau(G)\leq\tau(G')+8$. These hold with arbitrary edges from the link vertices to the outside and with arbitrary triangles away from $v$. Subgraph minimality now forbids the displayed link.

**From three links to four large codegrees.** Robustness makes a seven-vertex link connected in a subgraph-minimal violation. A WKE link gives a reducible singleton by Puleo. Gupta’s Lemma 4.5 gives at least three vertices of link degree at least four in the remaining connected non-WKE case. The independently checked equality catalogue gives precisely the three rows above. Buying the rim of one packed link triangle explicitly certifies a singleton reduction in each. The complete link $K_7$ in Gupta’s singleton obstruction has seven large vertices and lies outside this three-row catalogue. [Equality catalogue and original edge lists](seven-links.md#two-high) · [Puleo, Definitions 2.1–2.3 and Lemma 4.4](https://arxiv.org/pdf/1308.2211v3#page=4) · [Gupta, Lemma 4.5 and Proposition 4.9](https://arxiv.org/html/2608.06538v1#S4)

**Every seven has at least four ambient high neighbors.** Here a high vertex has degree at least eight. Suppose a degree-seven vertex $v$ has at most three such neighbors. Robustness gives minimum degree five. A seven cannot neighbor a thin six. Every nonthin six $x$ has at least four high subsumers, and all are adjacent to every seven in $N(x)$, since a seven cannot itself subsume a six. Thus $v$ has no degree-six neighbor. For a degree-five neighbor $x$, triangle codegree four on $vx$ would put $N[x]\subseteq N[v]$, also forbidden. So every five accounts for a spoke of codegree at most three. [Puleo, Lemma 2.7 and proof of Lemma 2.8](https://arxiv.org/pdf/1308.2211v3#page=6)

For a degree-seven neighbor $w$, codegrees five and six on $vw$ reduce the pair using its actual connected non-WKE endpoint links. At codegree four the previously checked pair catalogue reduces every pair having at most three common vertices of local degree greater than five after omitting the endpoints. Each such exceptional common vertex has ambient degree at least eight and is a neighbor of $v$. Our hypothesis therefore enforces that catalogue bound. Thus only the high neighbors of $v$ can provide spokes of codegree at least four. The local theorem gives at least four such spokes, contrary to the hypothesis. In particular $A_h=\varnothing$ for every high $h$. [Codegree-five and -six verification](paired-sevens.md#gupta) · [Three-defect codegree-four reduction](paired-sevens.md#pair) · [Certificate data](../verification/data/PAIR_AUDIT.json)

**Verification and scope.** A direct comparison of the edges and costs with the supplied edge lists checks every rooted triangle, every packed edge, and the complete rim in each representative. Relabeling covers the input catalogue’s $840+2520+1260=4620$ labeled links. The proof stops at these local reducibilities and their ambient incidence consequence.
