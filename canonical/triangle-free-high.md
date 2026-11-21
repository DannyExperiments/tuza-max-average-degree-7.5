# The triangle-free high-vertex graph

<a id="B"></a>

~~~text
           a₀ ─── a₁                    B is a cubic component on sevens
           │       │
           a₃ ─── a₂                    every vertex of B sees every aᵢ
               A                       all four highs form this induced cycle

                      one edge uv ∈ E(B)
                              aᵢ
                             ╱  ╲
                            u ── v      use the color i of uv

      Bought edges: E(B) and the four cycle edges in A.
      No other neighbor of a vertex of B exists.
~~~

**Theorem.** In every finite simple graph $G$, if the subgraph induced by $\{v:d_G(v)\ge8\}$ is triangle-free, then $\tau_\triangle(G)\le2\nu_\triangle(G)$. Equivalently the conclusion holds whenever every triangle contains a vertex of degree at most seven. The proof permits four-cycles and arbitrary degrees inside the high-vertex subgraph.

Suppose $G$ is a subgraph-minimal violation and write $H=\{v:d_G(v)\ge8\}$. Robustness gives minimum degree at least five. Every five and every nonthin six has at least three high subsumers, and subsumers of one low vertex are pairwise adjacent. The six high neighbors of a thin six induce an octahedron. Either low-vertex possibility already puts a triangle in $G[H]$. Thus, under the triangle-free hypothesis, every vertex outside $H$ is a seven. If there are no sevens, $G=G[H]$ has no triangle and satisfies the inequality. [Low-degree and subsumption inputs](low-vertex-reductions.md#local)

#### Each seven has a seven-neighbor on a spoke of codegree at least four

Fix a seven $y$. It has at least five incident edges of ambient triangle codegree at least four. Suppose every such edge goes to a high vertex. Let $X=N(y)\cap H,\ r=|X|$. We have $5\le r\le7$, and at least five vertices of the triangle-free graph $J=G[X]$ have degree at least $r-3$ in $J$. This follows by removing at most $7-r$ vertices from a rim in which these five vertices have degree at least four. For adjacent vertices of a triangle-free graph on $r$ vertices the two open neighborhoods are disjoint, so the sum of their degrees is at most $r$.

- If $r=7$, the five vertices of degree at least four must be independent by this degree-sum bound. Each then has at most two possible neighbors, a contradiction.
- If $r=6$, any vertex of degree at least four would have at least four neighbors of degree at most two. This contradicts the five vertices of degree at least three. Therefore each of the five relevant vertices has exactly three neighbors in $J$. Its fourth neighbor in the rim must be the unique seven there. That seven shares at least five high neighbors with $y$.
- If $r=5$, $J$ is triangle-free with minimum degree two. It has a cycle. A five-cycle with no four-cycle has no possible chord. If $J$ has a four-cycle, its fifth vertex needs at least two neighbors on the cycle. These must be opposite vertices, and neither a third contact nor a diagonal is possible. Thus $J$ is either $C_5$ or $K_{2,3}$. In $C_5$ all five high vertices must see both remaining sevens of the rim. In $K_{2,3}$ the three high vertices of degree two must see both sevens, and the two of degree three must each see at least one. Some seven consequently shares at least four high vertices with $y$.

In both latter cases a seven–seven spoke has codegree at least four, contrary to the assumption. This proves the claim for every seven. [Seven-link and paired-certificate analysis](seven-links.md#domain) · [Verification](../verification/check_quartet.py)

#### A component of sevens shares its entire four-cycle

For a wide seven–seven edge $yz$, the codegree-five and codegree-six pair reductions exclude those possibilities. At codegree four, exactly three cross-free signatures remain after the reviewed positive pair certificates. Their common vertices have ambient degree at least eight already on the union. Two signatures induce $K_4$ on them and would produce a high triangle. In the only remaining signature the four common tips form an induced $C_4=A_y$, and each of the four private vertices is adjacent to every member of $A_y$. A private vertex of degree at least eight would form a high triangle with either endpoint pair of any edge of the four-cycle. Therefore all private vertices are sevens. Since both root degrees are seven, their high neighborhoods are exactly $A_y$. This uses only necessary incidences surviving every optional private-edge choice. [Full pair domain and three signatures](paired-sevens.md#pair) · [Verification](../verification/check_quartet.py)

Apply this fact at every seven, choosing one wide seven-neighbor for each. At a given $y$, its other two seven-neighbors are private labels on its chosen pair, and see all four of $A_y$. Every seven has exactly four high neighbors, by the preceding paragraph applied at that seven. Thus **each** seven-neighbor of $y$ has the same high neighborhood $A_y$, irrespective of whether their joining edge is wide. By connectivity every component $B$ of $G[V(G)\setminus H]$ has one common $A$. Each vertex of $B$ has exactly three neighbors in $B$ and four in $A$. The component is triangle-free: two vertices of a triangle in $B$ would share all four of $A$ and the third seven, giving a forbidden seven–seven codegree of at least five. In particular $|V(B)|\ge6$ and $m=|E(B)|=3|V(B)|/2\ge9$.

#### Ambient reduction

A greedy edge coloring of the subcubic simple graph $B$ uses at most five colors, since at most four edges interfere with any edge being colored. Use its four largest color classes and assign them the four distinct vertices of $A$. For every selected edge $uv$ with color $a_i$, pack $uva_i$. The classes are matchings, so the triangles are edge-disjoint. Their number is at least $4m/5$. Buy $E(B)\cup E(G[A])$, a set of $m+4$ edges. Since $m\ge9$,
$$
         m+4\le 8m/5\le2|P|.
$$
Every triangle meeting $B$ either uses an edge within $B$, or has its other two vertices in $A$ and uses a bought cycle edge. Each packed edge is incident to $B$. After deleting $B$ and the purchases the surviving packing extends by $P$, and every surviving cover extends by the purchased edges. Thus this is a genuine reduction in the full ambient graph. Vizing's theorem would allow all $m$ edges to be packed; the elementary five-color argument suffices.

Lastly, for every subgraph $F\subseteq G$, $H(F)\subseteq H(G)$ and $F[H(F)]\subseteq G[H(G)]$. Triangle-freeness of the high subgraph therefore persists on taking a subgraph-minimal violation and gives the asserted result for all inputs. The additional seven-link and seven–seven certificate hypotheses used above hold in every subgraph-minimal violation.
