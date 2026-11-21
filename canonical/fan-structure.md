# High-triangle components and marked seven-links

<a id="component"></a>

## Exactly one ordinary high fan

~~~text
                 a                         high triangle intersection graph
               / | \ \                        abx ─── abc ─── acz
              x──b──c──z

  a sees x,b,c,z. The four other vertices induce exactly the path x–b–c–z.
  The seven fan edges split into the spokes ab,ac shared by its high faces
  and the outside cycle a–x–b–c–z–a, each side on one high face.
~~~

**Proposition.** All proposed inputs hold when a copy means a specified edge-subgraph, with reversal of the rim path counted once. A high vertex has degree at least eight in the whole graph. The mild refinement on exterior tip overlap is recorded below.

Let $\mathcal T$ have one vertex per high triangle, adjacent exactly when their edge sets intersect. Every induced three-vertex path in $\mathcal T$ has middle triangle $abc$, with its neighbors sharing different sides $ab,ac$. Write those neighbors $abx,acz$. Then $x\ne z$ because the end triangles share no edge. Their seven-edge union is the fan centered at $a$ on the path $x,b,c,z$. Conversely each ordinary fan edge-subgraph has exactly these three triangles within its own edge set, and they induce a three-vertex path in $\mathcal T$ irrespective of any extra ambient edges. These constructions are inverse.

In any graph containing exactly one induced path $L-M-R$ on three vertices, the path is its whole connected component. If an outside vertex adjacent to $M$ misses $L$ or $R$, it creates another path through $M$; if it sees both, $L$ and $R$ make a path through it. If it misses $M$ but sees an endpoint, that endpoint and $M$ give another path. Thus the three fan triangles share no edge with any other high triangle. Moreover any additional edge among $x,b,c,z$ closes a further high triangle with $a$ sharing one of the seven fan edges. Hence the support on the five vertices is induced.

Every other component of $\mathcal T$ is a clique, since a connected nonclique contains an induced three-vertex path. Pairwise edge-sharing triangles either share one common edge or form the four faces of a tetrahedron. Indeed, for two pages $uvs,uvt$, a third triangle meeting both but missing $uv$ must be $ust$ or $vst$. The fourth face then exists and belongs to the same component. No exterior triangle can share an edge with all four faces. This gives precisely books, singleton triangles and tetrahedra away from the seven fan edges.

In a subgraph-minimal violation every edge has ambient triangle codegree at least two, by the elementary zero- or one-triangle reductions. Each of $ax,xb,bc,cz,za$ consequently has a nonempty set of tips outside the five labels. All those vertices have degree at most seven since none can create another high face on the side. The smallest possible number of externally occupied fan edges allowed by this count is five. At this count $ab,ac$ are clean. Any exterior tip seeing $a$ then misses both $b$ and $c$. Thus the union of the tip sets of $ax,az$ is disjoint from the union for $xb,bc,cz$. Within-group overlaps are permitted by this incidence argument. A tip on both $xb$ and $cz$ necessarily lies on $bc$. For a bare incidence check, outside vertices with contacts $\{a,x,z\}$ and $\{x,b,c,z\}$ respectively realize both overlaps while keeping the two spokes clean; private leaves can raise the five displayed vertices to degree eight. This example concerns the high fan and its named tip sets.

The class with at most one such high fan is hereditary: deleting edges or vertices removes fan edge sets and can only lower degrees. A violation in the class must have exactly one fan by the preceding theorem. For each of its seven edges $e$, deleting $e$ destroys its only high fan. So $G-e$ satisfies Tuza. Writing $p=\nu(G)$ gives

$$
 2p+1\le\tau(G)\le1+\tau(G-e)\le1+2\nu(G-e)\le1+2p .
$$

Consequently every single deletion has $(\nu,\tau)=(p,2p)$, and $\tau(G)=2p+1$. This last calculation holds for any violating graph in the class. The minimum-codegree assertion above uses subgraph minimality. [Independently checked high-fan occurrence theorem](fan-structure.md#occurrence)

<a id="marked"></a>

## The five marked seven-neighborhoods

~~~text
            look along the seven–seven edge yz from either endpoint

           single-edge type                         path type
              h₁ ── h₂     h₃                        h₁ ── h₂ ── h₃

    All vertices drawn are in N(y) ∩ N(z). Adjacencies among these three
    vertices are intrinsic to that edge, independent of the endpoint view.
    The census below tests when these are the only types that can occur.
~~~

**Hypothesis and conclusion.** Suppose a finite simple subgraph-minimal Tuza violation has no triangle of high vertices containing two sides that each belong to at least two high triangles. Here high means degree at least eight. Its nonhigh vertices are all sevens. Each component they induce is an isolated vertex, a path with alternating edge types, or an even cycle with alternating edge types. The type of an edge is the graph on its three common neighbors in the whole graph. The conclusion uses the seven-link and wide-pair reductions.

**Applicability.** A high $K_4$ has three repeated sides on every face. In a high wheel over a square each triangular sector has its two spokes repeated. This also excludes the high octahedron, which contains such a wheel. Hence there are no sixes: a nonthin six would supply a high $K_4$, and a thin six a high octahedron. A five has three mutually adjacent high subsumers and requires two seven-neighbors. On a wide edge between sevens the surviving clique quartet is excluded, and a private high on the surviving square quartet would form that high wheel. A private five seeing all four corners is subsumed by a seven. The old closed cubic-square component reduction therefore still excludes a wide seven–seven edge. A seven cannot subsume a five. Thus every wide neighbor of a seven is high. [Puleo’s minimal-counterexample reductions](https://arxiv.org/pdf/1308.2211v3#page=5)

**Full seven-link census.** Starting from the audited 77 seven-rims, mark the actual high positions in all 128 ways. Retain the 159 of 9,856 markings assigning every wide spoke a high endpoint. For each such marking count the high triangles on every edge *within the marked induced rim*. Reject the row if any of these triangles has two sides of local count at least two. Direct enumeration gives the following five rows. The labels $(a,b,c,d,U,t,V)$ in the earlier drawing are $(0,1,2,3,4,5,6)$. `FEzvO` contains all nine edges between $\{0,1,2\}$ and $\{4,5,6\}$, plus $46,03,13,35$. `FFzvO` adds just $23$.

| Complete rim | Nonhigh positions | Locally repeated high edges |
| --- | --- | --- |
| `FEzvO` | 2, 3 | 46 |
| `FEzvO` | 3 | 46 |
| `FEzvO` | 2 | 35, 46 |
| `FEzvO` | None | 35, 46 |
| `FFzvO` | None | 35, 46 |

Every nonhigh neighbor in position 2 has common neighbors $4,5,6$ with the root, all high, spanning exactly the edge $46$. In position 3 its three common neighbors are $0,1,5$, all high, spanning the path $0-5-1$. A five at either slot would have its three pairwise adjacent high subsumers in this very common neighborhood, impossible in both cases. No five can occur since every five requires a seven neighbor. The all-high rows give isolated sevens, and the one-nonhigh rows give degree-one vertices in the seven-induced graph. In the two-nonhigh row the root has one incident edge of each of the two types. Each edge has the same intrinsic common-neighbor graph at both endpoints, so its type is well defined and adjacent edges on a path or cycle alternate. Every such cycle is even. A component consisting of a single edge is included.

**Exterior distinction.** A local repetition implies a global high repetition, so every rejected row is impossible. A locally unique side can acquire another high tip outside the root neighborhood. In a checked pair of actual graphs the same `FEzvO` rim at vertex 7 has nonhigh positions 2 and 3, each of ambient degree seven. The base graph satisfies the global condition. Attaching the already-high outside vertex 8 to 0 and 4 preserves the rim and all high labels but makes $04$ repeated as well as $46$ on the old triangle $046$. The five surviving rows give necessary local possibilities only. No existence in a minimal violation or reduction for the paths and cycles is asserted. [Verification](../verification/fan_domain.py)

<a id="occurrence"></a>

## A fan in the high layer of every counterexample

~~~text
                full rim at y                      look back from r to y

       0────1    Q = {0,1,2,3}             common neighbors: 0,1,s
        \  /     all six Q edges exist               0────1    s
          r────s                            s has degree at most seven
              / \                           in the surviving seven-rim row.
             2───3

        q is joined to all four corners and neither r nor s.
        y sees all seven labels. Other ambient edges remain unrestricted.
~~~

**Proposition.** Every finite simple graph whose degree-at-least-eight vertices induce a graph containing no $K_1\vee P_4$ as an ordinary subgraph satisfies $\tau_\triangle(G)\le2\nu_\triangle(G)$. Thus every Tuza counterexample contains five high vertices supporting this fan. Extra edges between them are allowed.

**Inherited reductions.** Write $H=G[\{v:d_G(v)\ge8\}]$. The forbidden-subgraph hypothesis passes to arbitrary subgraphs because high vertices and edges can only disappear. In a subgraph-minimal violation, minimum degree is at least five and vertices of degrees five and six are independent. A seven has at least five incident edges of triangle codegree at least four; call such edges wide. A seven cannot subsume a five. Two adjacent sevens cannot have five or six common neighbors. At codegree four, the only surviving two-root possibilities have four *high* common neighbors inducing a square or a clique, with every private label seeing all four. Both roots have precisely two private labels. These are statements about full neighborhoods in the ambient graph. [Puleo, Lemmas 2.6–2.7](https://arxiv.org/pdf/1308.2211v3#page=5) · [Five-wide input and its finite domain](seven-links.md#quartet) · [Positive four-tip reductions and three remaining signatures](paired-sevens.md#pair) · [Five- and six-tip reductions](paired-sevens.md#gupta)

In a fan-free $H$, every high vertex outside a high tetrahedron $Q$ sees at most one vertex of $Q$: an outside vertex $x$ seeing $a,b\in Q$ gives center $a$ over the path $x,b,c,d$, where $Q=\{a,b,c,d\}$. Distinct high tetrahedra therefore share at most one vertex.

**Sixes and the square pair.** A thin six supplies a high octahedron containing a high fan. The complete link of a nonthin six $q$ lacks at most one edge and has at least four high subsumers. If five of its vertices were high, their induced graph would contain $K_5$ minus at most one edge, which contains a fan. Thus exactly four neighbors are high and form the subsumer tetrahedron $Q$. The remaining two are sevens by low-degree independence. They are nonadjacent: each must fail to subsume $q$, and there is at most one missing link edge. Both see all of $Q$. Call a seven *special* when it sees an entire high tetrahedron, and *normal* otherwise.

On a wide seven–seven square pair, any high private vertex forms a high fan over three consecutive square sides. A private six is excluded because its four high neighbors form a clique. A private five seeing the quartet has exactly the four tips and its seven endpoint as neighbors, and that endpoint subsumes it. Thus all private labels are sevens. Every one of the three seven-neighbors of an endpoint sees the same high square and makes another wide joining edge. The pair classification propagates through the component, since all four common vertices are that square. The resulting triangle-free cubic component joined to an induced high square reduces by its four corner colors, as previously verified. Hence a wide seven–seven pair can only have a high clique quartet. In this case all private labels are nonhigh, because they see a high tetrahedron. At either endpoint its complete high neighborhood is precisely the quartet and its three remaining neighbors see the whole quartet. [Ambient square propagation and purchases](book-forest.md#tetra)

**A special seven without a wide seven-neighbor.** Fix a tetrahedron $Q$ seen by such a seven $y$. Every high neighbor of $y$ outside $Q$ has at most one neighbor in $Q$, and at most two others in the full seven-rim. Hence it is narrow. Every adjacent five is also narrow, since a seven cannot subsume a five. The five-wide lower bound now supplies a six-neighbor $q$. The four high neighbors of $q$ are all adjacent to $y$. Its tetrahedron must be $Q$: $y$ has at most six high neighbors, whereas distinct tetrahedra have union size at least seven. If another six also neighbored $y$, their neighborhoods would both consist of $Q,y$ and one further seven each. Their union would have size at most seven. Lemma 3.3(a) of Botler, Fernandes and Gutiérrez prohibits two sixes with that property in an irreducible robust graph. This lemma has no treewidth restriction. [Primary Lemma 3.3](https://arxiv.org/pdf/2002.07925#page=4)

Name the last two neighbors of $y$ as $r,s$. The other seven-neighbor of $q$ misses $y$, so neither $r$ nor $s$ sees $q$. Each has degree at most three in the rim, by high-fan avoidance, the five subsumption exclusion and the no-wide-seven-neighbor assumption. Each has rim degree at least two, since a graph edge on zero or one triangle reduces in a subgraph-minimal violation. The five vertices $Q\cup\{q\}$ induce $K_5$.

The recorded check enumerated all these actual rooted rims **without** using the 77-rim catalogue for this step. Label $Q=0123,\ q=4,\ r=5,\ s=6,\ y=7$. Fix $\delta=\mathbf1_{rs\in E}$ and ordered subsets $X=N(r)\cap Q,\ Y=N(s)\cap Q$. The constraints are $2\le |X|+\delta,|Y|+\delta\le3$. For either value of $\delta$ there are ten choices for each subset, hence 200 labeled rims. Up to permuting $Q$ and interchanging $r,s$, the key $(\delta,\min(|X|,|Y|),\max(|X|,|Y|),|X\cap Y|)$ determines a rim and gives 14 types. The recorded check generated a direct reducing packing and cover for 13 types and verified each transported certificate on every one of their 194 labeled instances. Each purchase covers all triangles at $y$ and buys every packed edge surviving deletion of $y$. The six remaining instances have the single key $(1,2,2,0)$. Thus $r,s$ are adjacent and see complementary tetrahedron pairs. Both are nonhigh by the one-corner bound. This proves that **every special seven has exactly its four tetrahedron corners as high neighbors**, in both the wide-pair and the no-wide-pair branches.  · [Verification](../verification/check_special_seven.py)

**Normal sevens and fives.** A six-neighbor would make a normal seven special, and every remaining wide seven–seven pair has a clique quartet. A five-neighbor is narrow. Thus the wide neighbors of a normal seven are high. Its marked high rim is both fan-free and tetrahedron-free, so it has no high triangle with two repeated *local* sides. The five previously checked markings apply to each normal seven separately, even if other sevens see tetrahedra. In them every nonhigh slot has exactly three common neighbors with its root. Those three are high and induce one edge or a three-vertex path. [Exact marked-link input, replayed in this round](book-forest.md#tetra)

Each five $x$ must neighbor a seven; if all its neighbors were high, their complete link missing at most one edge would give a high fan. Its three pairwise adjacent high subsumers see any seven $y$ adjacent to $x$. This is incompatible with the nonclique triple at a normal seven. At a special seven on a wide seven pair, $x$ would see all four corners and be subsumed by $y$. At a special seven in the no-wide-pair row, $x$ would occupy $r$ or $s$, seeing just two corners, although its three high subsumers all belong to $N(y)\cap H=Q$. These cases exclude all fives.

In the remaining no-wide-pair row, $r,s$ must be sevens since $q$ is the unique six-neighbor of $y$. If $r$ is normal, its three common neighbors with its nonhigh neighbor $y$ must all be high, whereas one of them is $s$. If $r$ is special, its complete high neighborhood is a tetrahedron $R$ containing its two neighbors in $Q$. Necessarily $R=Q$, whereas $r$ misses the other two corners. This rules out the row. Every special seven is therefore on a wide seven–seven pair and its three nonhigh neighbors all see its own $Q$.

**Closing the components.** Start from any special seven or six. Its only high neighbors are its four corners $Q$, and every nonhigh neighbor is a special seven or six with the same $Q$. For a neighboring six this follows from its full high neighborhood; for a neighboring seven it follows from the complete special-seven classification. Thus the whole nonhigh component $B$ containing the chosen vertex is attached to this one tetrahedron with no other exits. Its degrees within $B$ are two at sixes and three at sevens. It is triangle-free: two sevens in any low triangle would share $Q$ and the third vertex, and a low triangle must have two sevens since sixes are independent. Hence $m=|E(B)|\ge4$. By Vizing's simple-graph theorem $B$ has a proper edge-coloring with at most four colors. Use the four corners of $Q$ as colors. Pack all $m$ colored-edge triangles with their assigned corners, and one additional face of $Q$. The triangles are edge-disjoint. Buy $E(B)\cup E(Q)$, at cost $m+6\le2(m+1)$. This meets every triangle at $B$. The internal tetrahedron face is the only packed triangle with edges avoiding $B$, and all its edges are bought. Deleting $B$ and the purchases gives a proper subgraph from which every packing and cover lifts. It does not matter if high tetrahedra share a vertex, or if other low components use the same $Q$.

No special seven or six survives this reduction. There are no fives. A five-clique with four high vertices would consist of a high tetrahedron and a special seven, or would be a high five-clique, which itself contains a high fan. Both possibilities are excluded. The preceding checked theorem for a fan-free high layer with no such five-clique now finishes the proof, including the all-high case. [Previous signed transfer](book-forest.md#tetra)

This argument uses the local reductions above. The case of a unique fan is treated in [Two distinct high fans](two-fans.md).
