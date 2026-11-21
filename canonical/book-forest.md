# Packing and covering along the books

<a id="forest"></a>

## Every counterexample has a high triangle with two repeated sides

~~~text
     path type at two sevens               one-edge type at two sevens

       N(y)∩N(z) = a — h — b                N(y)∩N(z) = s — t     v
      private base uv on the y side         common high base st at both roots
      private base st on the z side         the other two bases are uv and Uv

         Degree-two node in the auxiliary graph of high book bases
                 D ─── y ─── B ─── z ─── E
                      root            root
       y packs D and two B sides; z packs E and two other B sides.
~~~

**Proposition.** Let $H$ be induced by the vertices of degree at least eight in a finite simple graph. If every triangle of $H$ contains at most one edge belonging to at least two triangles of $H$, the whole graph satisfies $\tau_\triangle\le2\nu_\triangle$. Equivalently every counterexample contains a high $K_4$ or the high fan $K_1\vee P_4$ as a subgraph. Additional edges among the five fan vertices are allowed.

#### Complete endpoint hypotheses and the first pair

The hypothesis passes to subgraphs because high vertices and all the witnesses for a repeated high edge can only disappear. Work in a subgraph-minimal violation. The previously checked census excludes degrees below seven and leaves two possible full links at every seven. Write $a,b,c$ for the three tips and $u,v,s,t$ for the four ends. The link contains all tip–end edges, with only $cu$ optionally missing, and just the two further edges $uv,st$. In the complete case all positions are high. In the deficient case only $c,u$ may be nonhigh, independently, and then they are sevens. A nonhigh in position $u$ has common-tip graph $a-v-b$ with the root. One in position $c$ has common-tip graph consisting of the edge $st$ and isolated vertex $v$. These are *full ambient common-neighbor graphs*. The earlier reduction of a seven–seven edge with four common tips and the low-vertex exclusions are part of this input. [Prior independent scope and marking audit](fan-structure.md#marked)

The path type gives a uniform two-root reduction. Label the two seven roots $y,z$, their common-tip path $a-h-b$, the private high bases $uv$ at $y$ and $st$ at $z$, and the remaining private tips $c,d$. Each of $a,b,c$ sees $u,v,h$, and each of $a,b,d$ sees $s,t,h$. The path center is uniquely identified; its two leaves are interchangeable. The private triples $\{u,v,c\},\{s,t,d\}$ are disjoint because the whole common neighborhood has size three. Either of $c,d$ may itself be a seven. Pack
$$
 dtz,\quad chy,\quad byz,\quad uvy,\quad asz
$$
and buy
$$
 as,ay,by,ch,cy,dt,hz,sz,tz,uv.
$$
All five packed triangles use distinct edges; the four packed edges avoiding both roots are $dt,ch,uv,as$, all bought. The ten purchases hit the 23 root triangles. The optional nine edges between private triples belong to no root triangle, and an exterior vertex cannot be a further root neighbor. This rules out every path-type edge. [Path-pair verification](../verification/check_path_pair.py)

In the one-edge case at $yz$, the unique edge $st$ of the common-tip graph fixes a shared **whole** high base. Only the order of $s,t$ may reverse. Its isolated vertex $v$ is one end of the other local base at each root. These bases are $uv,Uv$, with $u,U$ distinct because neither belongs to the common triple. Each root now has exactly two distinct high bases, including at one-edge components. Indeed any seven with two nonhigh neighbors would have a path-type edge, which just reduced. Thus the graph on sevens consists of isolated vertices and isolated one-edge pairs. No independent reduction of this latter type is required for the counting proof below.

#### Represented books and cover purchases

In a high book on a repeated edge, each high side other than the base belongs to exactly one high triangle. A second high triangle on that side would give two repeated sides on its existing page. Sides belonging to books with different bases are distinct, and no such side can be a repeated base. At every seven, $a,b$ and **both ends of each base** are high, so the four edges from $a,b$ to those ends are genuine sides of high pages.

Make an auxiliary multigraph whose vertices are the high book bases represented at least once, and whose edges are *all* sevens, joining their two local bases. Parallel edges are retained and there are no loops. At a root $y$, buying its two book bases and its three spokes to $a,b,c$ covers every triangle through $y$, including when $c$ is another seven. Every high–high rim edge at $y$ is a represented base or a side of a genuine high page on one of the two bases, with at most one exception. The exception is the edge $cv$ of an incomplete all-high rim. If $c$ is the remaining possible seven, $cv$ is not high–high. A nonhigh root outside the users of a book $B$ can therefore see a true side of $B$ only as this unique exceptional edge. One isolated incomplete root can account for at most one such side across all books combined.

An auxiliary cycle of $k$ edges reduces, including a parallel-edge cycle of length two. Orient the cycle. At each root pack one triangle on its tail base and two using a two-edge matching of high sides on its head base, taking its two distinct full high tips. Rooted edges are disjoint because the two bases at a root have disjoint ends, the tips are separate, and every packed spoke goes to a high vertex. Off-root edges are distinct because each base is used once in each role and because sides of different books are disjoint. Buy the $k$ cycle bases, the $2k$ packed sides, and the three tip spokes at each root, total at most $6k$ edges for $3k$ triangles. This covers all root triangles and buys every packed edge surviving root deletion. These claims still hold for adjacent roots. Hence the multigraph is a forest.

#### Leaves and degree-two books

For a book $B$ of auxiliary degree one, let $y$ be its unique user. Prescribe *any* side $p$ of a full high page at $y$, choose that page as a packed triangle, and pack $y$ on its other base $D$. Match the two remaining tips of $y$ to the two ends of $B$ to give two further root triangles. At most one edge of that $K_{2,2}$ is missing, so a perfect matching exists. A nonhigh third tip is allowed in either rooted triangle. There are four edge-disjoint triangles, using $B,D$ and four distinct cross-edges at $B$. Buy both bases, all three tip spokes at $y$ and the other three used cross-edges. Delete $y$, the purchases and the omitted side $p$. The only high triangle on $p$ uses the purchased base $B$. If no other seven sees $p$, every triangle lost in that deletion is covered and the residual packing extends. The eight purchases therefore suffice. Each of at least four distinct genuine high sides at a degree-one book must consequently be seen by a seven outside its user.

For a book $B$ of auxiliary degree two, let its users be $y,z$. Their other bases $D,E$ are distinct by acyclicity; they may share an endpoint. Start with any prescribed side $p$ of a full high page used by $y$, and choose a two-edge matching of the sides of $B$ at $y$ containing $p$, using two distinct full high tips. Choose *any* two full high tips of $B$ at $z$. The first matching deletes at most a matching from the resulting $K_{2,2}$ at $z$, leaving a perfect matching. In particular the two roots need not see any of the same tips. Use the two matchings for four root triangles and pack $y$ on $D$, $z$ on $E$. Off-root edges are distinct by the high book properties. Buy $B,D,E$, the three tip spokes at each root, and three of the four used high sides, omitting $p$; this costs at most twelve for six triangles. Delete both roots and every used side together with the purchases. If no seven outside $\{y,z\}$ sees $p$, every triangle on the unbought deleted side is covered as above. All other deleted triangles contain a purchase or are covered at a root. Thus every degree-two book requires at least four distinct high sides seen by sevens outside its two users. This proof includes the case when $y,z$ are neighbors. The only flank allowed to remain unbought in either construction is a genuine side of a high page, not the exceptional edge $cv$.

#### Counting and final implication

Let $n_1,n_2,n_{3+}$ count auxiliary vertices of the indicated degrees, let $m$ be the number of edges (all sevens), and let $k$ be the number of nonempty tree components. Different books require different sides. Each witness outside a book's one or two users can witness just one of those high sides because it must be using its exceptional edge. Therefore $4(n_1+n_2)\le m$. On the other hand the degree sum in a forest gives $n_{3+}\le n_1-2k$, hence
$$
 m=n_1+n_2+n_{3+}-k\le2n_1+n_2-3k<4(n_1+n_2)
$$
whenever $m>0$. This eliminates all sevens. Unrepresented high books were deliberately excluded from the auxiliary vertex set: they supply no edges there and require no witness count.

Every remaining vertex is high. Distinct books have disjoint triangle edge sets, since two pages sharing an edge both belong to the unique book on their repeated side. The other triangles use edges belonging to no other triangle. Selecting one page per book and every isolated triangle packs as many triangles as the number of edges needed by selecting each base and one edge per isolated triangle. Therefore $\tau_\triangle=\nu_\triangle$, finishing the hereditary class proof.

Finally let a high triangle $abc$ have repeated sides $ab,ac$ with additional high tips $w,z$, respectively. If $w=z$ the four vertices induce $K_4$. If $w\ne z$, the path $w-b-c-z$ with universal vertex $a$ gives the claimed fan subgraph. Conversely the middle triangle of that fan has both spokes repeated, and any face of a high $K_4$ has all three sides repeated. This is an ordinary subgraph occurrence. It makes no assertion about absent chords on the five fan vertices or the general case where the occurrence is present.

The independent replay checks all 512 private-edge completions of the path pair, all 22 choices of a full high side across the two rims for a degree-one book, and 750 matching choices for degree-two books. A connected 41-vertex example realizes adjacent one-edge-type roots whose two other bases have a common end. Six packed triangles and eleven purchases suffice for the tested release in this graph. [Path-pair verification](../verification/check_path_pair.py)

The argument uses the minimal-counterexample reductions above.

<a id="tetra"></a>

## A high fan or a five-clique with four high vertices

~~~text
       Along a represented base                 Along a tetrahedron edge
                 a        b                                x────z
                  \      /                                /|    |\
                   u────v                                u───────v
                 root y sees all four                    y cannot see u,v,x,z

   a and b each see u and v.                  In a high tetrahedron uvxz, any high
   Its two high pages are auv,buv.            tip other than x,z makes a high fan.

       From one seven's rim, the possibly exceptional edge is cv:

             tips    a   b   c          All tip–end edges exist except possibly cu.
             bases   u───v   s───t      The ends have only their two base edges.
                    root y sees all seven.
~~~

**Proposition.** Let $H=G[\{v:d_G(v)\ge8\}]$ for a finite simple graph $G$. If $H$ has no $K_1\vee P_4$ as an ordinary subgraph and $G$ has no five-clique with at least four vertices in $H$, then $\tau_\triangle(G)\le2\nu_\triangle(G)$. The number of high tetrahedra is unrestricted. Here “a seven” denotes a vertex of degree exactly seven in the graph being considered.

**Heredity and the low vertices.** Both forbidden configurations survive on passing to supergraphs, since degrees can only increase. We may therefore take a subgraph-minimal violation to which the unrestricted local minimality reductions apply. In particular the minimum degree is at least five, and vertices of degree five or six form an independent set. A thin six has six high neighbors inducing an octahedron. The four neighbors of any vertex of the octahedron induce a cycle and contain a path on four vertices, giving a high fan. A nonthin six has at least four high subsumers, all universal in its link; these give a five-clique with the six. Thus there is no six. A five $x$ has at least three high subsumers. They are pairwise adjacent and adjacent to every other neighbor of $x$. Any fourth high neighbor would yield a five-clique on four highs and $x$. Its other two neighbors are therefore sevens. A seven cannot subsume $x$, so its codegree with $x$ is at most three. [Puleo, Lemmas 2.6–2.7 and the low-degree cases in the proof of Lemma 2.8](https://arxiv.org/pdf/1308.2211v3#page=5)

**Wide seven pairs.** A wide edge has at least four common neighbors. The previously verified pair reductions for adjacent sevens exclude five and six common neighbors and leave three signatures at four. In every such signature the four tips are high and all four private vertices see every tip. A clique on the four tips is forbidden because either seven then completes a five-clique with four highs. In the square signature, a private high would be the center of a fan over three consecutive square edges. A private five would have four high neighbors. All four private vertices must consequently be sevens. At either endpoint its three seven-neighbors are its partner and its two private neighbors. Each sees the full high square, so each such joining edge is itself wide. Reapplying the same allowed signature at each joining edge proves that the whole connected seven component is cubic and joined to this **same** high square, exhausting each of its vertices' degree seven. No triangle can occur among the sevens there, since its endpoints would have a fifth common neighbor. Hence $m$, the component's number of edges, is at least nine. Its five-color greedy edge coloring gives four color classes of combined size at least $4m/5$. Assign these four matchings to distinct square corners to pack one triangle per selected edge. The $m$ component edges and four square edges hit all triangles at the removed vertices, with $m+4\le 8m/5$. This is an ambient reduction. Thus every wide neighbor of any remaining seven is high. The application requires only one wide seven pair to start the component. [Five- and six-tip reduction](paired-sevens.md#gupta) · [Four-tip domains and exceptional signatures](paired-sevens.md#pair)

**Local census.** At a seven $y$, the high-induced graph on $N(y)$ is fan-free as a subgraph of $H$. It contains no tetrahedron, since $y$ would complete a five-clique. A triangle with two locally repeated sides produces either a local tetrahedron or a local fan, according as the supplementary tips coincide or differ. Thus the actual marked rim satisfies precisely the local predicate used by the five-row census. Replaying the checked domain gave 1,044 unlabeled seven-rims covering $2^{21}$ labeled graphs, 853 connected rims and 117 connected non-WKE rims. Forty positive cone certificates leave 77. Of their 9,856 markings, 159 keep every wide spoke high and five pass the local high-triangle test. Crucially, the test counts triangles **inside the marked rim**. External high faces elsewhere on tetrahedra cannot invalidate the inference. [Exact marking predicate and five rows](fan-structure.md#marked)

Writing the rim as drawn above, $cu$ is either present, with all seven neighbors high, or absent, with only $c,u$ potentially nonhigh. At $c$, the three common vertices with $y$ induce a single edge and an isolated vertex. At $u$, they induce a three-vertex path. In neither case is their induced graph a triangle. A five in either position would have its three pairwise adjacent high subsumers in that common neighborhood. Every five has a seven-neighbor, so this excludes all fives. Both nonhigh positions are now sevens. The path type admits the five-triangle, ten-edge pair reduction using only the two full endpoint links. the check reconstructed all 512 optional private-edge choices and all 23 rooted triangles in each. Hence $u$ is always high, and at every remaining seven both bases and the two full tips $a,b$ are high. [Ambient pair witness and independent replay](book-forest.md#forest)

**The represented bases.** Call a base represented if some seven $y$ uses it as $uv$ or $st$. Such a base $B=uv$ has two distinct high tips $a,b$ adjacent to $y$. In any high tetrahedron $uvxz$, an exterior high vertex $w$ adjacent to $u,v$ would give a high fan centered at $u$ over $w,v,x,z$. Thus if $B$ were a tetrahedron edge, $a,b$ would have to be $x,z$; the seven would see the whole tetrahedron. This is forbidden. In particular a represented base lies in no high tetrahedron, even if many tetrahedra occur elsewhere.

Let $uvt$ be **any** high page on a represented base $uv$. It has a second high page on $uv$. If a proper side, say $ut$, were repeated, then $uvt$ would have two repeated high sides. Equal supplementary tips would put $uv$ in a high tetrahedron; different supplementary tips would give a high fan. Both are impossible. Consequently each proper side of a represented book has one high triangle in the entire graph. It cannot be another repeated base or a proper side of a distinct represented book.

**Forest transfer.** Every seven represents exactly one edge, joining its two distinct bases in the previous auxiliary multigraph. At its full rim every high edge is one of its two bases or their true page sides, with the sole possible exception $cv$ where $cu$ is missing and $c$ is high. In the present class this exceptional edge can belong to an unrelated tetrahedron. This causes no new lost page because only a genuine page side of a represented book is ever released unpaid. Such a side has just been proved globally unique on the high side. An outside seven seeing it must use its unique exceptional occurrence or be another user of that same book.

The cycle reduction packs three triangles per root and buys at most six edges per root. For a represented base of auxiliary degree one or two, treating all its users together forces a separate outside witness for each of four true sides. The packing and cover for these short paths use the full rim, the two distinct full tips, and the global uniqueness just established. They cover every triangle lost, including at adjacent sevens. The path and cycle proof needs no assertion about high edges elsewhere. In particular a dangling occurrence on a tetrahedron can only reduce the supply of eligible witnesses for represented sides. With $n_1,n_2,n_{\ge3}$ the counts of represented bases of the three degree types, $m$ the number of sevens, and $k$ the number of nonempty forest components, every remaining seven supplies at most one witness. Thus $4(n_1+n_2)\le m\le 2n_1+n_2-3k$, impossible for a nonempty forest. The finite checks for the separate path constructions replayed all 22 degree-one full-side choices and 750 degree-two matching comparisons. [Detailed ambient purchases and forest proof](book-forest.md#forest)

**Terminal graph and the four-side target.** All vertices are high. Each high tetrahedron is an entire component for adjacency of triangles by shared edges, since an exterior high tip on a tetrahedron edge gives a fan. Every triangle outside those tetrahedra has at most one repeated side, so its component is a book or a singleton. In a tetrahedron buy two opposite edges and pack one face. In every book or singleton buy one edge and pack one triangle. Distinct components share no edge, so these choices prove the claimed inequality. For a graph in the target with one high tetrahedron, any five-clique with four highs would use its four vertices and give each of its sides the same exterior tip. Even one clean side rules it out. The four- and five-occupied-side cases are therefore excluded, as is any six-occupied-side case where there is no common exterior tip to all six. For multiple tetrahedra the corresponding exclusion requires the hypothesis at **every** one.

This proof makes no assertion that a single ambient codegree-two edge with adjacent tips is reducible in unrestricted graphs.
