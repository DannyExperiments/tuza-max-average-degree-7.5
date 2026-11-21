# Low-degree links and the initial charge

<a id="local"></a>

~~~text
       surrounding graph       N(v) ∩ N(w) = C         surrounding graph
             U                 c₁   …   cₜ                  W
          ╲  │  ╱               ╲ ╲   ╱ ╱               ╲  │  ╱
            [v] ───────────────────────────────────────── [w]
          d(v)=7                edge vw                  d(w)=7
            U = N(v) \ N[w]                      W = N(w) \ N[v]

       low receiver u        neutral donor h           low receiver u′
       d(u) ∈ {5,6} ───────── d(h) ∈ {8,9} ─────────── d(u′) ∈ {5,6}
                  transfers depend on subsumption and thinness
~~~

Both drawings show portions of the ambient graph. In the first drawing every vertex of $C$ joins both endpoints. No edges from $U$ to $w$, or $W$ to $v$, are present. Edges between the two exterior sets, inside each of the three sets, and from $C$ to the exterior sets are conditional. The second drawing does not assert that two receivers exist for every donor.

### A fixed increment

**Proposition.** Every finite simple graph of maximum average degree at most $64/9=7+1/9$ satisfies Tuza’s inequality. We prove the sufficient stronger claim that every subgraph-minimal violation $G$ has $2|E(G)|>(64/9)|V(G)|$. The deduction uses the local certificates in the cited preprints.

Let $L,H$ denote the vertices of degrees $5,6$ and at least eight, respectively. All remaining vertices of a minimal violation have degree seven. Puleo’s vertex and edge reductions imply robustness, non-WKE of each link component, and his Lemma 2.7. Write $h$ *subsumes* $x$ when $hx$ is an edge and $N[x]\subseteq N[h]$. Use Puleo’s transfers. A five takes $2/3$ from each subsumer. A six with link $K_{2,2,2}$ is *thin* and takes $1/6$ from each neighbor. Every other six takes $1/4$ from each subsumer. Write $\sigma(v)$ for final charge minus seven. Every $\sigma(v)\ge0$, and their sum is $2|E|-7|V|$. Each five has at least three subsumers, each nonthin six at least four. Every such subsumer lies in $H$. The set $L$ is independent. Thin sixes have no neighbors of degree seven. [Puleo, Lemmas 2.6–2.8](https://arxiv.org/pdf/1308.2211#page=5)

**First local check.** A thin six also has no neighbor of degree eight or nine. The neighbor’s link is connected by robustness, since two components would need at least ten vertices. Immediately after the proof of Lemma 3.4, Kandasamy introduces a fresh setup for Lemma 3.5. It takes $x$ with actual link $K_{2,2,2}$, a neighbor $u$ of degree eight or nine, and the private set $B=N(u)\setminus(N(x)\cup\{x\})$ of size three or four. The codegree cap of four in the preceding Lemma 3.4 and the additional contact bound in the subsequent Lemma 3.6 play no role in this proof. The seven-vertex core supports three initial packing/cover pairs of sizes $(4,6),(4,9),(5,9)$. The second selects every edge from $u$ to the common four-cycle and its packing can leave any prescribed one of those edges unused. The attached checker verifies these facts directly on the core, including all triangles at both endpoints and every packed outside edge. If $G[B]$ has a two-matching the first pair extends. Otherwise $G[B]$ is empty, a star with isolates, or a triangle with at most one isolate. The other pairs extend using just its private edges and its contacts to the four-cycle. Connectivity supplies any needed contact from an isolated private vertex or from the private triangle. The displayed covers in Lemma 3.5 and the local transfer Lemma 2.5 account for every triangle at $x,u$; no outer degree or additional reduction is required. [Kandasamy, §§2.1, 3.2](https://arxiv.org/html/2610.15269v1#S3.SS2)

**Second local check.** If $h$ subsumes two low vertices $x,y$, their open neighborhoods lie in $T=\{h\}\cup(N(h)\setminus L)$. When $|T|\le7$, Botler–Fernandes–Gutiérrez Lemma 3.3 forces both degrees to be five, both links to be cliques and $|N(x)\cap N(y)|=3$. If $h$ subsumes three such vertices then every pair of their neighborhoods has union seven. Thus $|T|=7$ and their three complementary pairs in $T$ are pairwise disjoint. Every pair of vertices of $T$ occurs together in one of the three neighborhoods, giving $G[T]=K_7$. The following is the full cell. Additional ambient edges may leave $T$, and every neighbor of each $z_i$ is already shown.

~~~text
                  complete core  T = {1,2,3,4,5,6,7}
                                     3 = h
        z₁=8                      z₂=9                     z₃=10
     joins 12345               joins 34567               joins 12367
       misses 67                 misses 12                 misses 45
~~~

These ten vertices span 36 edges. More strongly, the three $z_i$ reduce in the full ambient graph. Use the 21 core edges as cover and the eleven triangles from Figure 4 of the same paper. All triangles at a $z_i$ contain a core edge and every packed edge outside the three $z_i$ is a core edge. The recorded check verifies the published eleven triples on these labels. Hence an irreducible graph cannot contain the triple even when its maximum average degree is unrestricted. [Botler–Fernandes–Gutiérrez, Lemma 3.3 and the proof of Theorem 3.4, Figure 4](https://arxiv.org/pdf/2002.07925#page=8)

**Dominating the degree-sevens.** A seven-vertex $v$ having a low neighbor $x$ sees at least three vertices of $H$. Here $x$ is a five or a nonthin six. Each of its subsumers is distinct from $v$ and adjacent to $v$. A seven with no low neighbor must still see at least one vertex of $H$. Otherwise all seven neighbors have degree seven. The link of $v$ is connected, by robustness, and non-WKE. Gupta’s seven-vertex census supplies a neighbor $w$ on an edge of triangle codegree $c\in\{4,5,6\}$. Both endpoints have degree seven and both endpoint links are connected and non-WKE. For $c=6$ the certificate uses the common core and the two endpoints, and for $c=5$ the template and the excluded-link test use the one private neighbor at each end. For $c=4$, every common vertex is a neighbor of $v$ of degree seven. It has at most five local neighbors other than $v,w$, exactly Gupta’s additional condition (A2). Condition (A1) is the two endpoint link conditions already verified. The 1,144 certificates apply. Edges between private sets lie in no triangle at $v,w$, and Gupta’s Lemma 5.4 transfers each certificate to the ambient graph. The resulting pair reduction contradicts minimality. [Gupta, Lemmas 4.5, 5.4–5.5, Propositions 7.3, 8.5 and 9.1](https://arxiv.org/html/2608.06538v1#S9)

Every low vertex also sees at least three high vertices, through its three or more high subsumers or through all six neighbors of a thin six. We have thus established the required high-neighbor counts for lows, sevens adjacent to a low, and all other sevens.

### Quantitative check

Fix $h\in H$. Put $d=d(h)$, $\ell=|N(h)\cap L|$, and $t$ equal to the number of lows subsumed by $h$.

- If $d=8$, $h$ cannot subsume a five. If it subsumed two sixes, then $1+d-\ell\le7$ and the second local check would force them to be fives. Thus $t\le1$. There are no thin payments, so $\sigma(h)\ge3/4$, with $\sigma(h)=1$ when $t=0$.
- If $d=9$, $t\le3$ by Puleo 2.7(f). If $t=3$, $\ell\ge3$ gives $1+d-\ell\le7$, forbidden by the second local check. Therefore $t\le2$. There are no thin payments and $\sigma(h)\ge 2-2t/3$.
- If $d\ge10$, then $\sigma(h)\ge(d-7)/3$. When $t=0$, the payment is at most $d/6$. If $t>0$, Puleo 2.7(g) gives $\ell\le d-6$. When $\ell\le d-7$, the payment is at most $2(d-7)/3$. For $\ell=d-6$ the common set $T$ has seven vertices, so $t\le2$ by the second local check. The payment is then at most $4/3+(d-8)/6=d/6$. In both cases using the $d/6$ bound, $d-7-d/6\ge(d-7)/3$ because $3d\ge28$.

For each $h\in H$, count $m(h)$ as one for $h$, plus one per neighboring seven with no low neighbor, plus $1/3$ per neighboring low or seven with a low neighbor. Every vertex receives total weight at least one across the high vertices, by the preceding domination argument. Consequently $|V|\le\sum_{h\in H}m(h)$.

We verify $m(h)\le9\sigma(h)$. Start at the convenient upper bound $d+1$ for $m(h)$. Every high neighbor saves one unit and every low or seven with a low neighbor saves $2/3$ units. Whenever $h$ subsumes a low $x$, there are at least four other vertices in $N(x)$, all adjacent to $h$. At least two of these are fellow high subsumers. Every other one is high or a seven next to $x$. Those four distinct vertices therefore save at least $2+2(2/3)=10/3$, apart from any savings at the low vertices themselves.

| Degree and payments at $h$ | Upper bound on $m(h)$ | Comparison with $9\sigma(h)$ |
|---|---:|---|
| $8,\ t=0$ | $9$ | $9\sigma=9$ |
| $8,\ t=1$ | $9-10/3-2/3=5$ | $9\sigma\ge27/4$ |
| $9,\ t\le1$ | $10$ | $9\sigma\ge12$ |
| $9,\ t=2$ | $10-10/3-4/3=16/3$ | $9\sigma\ge6$ |
| $10,\ t=0$ | $11$ | $\sigma\ge3-10/6=4/3$ |
| $10,\ t>0$ | $11-10/3-2/3=7$ | $\sigma\ge1$ |
| $d\ge11$ | $d+1$ | $d+1\le3(d-7)\le9\sigma$ |

The last comparison is strict for $d>11$. For $d=11$, equality would require $m=12$. Then every neighbor would be a seven without low neighbors, so $\sigma=4$, also strict. Kandasamy’s degree-ten theorem gives at least one vertex of degree at least eleven in a minimal violation. Thus

$$
|V| \ \le\ \sum_{h\in H}m(h)\ <\ 9\sum_{h\in H}\sigma(h)
\ \le\ 9(2|E|-7|V|).
$$

The hereditary property of maximum average degree transfers the asserted bound to every finite input graph. Endpoint inclusion follows from the displayed strict inequality. The degree-nine estimate already excludes equality in that row. The degree-eight row without recipients allows equality in the incidence estimate alone, so this computation does not optimize the density constant. [Kandasamy, Theorem 1.1](https://arxiv.org/abs/2610.15269)

### Finite controls and scope

On $K_6$ minus one edge, the recorded exact check gave packing number four. A root of degree five whose link is $K_5-e$ realizes the neutral five-link pattern. The other vertices of the finite cell include degree fours. On the Figure 4 cell there are 65 actual triangles, with exact packing number eleven from the recorded check as well as the direct eleven-witness. The single-edge neutrality test fails in both cells. Figure 4 has no WKE link component, nevertheless its three-vertex reduction applies. Its component-shape test reached the 32-packing cap and is inconclusive; its cheap cut was witnessed. Both examples contain a $K_4$, outside the domain of the $K_4$-free test. The unrestricted proof above uses the shown reductions and discharge. This deduction uses the cited finite certificates. The later donor counts strengthen this intermediate density bound.
