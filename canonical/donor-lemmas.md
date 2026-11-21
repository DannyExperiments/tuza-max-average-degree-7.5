# Earlier structural and charge estimates

<a id="fractional"></a>

## Independent check of the fractional endpoint

~~~text
        degree eight h                       degree nine g with two paid fives
           a     b                                      g
            \   /                               /       |        \
              h                             x₁,x₂    six highs    last neighbor
       / / / / |  \                          1/5 each                ≤ 1/4
     y₀ y₁ y₂ y₃ y₄ y₅
     at least one sends ≤ 1/5
     each other sends ≤ 1/4
~~~

The lines show incidence shares arriving at the high vertex. A high receives weight one for itself. The degree-eight panel depicts its two-high-neighbor case. The degree-nine panel reserves the last neighbor even when it contributes zero weight.

**Proposition.** Every finite simple graph with $\operatorname{mad}(G)\le733/99$ satisfies $\tau_\triangle(G)\le2\nu_\triangle(G)$. The largest donor ratio allowed by the checked rows is $99/40$, at degree nine. Every row of degree at least eleven is strictly below it. The change from $37/5$ is $2/495$.

Write $H=\{h:d(h)\ge8\}$, $r(y)=|N(y)\cap H|$, $j=|N(h)\cap H|$, and let $f$ count the fives subsumed by $h$. For a subgraph-minimal violation let $s(v)$ be the final charge above seven under Puleo's rules, and $w(h)=1+\sum_{y\in N(h)\setminus H}1/r(y)$. Every nonhigh vertex with $r=3$ is a five subsumed by all three high neighbors. All others have $r\ge4$. Thus $w\le1+(d-j)/4+f/12$, and the coarser $w\le1+(d-j)/3$ also holds. [Normalized count and preceding charge rows](donor-lemmas.md#fractional) · [Seven-vertex and low-neighbor transfer](seven-links.md#three-high)

At degree eight $s=1$, $j\ge2$, and all nonhigh neighbors have $r\ge4$. For $j=2$ the audited group reduction forces one of the six to have $r\ge5$, giving $w\le1+5/4+1/5=49/20$. For $j\ge3$, $w\le1+5/4=9/4$. Hence the degree-eight ratio is at most $49/20=98/40$. [Degree-eight charge](seven-links.md#eight-spokes) · [Two-high-neighbor minimum](seven-links.md#two-high) · [Group reduction and equality exclusion](seven-links.md#quartet)

| Degree and condition | Upper bound on $w$ | Lower bound on $s$ | Upper bound on $w/s$ |
| --- | ---: | ---: | ---: |
| Nine, no payment | $13/4$ | $2$ | $13/8$ |
| Nine, one five | $17/6$ | $4/3$ | $17/8$ |
| Nine, one six | $5/2$ | $7/4$ | $10/7$ |
| Nine, two sixes | $5/2$ | $3/2$ | $5/3$ |
| Nine, one five and one six | $31/12$ | $13/12$ | $31/13$ |
| Nine, two fives | $33/20$ | $2/3$ | $99/40$ |
| Ten, no subsumed low and no thin neighbor | $13/3$ | $3$ | $13/9$ |
| Ten, no subsumed low and some thin neighbor | $3$ | $2$ | $3/2$ |
| Ten, some subsumed low and $j\le2$ | $11/3$ | $7/3$ | $11/7$ |
| Ten, some subsumed low, $j\ge3$, $f\le2$ | $35/12$ | $4/3$ | $35/16$ |
| Ten, three subsumed fives | $7/3$ | $1$ | $7/3$ |
| Eleven, $j\le2$ | $14/3$ | $10/3$ | $7/5$ |
| Eleven, $j=3$ | $11/3$ | $7/4$ | $44/21$ |
| Eleven, $j\ge4$ | $19/6$ | $4/3$ | $19/8$ |
| Twelve, $j\le2$ | $5$ | $13/3$ | $15/13$ |
| Twelve, $j\ge3$ | $4$ | $5/3$ | $12/5$ |
| $d\ge13,\ j\le1$ | $(d+4)/4$ | $(d-7)/3$ | $3(d+4)/(4(d-7))\le17/8$ |
| $d\ge13,\ j\ge2$ | $(d+1)/3$ | $(d-7)/3$ | $(d+1)/(d-7)\le7/3$ |

At nine there is no thin-six payment, and at most two lows can be subsumed. A paid five entails $j\ge2$, a paid six entails $j\ge3$, and their costs are $2/3$ and $1/4$. With two paid fives the verified union-eight reduction and BFG's small-union lemma force their open neighborhoods to have union seven and both links to be cliques. Consequently each five has exactly five high neighbors, and the donor has at least six high peers. At most one neighbor beyond these eight can contribute. A $1/3$ contribution would require a third subsumed five. This gives $w\le1+2/5+1/4=33/20$, exactly the numerator used in the possible equality row. [Degree-nine proof](donor-lemmas.md#nine-budget)

For $d\ge10$, the charge estimate $s\ge(d-7)/3$ uses the three-low reduction on a common seven-set. Indeed, if a low is subsumed then the number $\ell$ of adjacent lows is at most $d-6$. For $\ell\le d-7$ the donor loses at most $2(d-7)/3$. If $\ell=d-6$, at most two lows are subsumed and the loss is at most $4/3+(d-8)/6=d/6$. With no subsumed low the same $d/6$ bound applies. When $j\le2$, a thin neighbor or subsumed six would force at least four or three high peers, respectively. Two paid fives would share the donor and its only two possible fellow subsumers, forcing union at most seven and clique links, which would give four high peers. Thus loss is at most $2/3$ on those rows. [Ambient three-low reduction and charge estimates](low-vertex-reductions.md#local)

At ten, a thin neighbor forces $j\ge4$, leaving at most six thin payments. A donor subsuming some low has $\ell\le4$. At $\ell=4$ the seven-set argument caps the loss at $5/3$. At $\ell\le3$ with $f\le2$, the loss is at most $4/3+1/4$. In either case $s\ge4/3$. Three subsumed fives have open neighborhoods in the same eight-set. Their complementary triples cannot be pairwise disjoint, so two neighborhoods have union at most seven and are cliques, supplying six high peers. Thus the $f=3$ row has $j\ge6$. [Degree-ten proof](donor-lemmas.md#high-donors)

At eleven with $j=3$ no thin six is adjacent. Each subsumed five supplies two fellow subsumers among the three peers, and two fives supplying the same pair would force clique links and four peers. Thus $f\le3$. With at most four adjacent lows the loss is at most $3(2/3)+1/4=9/4$. With five lows the seven-set argument allows at most two subsumed lows, and any donating eleven with a subsumed low has $\ell\le5$. This proves $s\ge7/4$. At $j\ge4$, $f\le5$ yields $w\le1+7/4+5/12=19/6$. The last two ratios in the table decrease in $d$ and attain their upper bounds at $d=13$. The largest displayed upper bound over degrees at least eleven is $12/5=96/40$.

Each high counts itself and every nonhigh distributes exactly one across its high neighbors. All surpluses are nonnegative, with $\sum_v s(v)=2|E|-7|V|$. Kandasamy's Theorem 1.1 gives a donor of degree at least eleven in every violation, and its comparison is strict. Thus
$$
 |V|=\sum_{h\in H}w(h)<\frac{99}{40}\sum_{h\in H}s(h)
 \le\frac{99}{40}(2|E|-7|V|).
$$
Every subgraph-minimal violation has average degree strictly greater than $7+40/99=733/99$. A graph with maximum average degree at most $733/99$ passes that same bound to every subgraph, proving the inclusive endpoint. Strictness uses Kandasamy's maximum-degree-ten theorem at preprint level. [Kandasamy, Theorem 1.1](https://arxiv.org/html/2610.15269v1#S1)

<a id="rebate"></a>

## Returning the surplus of a five with a clique link

~~~text
                   h₁  h₂  h₃  h₄  h₅        complete five-neighbor link
                    \   \   |   /   /
                              x             degree 5

                each hᵢ pays x   2/3
                x returns to hᵢ  4/15
~~~

The five return arrows have distinct recipients at a given vertex $x$. A high vertex may receive arrows from several fives.

**Proposition.** Every finite simple graph $G$ with $\operatorname{mad}(G)\le363/49$ satisfies $\tau_\triangle(G)\le2\nu_\triangle(G)$. The following proof uses the preceding $733/99$ donor table. It is independent of the current five-hub enumeration. The numerical gain over the previous endpoint is $20/4851$. [Inherited donor inequalities](donor-lemmas.md#fractional)

Work in a subgraph-minimal violation. Let $s(v)$ be final charge above seven under Puleo’s rules. Every $s(v)\ge0$, and $\sum_vs(v)=2|E|-7|V|$. An edge from a subsumer to a five carries $2/3$. Let $L$ be the set of degree-five vertices whose actual link is $K_5$. For $x\in L$ all five neighbors subsume it and are of degree at least nine. Since $x$ does not pay any lower neighbor, its surplus is exactly
$$
                s(x)=5-7+5(2/3)=4/3.
$$
Denote the adjusted surplus by $s'$. Each $x\in L$ returns $4/15$ to each of its five neighbors. This exhausts its $4/3$ and leaves $s'(x)=0$. Every other nonhigh retains its original surplus. A high $h$ has $s'(h)=s(h)+(4/15)|N(h)\cap L|$. Each ordered incidence transfers once in both directions of the accounting, so overlaps between five-neighborhoods preserve both nonnegativity and the total. Equivalently, on these particular incidences the net payment from a high to a five becomes $2/5$. [Puleo, Lemmas 2.7 and 2.8](https://arxiv.org/pdf/1308.2211v3#page=6)

Let $H=\{h:d(h)\ge8\}$, $r(y)=|N(y)\cap H|$, and $w(h)=1+\sum_{y\in N(h)\setminus H}1/r(y)$. Then $\sum_{h\in H}w(h)=|V|$. A nine paying two fives $x,y$ has $s(h)\ge2/3$. The checked union-seven lemma gives $x,y\in L$ and the inherited weight bound is $w(h)\le33/20$. It follows that
$$
                s'(h)\ge 2/3+8/15=6/5,\qquad
                \frac{w(h)}{s'(h)}\le 11/8.
$$
One receiver’s surplus can be used by each of its five subsumers at the stated $4/15$ share. Two distinct receivers therefore give two shares at their common donor even if some of the other four subsumers coincide. [Degree-nine union proof](donor-lemmas.md#nine-budget)

For every other high donor $s'\ge s$. The maximum of the previous degree-eight row is $49/20$. For nines other than the line just corrected, the largest prior ratio is $31/13$. At degree ten it is $7/3$, and at degrees at least eleven it is $12/5$. Each of the latter three bounds is strictly below $49/20$. Kandasamy’s maximum-degree-ten theorem supplies a vertex of degree at least eleven in a violation. Consequently
$$
 |V|=\sum_{h\in H}w(h)
 <\frac{49}{20}\sum_{h\in H}s'(h)
 \le \frac{49}{20}\bigl(2|E|-7|V|\bigr).
$$
Thus every subgraph-minimal violation has average degree strictly greater than $7+20/49=363/49$. A subgraph of a graph with maximum average degree at most $363/49$ inherits the bound, proving the inclusive statement. [Fraction-by-fraction table](donor-lemmas.md#fractional) · [Kandasamy, Theorem 1.1](https://arxiv.org/html/2610.15269v1#S1)

Puleo’s unrestricted threshold is $\operatorname{mad}<7$. Tsujimura’s $25/2$ theorem requires additional triangle-overlap hypotheses, while Kandasamy’s global degree-ten theorem has a maximum-degree hypothesis. The $363/49$ deduction here applies with arbitrary edge codegrees. [Puleo](https://doi.org/10.1016/j.ejc.2015.03.006) · [Tsujimura, Theorem 1.1](https://arxiv.org/html/2611.11128v2#Sx1) · [Kandasamy, Theorem 1.1](https://arxiv.org/abs/2610.15269)

**Alternative endpoint check.** The earlier occurrence theorem also forces strictness. Equality would require all highs to be eights and all their rows to attain $49/20$. Then five-vertices are impossible because their subsumers have degree at least nine. Nonthin sixes would need subsumers even though eights cannot subsume them, and thin sixes cannot neighbor any eight or seven. All nonhighs are therefore sevens. Each high has exactly two high peers and, by equality in its weight estimate, five seven-neighbors with $r=4$ and one with $r=5$. If there are $a>0$ eights, the counts of the two types of sevens are $5a/4$ and $a/5$. Hence exactly $4/29$ of the sevens have $r\ge5$, contradicting the previously proved lower bound $3/13$. This version dispenses with the global maximum-degree-ten theorem for strictness, while retaining the local thin-six and occurrence inputs.  · [Degree-eight and low-vertex facts](donor-lemmas.md#fractional)

<a id="eight-atlas"></a>

## The 203 retained eight-vertex links

The fixed eight-vertex catalogue has 12,346 representatives and the catalogue verification accounts for all $2^{28}$ labeled simple graphs by disjoint isomorphism orbits. Every omitted type received a positive reason in the following disjoint count. [Eight-vertex catalogue](../verification/data/graph8.g6) · [Catalogue verification](../verification/data/catalog-verification.json)

| Reason | Number of types |
| --- | ---: |
| A spoke has zero or one incident triangle | 4,887 |
| A connected component of order at most four has a checked WKE witness | 17 |
| The whole link has a checked WKE witness | 7,036 |
| A supplied partial-star witness passes literal checking | 203 |
| Retained for the second endpoint | 203 |

A spoke in no triangle can be deleted. If $xy$ has sole triangle $xyz$, delete its three edges, append this triangle to the residual packing, and buy $xz,yz$. For the WKE rows the checker searched ordinary rim matchings $M$ and label sets $Q$ with $|Q|=|M|$ meeting every edge of the relevant rim outside $M$. Applying a witness from a component to the complete rooted cone was checked explicitly.

For a general partial-star witness, use a rooted triangle on each edge of $M$ and the specified rim triangles $D$. Buy every packed rim edge and the spokes to $Q$. Delete the bought edges together with all packed spokes. All packed edges are then unavailable to a residual packing. The recorded check verified that the purchase count is at most $2(|M|+|D|)$ and that every actual triangle using a packed spoke meets a purchase. Triangles using only untouched spokes may remain in the residual graph. This distinction matters for the 203 partial-star certificates. The proof uses only positive exclusions and works even if a retained type has another reduction.

The public domain check verifies all five rows in the classification above. [Eight-link domain verification](../verification/check_eight_domain.py)

<a id="eight"></a>

## Five neighbors of degree at most seven around an eight

~~~text
           z₁   z₂   z₃   z₄   z₅          five marked vertices, degrees ≤7
             ╲   ╲   │   ╱   ╱
                       h                   degree 8
                   ╱   │   ╲
                  a    b    c              unmarked, degrees unrestricted

           selected zᵢ ─── t               t outside the nine-vertex cone
                    buy zᵢt
~~~

Every line from $h$ is mandatory. Edges among its eight neighbors are read from the full link. The indicated exterior edge illustrates one of the exits bought for a selected mark.

**Proposition.** In every finite simple subgraph-minimal violation of Tuza's inequality, each degree-eight vertex has at least four neighbors of degree at least eight. No global minimum-degree assumption is used.

Let $L=G[N(h)]$, $K=G[N[h]]$, and suppose that five rim vertices $T$ have degrees at most seven. Choose $S\subseteq T$, delete $U=\{h\}\cup S$, and write $R=N(h)\setminus S$. Buy the edges inside each side $U,R$, and every edge from $S$ to outside $K$. Every triangle inside $K$ has a same-side edge. An exterior triangle meeting $U$ has a purchased exit because $h$ has no exterior neighbors. Any packed triangle of $K$ has every edge disjoint from $U$ in $G[R]$, where it is purchased. Hence an edge-disjoint packing $P$ in $K$ pays for this deletion whenever its purchase count is at most $2|P|$. Both residual packing and residual cover then lift.

The exact cost is
$$
  \sum_{z\in S}\bigl(d_G(z)-1-d_L(z)\bigr)
    + |S|+e_L(S)+e_L(R)
  = \sum_{z\in S} d_G(z)+2e_L(R)-e(L).
$$
In particular $7|S|+2e_L(R)-e(L)$ is an upper bound. If any mark has $d_L(z)=7$, its eight distinct neighbors in $K$ already contradict $d_G(z)\le7$. This feasibility check removes such rows before using any exterior budget. For every feasible mark, $6-d_L(z)$ is its nonnegative exit count when its ambient degree is exactly seven.

The preceding witness catalogue gives a positive reduction for every eight-link outside the 203 retained types. On each retained type the recorded check formed all 56 sets of five marks, priced all 32 subchoices using the actual internal edges, and verified the formula above. the check verified the packing and its optimum independently on each cone. A size certificate alone suffices for the reduction.

| Result | Count |
| --- | ---: |
| Five-mark placements | 11,368 |
| Subset prices reconstructed | 363,776 |
| Impossible because a marked vertex already has eight neighbors | 3,308 |
| Degree-feasible placements with a verified reduction | 8,060 |
| Degree-feasible placements with no budget slack | 36 |

Among the feasible rows the verifier chose deletions with two, three and four marks in 2,573, 5,351 and 136 cases, respectively. It checked 310,750 internal triangles meeting the chosen deletion and 10,784 distinct exit purchases counted across the placements. As an actual incidence test the recorded check added a nine-clique outside the cone, made each unmarked rim vertex complete to it, and connected each mark to the first $6-d_L(z)$ clique vertices. All five marks now have degree exactly seven. The 45,081 triangles leaving the tested deletions in these completions all meet a bought exit. Arbitrary shared exits and exterior edges are covered by the preceding proof.

For example, in `GEr^vo` with marks $0,2,3,5,6$, choose $S=\{0,3\}$ and $h=8$. The internal purchase count is 12, and marks 0 and 3 can have one exit each. These seven edge-disjoint triangles pay the full cost of 14.
$$
 478,\quad358,\quad146,\quad137,\quad268,\quad045,\quad036.
$$
Here each string gives the three vertex labels of one triangle. The six internal labels outside the deletion are $1,2,4,5,6,7$. Their nine actual mutual edges are all bought, together with $03,08,38$. The same arrangement works if either exit is absent.

If an eight had at most three neighbors of degree at least eight, at least five of its neighbors would have degree at most seven, supplying one of the excluded placements. Thus, for $H=\{v:d(v)\ge8\}$, an eight $h$ has $|N(h)\cap H|\ge4$. The earlier low-neighbor theorem gives $r(z)=|N(z)\cap H|\ge4$ for every $z\in N(h)\setminus H$. Indeed the only possible nonhigh vertices with $r=3$ are fives subsumed by three vertices of degree at least nine. It follows that
$$
 w(h)=1+\sum_{z\in N(h)\setminus H}\frac1{r(z)}
       \le 1+\frac{4}{4}=2 .
$$
The earlier charge calculation gives $s(h)=1$. [Low-neighbor and degree-eight charge bounds](donor-lemmas.md#fractional)

**Direct density consequence.** The existing surplus transfer from fives with clique links gives adjusted nonnegative surplus $s'$, with the same total, and ratio $w/s'\le 11/8$ on a nine paying two fives. All other nines have $w/s'\le31/13$. For twelves with at least three high neighbors, use the earlier weight bound $w\le1+(12-j)/4+f/12$, where $f$ counts subsumed fives. If $f>0$, at most $12-6=6$ neighbors can be low. Thus always $f\le6,\ w\le15/4$, and $s'\ge s\ge5/3$ gives $w/s'\le9/4$. Twelves with $j\le2$ already have ratio at most $15/13$. The preceding table bounds all tens by $7/3$, elevens by $19/8$, and all degrees at least thirteen by $7/3$. All the bounds for degrees at least eleven are strictly below $31/13$, since $19\cdot13=247<248=31\cdot8$. [Inherited degree table](donor-lemmas.md#fractional) · [Surplus transfer](donor-lemmas.md#rebate)

Kandasamy's maximum-degree-ten theorem supplies a vertex of degree at least eleven in a violation. Hence at least one comparison is strict. Summing gives $|V|=\sum_{h\in H}w(h)<(31/13)\sum_v s'(v)=(31/13)(2|E|-7|V|)$. Consequently every graph with maximum average degree at most $7+13/31=230/31$ satisfies Tuza. This bound is already obtained before any further study of the nine paying a five and a six. [Kandasamy, Theorem 1.1](https://arxiv.org/html/2610.15269v1#S1)

The public verifier evaluates all 11,368 five-mark placements on the retained classes. [Marked eight-link verification](../verification/check_eight_placements.py)

<a id="nine"></a>

## One subsumed five and one subsumed six at a nine

~~~text
          view from x                      view from z

            h  a  b                       h  a  b  c
             \ | /                          \ | | /
             x                               z
            / \                             / \
           p   q                           r   t

    h is the degree-nine donor in both views. Its three high peers are a,b,c.
    Each letter in the top row sees every other neighbor in its own view.
    The two views share their three letters h,a,b. Outside adjacencies at
    p,q,r,t must be considered when selecting any of them for deletion.
~~~

**Proposition.** In a subgraph-minimal Tuza violation, a nine with exactly three neighbors of degree at least eight cannot subsume both a five with exactly three such neighbors and a nonthin six. The two links force ten distinct displayed vertices, six optional edges, and an affordable reduction on all 64 assignments. The unrestricted density endpoint requested for this check, $\operatorname{mad}(G)\le7+8/19=141/19$, follows inclusively from the prior donor bounds. ****

### The forced edges

Write $H=\{u:d(u)\ge8\}$, $r(v)=|N(v)\cap H|$, and $j(h)=|N(h)\cap H|$. Subsumption of a neighbor $v$ by $h$ means $N[v]\subseteq N[h]$. In a subgraph-minimal violation, degrees five and six form an independent set. A five has at least three subsumers of degree at least nine. A nonthin six has at least four subsumers, all of degree at least eight. In the link of any vertex, its subsumers are precisely the universal vertices. These statements follow from the missing-edge matching in the low links and the degree exclusions in Puleo's Lemma 2.7. [Puleo, Lemmas 2.6–2.8, pp. 5–7](https://arxiv.org/pdf/1308.2211v3#page=5)

The five $x$ has $r(x)=3$. Its three high neighbors are therefore precisely its subsumers, say $h,a,b$. Write its other two neighbors as $p,q$. Both have degree seven, so $pq$ is absent. Otherwise the full five-link would be a clique and both would subsume $x$. At the six $z$, the other three subsumers besides $h$ must be the three high peers of $h$, because $h$ subsumes $z$. These are $a,b,c$. Its other two neighbors, $r,t$, are sevens. Their edge is absent since it would make them subsumers of $z$.

The open neighborhoods of $x,z$ lie in $\{h\}\cup(N(h)\setminus\{x,z\})$, an eight-element set. Botler–Fernandes–Gutiérrez's lemma for robust irreducible graphs would force both degrees to be five if the union had size at most seven. Thus the union has size eight and its intersection has size $5+6-8=3$. The three common vertices $h,a,b$ exhaust it. This excludes all private identifications, and the nine neighbors of $h$ are exhausted. [Botler–Fernandes–Gutiérrez, Lemma 3.3, p. 4](https://arxiv.org/pdf/2002.07925v2#page=4)

For the bank labeling use $(h,a,b,c,x,z,p,q,r,t)=(0,1,2,3,4,5,6,7,8,9)$. Every vertex among $h,a,b$ sees every other displayed vertex. Among the seven remaining vertices the mandatory edges are $xp,xq,zc,zr,zt,cr,ct$. The only undecided edges are $cp,cq,pr,pt,qr,qt$, in that bit order. An edge from $x$ or $z$ outside its named neighborhood is impossible because its degree is exhausted. This gives all 64 potential labeled graphs irrespective of whether each can occur in a minimal violation.

### All 64 reductions

The recorded check reconstructed the cone from the three universal vertices and the seven specified remaining edges, independently of the bank generator. For each mask the recorded check formed all actual internal triangles, checked distinct purchase edges and that every packed triangle exists, and checked disjointness of every pair of packed triangles. Deleting the listed root set $U$ leaves every surviving packed edge among the internal purchases. Each internal triangle meeting $U$ contains a purchased edge.

The displayed neighborhoods of $h,x,z$ are complete. When a marked private seven $v\in\{p,q,r,t\}$ is also deleted, purchase all $7-d_{G[N[h]]}(v)$ edges from $v$ outside the display. Every ambient triangle meeting a deleted root and leaving the display contains one of those purchases. If two roots have the same exterior neighbor their two incident exits are still distinct edges. The packing is wholly internal. The total cost is at most twice the packing size, so both solutions lift from the proper subgraph obtained by deleting the roots and all purchases. [Puleo, Definition 2.1 and Lemma 2.2](https://arxiv.org/pdf/1308.2211v3#page=4)

| Replayed quantity | Result |
| --- | ---: |
| Distinct masks and valid reductions | 64 |
| Packed triangles across the rows | 507 |
| Internal root-triangle checks | 3,010 |
| Internal purchases across the rows | 925 |
| Exit purchases across the rows | 56 |
| Rows using zero / one / two exits | 20 / 32 / 12 |
| Rows with budget slack zero / one | 31 / 33 |

Two additional controls at every mask identify all possible exterior exits as much as possible, or keep them disjoint, and add all edges among exterior vertices and from them to $a,b,c$. They produce respectively 216 and 168 further rooted triangles across the rows. The universal ambient argument above applies also to every intermediate identification.

### Strictness at the stated endpoint

Use the previously audited weight $w(h)=1+\sum_{y\in N(h)\setminus H}1/r(y)$ and the adjusted nonnegative surplus $s'$, which returns $4/15$ from each five with clique link to each of its five subsumers. Thus $\sum_{h\in H}w(h)=|V|$, $s'(h)\ge s(h)$, and $\sum_vs'(v)=2|E|-7|V|$. If $f$ counts the fives subsumed by $h$, every neighboring vertex with $r=3$ is one of them, giving $w(h)\le1+(d-j)/4+f/12$. [Weight and original rows](donor-lemmas.md#fractional) · [Clique-five surplus return](donor-lemmas.md#rebate)

The mixed nine has $f=1$, $j\ge3$ and $s'\ge2-2/3-1/4=13/12$. When $j\ge4$, $w\le7/3$, giving $w/s'\le28/13$. When $j=3$, the reductions above force $r(x)\ge4$. Every nonhigh neighbor now sends at most $1/4$, giving $w/s'\le(5/2)/(13/12)=30/13$. Both are strictly less than $19/8$. A nine with two subsumed fives has $w/s'\le11/8$ by the verified return of surplus. The other nine rows have maximum $17/8$. Each eight has at least four high neighbors and $s=1$, giving $w/s'\le2$. [Eight-neighbor weight audit](donor-lemmas.md#eight)

At an eleven with $j\ge4$, the numerator $19/6$ in the earlier table allowed $f=5$. A donor with any subsumed low has at most $d-6=5$ low neighbors by Puleo 2.7(g). If it has exactly five, the open neighborhoods of all subsumed lows are in the same seven-set $\{h\}\cup(N(h)\setminus\{\text{low neighbors}\})$. The checked three-low reduction excludes three subsumed lows on that set. Hence $f\le4$, $w\le1+7/4+4/12=37/12$, and $s'\ge4/3$ gives $w/s'\le37/16<19/8$. At twelve and $j\ge3$, the same published neighbor bound gives $f\le6$, including $f=0$ when no low is subsumed. Thus $w\le1+9/4+6/12=15/4$ and $s'\ge5/3$ gives $w/s'\le9/4<19/8$. The seven-set argument is only needed for the eleven comparison here. [Three-low reduction and degree-dependent bounds](low-vertex-reductions.md#local) · [Published low-neighbor bound, Lemma 2.7(g)](https://arxiv.org/pdf/1308.2211v3#page=6)

The inherited maxima for ten, eleven with $j\le3$, twelve with $j\le2$, and every $d\ge13$ are respectively $7/3,44/21,15/13,7/3$, all strictly below $19/8$. Therefore every high row satisfies $w(h)<(19/8)s'(h)$. Summation gives $|V|<(19/8)(2|E|-7|V|)$, proving average degree strictly greater than $141/19$ in any subgraph-minimal violation. Every subgraph of a graph of maximum average degree at most $141/19$ inherits the upper bound, so the requested endpoint is inclusive. The strict pointwise comparisons suffice at this endpoint. [Inherited full degree table](donor-lemmas.md#fractional)

The complete 64-mask check includes the shared and disjoint exit controls. [Mixed-nine verification](../verification/check_mixed_nine.py)

<a id="high-donors"></a>

## The fractional count at degree eight and above

~~~text
         high neighbors of a nonhigh y          degree-ten donor and three fives

            a ——— b                                       h
             \   /                                      / | \
               h                                       x₁ x₂ x₃
               |                                  N(xᵢ) ⊆ D,  |D|=8
               y                               |D \ N(xᵢ)|=3 for each i
~~~

In the first panel $h,a,b$ are the only high neighbors of $y$, and the three drawn edges are the proposed exact-three-neighbor conclusion. The edge $hy$ carries weight $1/3$. If $h$ sees fewer than two other high vertices, such a $y$ cannot occur and every incoming nonhigh share is at most $1/4$. The second panel concerns actual open neighborhoods of three degree-five vertices subsumed by $h$; the three omitted triples lie in one eight-set.

### Fixed verdict

**Every subgraph-minimal violation of Tuza has average degree strictly above $22/3$.** Therefore every finite simple graph $G$ with $\operatorname{mad}(G)\le22/3$ satisfies $\tau_\triangle(G)\le2\nu_\triangle(G)$. The calculation uses each nonhigh vertex's actual number of high neighbors, the checked seven-link count, and a local Fano-line reduction. The threshold improves the preceding $80/11$ by $2/33$. [Preceding degree-nine reduction and charge table](donor-lemmas.md#nine-budget)

#### Exactly three high neighbors

Write $H=\{v:d(v)\ge8\}$ and $r(y)=|N(y)\cap H|$. Previously checked results give $r(y)\ge3$ for every vertex outside $H$. The high neighbors of each $y$ with $r(y)=3$ form a triangle.

For a low $y$, the thin sixes have six high neighbors and a nonthin six has at least four high subsumers. A five with exactly three high neighbors has precisely its three pairwise adjacent subsumers as those neighbors. If a seven $y$ sees a low, the low cannot be a thin six; $y$ cannot be a subsumer. The high subsumers of the low all neighbor $y$ and each other. Hence $r(y)=3$ forces a five with precisely those three subsumers.

If a seven $y$ sees no low and $r(y)=3$, every other neighbor is seven. Gupta's connected non-WKE seven-link census supplies at least three neighbors on incident edges of codegree at least four. Such an edge going to a seven is impossible: codegrees five/six reduce, and at codegree four a common tip beyond the standard local degree budget must be high. There are at most three such tips, so the checked pair certificates give a reduction. Thus exactly three vertices of the seven-link have link degree at least four, precisely the three high neighbors. [Seven–seven domain and independent pair checks](paired-sevens.md#pair) · [Gupta, §§4–9](https://arxiv.org/html/2608.06538v1)

The recorded check generated the seven-link data without assuming a graph catalogue. Fix the three link-degree-at-least-four labels. Enumerate both induced graphs on the parts of sizes three and four, and all incidence rows between them, retaining exactly the desired degree inequalities. Of 11,484 labeled candidates on this fixed triple, group the relabelings under $S_3\times S_4$, test connectivity, and test WKE by enumerating all actual matchings $M$ and all vertex sets $Q$ of size $|M|$. Smaller $Q$ can be enlarged. There are three connected non-WKE orbits; their fixed-triple sizes are 24, 36 and 72. In all three, the prescribed vertices are pairwise adjacent. Over the 35 possible fixed triples this accounts for 4,620 labeled graphs.

#### The paid degree eight

Suppose $h$ has degree eight and subsumes a nonthin degree-six vertex $x$. Their five common neighbors $C$ form $K_5$ or $K_5-e$, since any missing link edge at $x$ avoids the universal vertex $h$. The two private neighbors $a,b$ of $h$ have arbitrary contacts with $C$ and with each other. Both root neighborhoods are now completely specified. Put
$$
 X=E(G[C])\cup\{xh,ha,hb\}.
$$
On $\{x,h,0,1,2,3,4\}$, taking $C=\{0,1,2,3,4\}$, the seven triangles $xh0,x12,x34,h13,h24,014,023$ use the 21 distinct pairs exactly once. If $e$ is absent, omit its one triangle. Every packed edge outside $\{x,h\}$ is in $X$, as is an edge of every triangle at either root. The cost/packing sizes are $13/7$ or $12/6$. The actual rooted reduction transfers regardless of exterior contacts. The recorded check on the minimal and maximal edge sets recovered 22,528 private attachments and 646,144 root-triangle incidences. A degree eight cannot subsume a five by Puleo and cannot meet a thin six by Kandasamy's local reduction. Thus **every eight pays no charge**. [Fixed local certificate](seven-links.md#eight-spokes) · [Earlier thin-six dependency](low-vertex-reductions.md#local)

The proposed fallback is also valid. Before using the Fano reduction, a paying eight has just one subsumed nonthin six and surplus $3/4$. Put $j=|N(h)\cap H|$. At $j=3$ that six's link is $K_6-e$, and the endpoints of $e$ are both nonhigh. The six and these two neighbors each see the four high subsumers; each can contribute at most $1/4$ to $h$. The remaining two nonhigh neighbors contribute at most $1/3$ each, yielding $w\le1+3/4+2/3=29/12$ and $w/s\le29/9$. At $j=4$ the six itself contributes only $1/4$, giving $w\le1+1/4+3/3=9/4$; at $j\ge5$, $w\le2$. The excluded $j=3$ case alone would have limited the resulting threshold to $212/29$.

#### Actual weights and strictness at eleven

For each $h\in H$ use
$$
 w(h)=1+\sum_{y\in N(h)\setminus H}\frac{1}{r(y)}.
$$
Then $\sum_{h\in H}w(h)=|V|$ exactly. When $j\le1$, a nonhigh neighbor with $r=3$ would force two other high neighbors of $h$ by the triangle property. Consequently $w\le1+(d-j)/4$ for $j\le1$. For $j\ge2$, $w\le1+(d-j)/3$.

Let $s(v)$ be Puleo's final charge minus seven. All $s(v)\ge0$ and $\sum_v s(v)=2|E|-7|V|$. At degree eight $s=1$, and the two bounds above both imply $w\le3$. At degree nine the earlier proof already gives $w\le3s$. More explicitly, at most one subsumed low gives $s\ge4/3,w\le4$; two including a six give $s\ge13/12,w\le3$. Two subsumed fives have only the clique-link, union-seven case left, giving $s=2/3,j\ge6,w\le2$. [Degree-nine proof](donor-lemmas.md#nine-budget)

At degree ten with no subsumed low, any payment is to a thin six and $s\ge3-10/6=4/3$. For $j\le1$, $w\le7/2$; for $j\ge2$, $w\le11/3$. With a subsumed low, $j\ge2$, so $w\le11/3$. Write $\ell=|N(h)\cap L|$, where $L$ is the independent set of lows. Puleo gives $\ell\le4$. For $\ell=4$, every subsumed low has its open neighborhood in the same seven-set. At most two can be subsumed by the BFG three-low reduction in the previous proof, so the loss is at most $2(2/3)+2(1/6)=5/3$. For $\ell\le3$, unless three fives are subsumed, the loss is at most $2(2/3)+1/4=19/12$. Either way, $s\ge4/3$. [Puleo, Lemma 2.7(g)](https://arxiv.org/pdf/1308.2211) · [Explicit three-low reduction](low-vertex-reductions.md#local)

The exception has exactly three lows, all subsumed fives. Each open neighborhood is a five-subset of the same eight-set $\{h\}\cup(N(h)\setminus L)$. Its complement there has size three, and three triples cannot be pairwise disjoint on eight vertices. Some two neighborhoods have union of size at most seven. BFG Lemma 3.3 forces that union to have size seven and both links to be cliques. All six peers of $h$ in that union are therefore high subsumers adjacent to $h$. Here $s=1$ and $w\le1+(10-6)/3=7/3$. [BFG, Lemma 3.3](https://arxiv.org/pdf/2002.07925)

For every $d\ge11$, the earlier charge bound gives $3s\ge d-7$. If $d\ge13$, $w\le1+d/3<d-7$. For $d=12$, $j\ge1$ gives $w\le1+11/3<5$, and $j=0$ gives $w\le4$. For $d=11$, $j\ge3$ gives $w\le1+8/3<4$, while $j=0$ or $1$ gives $w\le1+11/4<4$. It remains to handle $d=11,j=2$. A thin-six neighbor would give four other high neighbors in its octahedral link; subsuming a nonthin six would give at least three. Any subsumed five must therefore have $h$ and the same two other highs as subsumers. Two such fives would have neighborhood union of size at most seven and hence clique links, forcing at least four fellow high subsumers, impossible. Thus the eleven loses at most $2/3$, giving $s\ge10/3$ and $w\le4<3s$. **Every donor of degree at least eleven satisfies strict inequality.**

Kandasamy's maximum-degree-ten theorem forces at least one such donor in a violation. It follows that $|V|=\sum_h w(h)<3\sum_v s(v)=3(2|E|-7|V|)$. The average degree is strictly above $22/3$. A counterexample with $\operatorname{mad}\le22/3$ would contain a subgraph-minimal one satisfying the same maximum-average-degree bound, proving the endpoint. Kandasamy's global theorem remains a cited preprint-level dependency for strictness. [Kandasamy, Theorem 1.1](https://arxiv.org/abs/2610.15269)

<a id="nine-budget"></a>

## Independent count for the degree-nine donor

~~~text
               complete N(x)                       complete N(y)
             h   k   a   p   q                  h   k   b   r   s
             ●   ●   ●   ●   ●                  ●   ●   ●   ●   ●
                      \     /                            \     /
                        x  ───────── h ────────────────  y

   In the T=3 row, pq and rs are the sole absent edges in the two links.
   Vertices h,k,a subsume x. Vertices h,k,b subsume y.
   The nine private contacts {a,p,q} × {b,r,s} are free before the reduction.
~~~

The rows list all five neighbors of each low vertex. All seven peers $k,a,b,p,q,r,s$ see $h$. Outer neighbors of these peers are initially unrestricted. The drawing records required edges inside the two links; the additional contacts between the private triples require their own check.

### Fixed conclusion

Every subgraph-minimal Tuza violation has average degree strictly greater than $80/11$. Consequently every finite simple graph with maximum average degree at most $80/11$ satisfies $\tau_\triangle\le2\nu_\triangle$. The new local step removes **all** degree-nine two-five configurations with open-neighborhood union eight. The additional common neighbor may be universal, nonuniversal, or universal on just one side. The proof depends on the previously checked three-high-neighbor lemma and charging bounds. [Three-high-neighbor proof and finite audit](paired-sevens.md#pair)

#### What the equality row forces

Here a *high* is a vertex of degree at least eight, a *low* has degree at most six, and $h$ subsumes $x$ when $hx$ is present and $N[x]\subseteq N[h]$. Let $h$ have degree nine and subsume two distinct fives $x,y$. The lows are independent. Their open neighborhoods are both contained in $\{h\}\cup(N(h)\setminus L_{\rm low})$, of size at most eight. BFG Lemma 3.3 excludes union size below seven. At union size seven it makes both links cliques, so the other six vertices in the union all subsume a five, have degree at least nine, and neighbor $h$. [Puleo, Lemma 2.7](https://arxiv.org/pdf/1308.2211) · [Botler–Fernandes–Gutiérrez, Lemma 3.3](https://arxiv.org/pdf/2002.07925)

At union size eight, $x,y$ have exactly two common neighbors $h,k$. Write their private triples as $A=\{a,p,q\}$ and $B=\{b,r,s\}$. Then
$$
 N(x)=\{h,k\}\cup A,\quad N(y)=\{h,k\}\cup B,\quad
 N(h)=\{x,y,k\}\cup A\cup B.
$$
Each five-link is a clique or a clique missing one edge, by Puleo 2.7(a). No missing edge involves the subsumer $h$. Let $T=|N(h)\cap H_{\rm high}|$. At $T=3$, neither link is complete: a complete five-link gives $h$ four other high neighbors immediately. Each five therefore has exactly two fellow subsumers besides $h$. The two pairs of fellow subsumers are distinct, as the intersection of the two open neighborhoods has just $h,k$. With only three highs in the peer set they must intersect precisely in $k$. Thus $k$ is universal in both links, the other fellow subsumers may be named $a,b$, and the four vertices $p,q,r,s$ all have degree seven. Their respective missing edges are $pq$ and $rs$. This proves the roles in the opening picture. The stronger reduction below permits every role of $k$.

#### Six reductions covering all attachments

Up to permuting the private triples, a five-link has the following three possibilities. $P$ misses an edge between two private vertices, $K$ misses an edge from $k$ to a private vertex, and $C$ is complete. Label
$$
 (0,1,2,3,4,5,6,7,8,9)=(h,k,x,y,a,p,q,b,r,s).
$$
For $P$ omit $56$ on the left or $89$ on the right. For $K$ omit $15$ on the left or $18$ on the right. Exchanging the two low vertices makes six unordered role pairs sufficient. The minimum graph is $K_{\{0,1,2,4,5,6\}}\cup K_{\{0,1,3,7,8,9\}}$ with the prescribed omissions. The maximum graph adds all nine edges from $\{4,5,6\}$ to $\{7,8,9\}$. These are exactly the free edges on the ten named vertices. Any further ambient edges at $k$ or at the private vertices are allowed.

In every row remove $\{0,2,3\}$. Concatenate vertex labels to specify each triangle or edge.

| Roles | Packed triangles | Purchased edges | Sizes $(\lvert S\rvert,\lvert X\rvert)$ |
|---|---|---|---:|
| $PP$ | 124 046 138 015 039 078 179 | 03 04 05 06 12 14 15 17 18 19 24 46 78 79 | (7,14) |
| $KP$ | 013 378 026 124 045 079 | 01 03 04 05 06 13 14 26 45 78 79 | (6,11) |
| $KK$ | 124 389 078 016 137 025 456 | 02 07 08 09 13 14 16 17 37 45 46 56 78 89 | (7,14) |
| $CP$ | 079 256 046 137 012 038 145 | 02 07 08 09 13 14 15 16 17 37 45 46 56 79 | (7,14) |
| $CK$ | 139 089 024 016 037 256 145 | 01 02 07 08 09 14 15 16 19 37 45 46 56 89 | (7,14) |
| $CC$ | 079 178 245 046 126 015 139 038 | 03 04 05 06 12 15 16 17 18 19 25 45 46 78 79 89 | (8,16) |

Every listed packing and every purchased edge occurs in its minimum graph. Within a row all packed edges are distinct, including all edges disjoint from the removed triple, each of which is purchased. The cover meets every triangle at roots $0,2,3$ in the maximum graph, so the same witness works under every private attachment. For a direct check, the verifier regenerates the three complete neighborhoods and tests the actual triangles through the roots at each of the $2^9$ settings per row. It also verifies edge-disjointness, inclusion of the outside packed edges in the purchases, and $|X|\le2|S|$. Since the three roots have exactly the displayed neighborhoods in $G$, a new ambient vertex cannot make a further root triangle. Puleo's reduction lifts to $G$ and contradicts minimality.

#### Density and endpoint

Let $s(v)$ be final charge minus seven under Puleo's rule. Then $s(v)\ge0$ and $\sum_v s(v)=2|E|-7|V|$. For each high $h$ of degree $d$ put $T=|N(h)\cap H_{\rm high}|$ and $w(h)=1+(d-T)/3$. Every nonhigh vertex has at least three high neighbors by the preceding round, so $\sum_h w(h)\ge|V|$. A nine subsuming two fives has $s=2/3$ and $w/s=(12-T)/2$. Excluding $T=3$ alone would give $w/s\le4$ and the conditional endpoint $29/4$. At $T=4$ the coefficient is exactly four before any further local exclusion. The six witnesses remove union size eight altogether. The only possible two-five row now has union seven, $T\ge6$, and $w/s\le3$.

For clarity, here is the full comparison with the already reviewed charge rows. A payment of a nonthin six or five is made by a subsumer. Thin-six payments cannot occur at degrees eight or nine. [Structural bounds, thin-six exclusion and transfer rules](low-vertex-reductions.md#local)

| Donor | Upper bound on $w/s$ |
|---|---:|
| Eight, no subsumed low | $11/3$ |
| Eight, one subsumed six | $32/9$ |
| Nine, at most one subsumed low | $3$ |
| Nine, two subsumed lows including a six | $36/13$ |
| Nine, two subsumed fives | $3$ |
| Ten, no subsumed low | $13/4$ |
| Ten, some subsumed low | $11/3$ |
| $d\ge11$ | $(d+3)/(d-7)\le7/2<11/3$ |

For eight, the sole possible nonthin payment is $1/4$ and gives at least three high neighbors. For nine, at most one payment costs at most $2/3$. For two including a six the charge is at least $2-2/3-1/4=13/12$ and there are at least three high neighbors. For ten without a subsumed low the charge is at least $3-10/6=4/3$. In the paying case there are at least two high neighbors and the earlier bound $s\ge(d-7)/3$ gives $s\ge1$. The same bound handles all larger degrees.

Kandasamy's maximum-degree-ten theorem implies that every violation has a vertex of degree at least eleven. Hence at least one comparison is strict, and
$$
 |V|\le\sum_h w(h)<\frac{11}{3}\sum_h s(h)
       \le\frac{11}{3}(2|E|-7|V|).
$$
Rearrangement gives average degree strictly greater than $80/11$. Maximum average degree is hereditary, proving the claimed inclusive threshold. The external theorem used for endpoint strictness remains cited at preprint level. [Kandasamy, Theorem 1.1](https://arxiv.org/abs/2610.15269)

The two-five witness check covers all 49 labeled choices of holes and 512 cross-edge masks. [Two-five union verification](../verification/check_union_eight.py)
