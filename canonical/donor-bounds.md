# The donor table and the 127/17 estimate

<a id="mixed"></a>

~~~text
                     two open neighborhoods at a degree-nine donor h

                       X = N(x)                Z = N(z)
                      5 vertices              6 vertices
                        x has degree 5        z has degree 6
                      X only     X ∩ Z     Z only
                         2          3         3
                                    h
                       X ∪ Z = {h} ∪ (N(h) − {x,z}), size 8

             Four high peers of h, with r(x)=3 and r(z)=4

          X only                 X ∩ Z               Z only
          a, p                   h, b, y              c, d, q
          high, seven            high, high, seven    high, high, seven
               N(x) ∩ H = {a,h,b}       N(z) ∩ H = {h,b,c,d}
                         y sees a,h,b,c,d
~~~

The top panel shows all possible identifications after applying the neighborhood-union lemma. The lower panel draws the only cardinality pattern for the stated pair of high-neighbor counts, up to relabeling. The vertices $x$ and $z$ are nonadjacent, $h$ subsumes both, and edges outside these two open neighborhoods can be arbitrary subject to the ambient hypotheses. Only the indicated incidences and degrees are used. In particular, the third common vertex $y$ sends at most $1/5$ of its weight to $h$.

**Theorem.** Every finite simple graph $G$ with $\operatorname{mad}(G)\le127/17$ satisfies $\tau_\triangle(G)\le2\nu_\triangle(G)$. The thresholds $230/31$ and $209/28$ follow as weaker consequences. The resulting donor coefficient is $17/8$. Its only remaining equality row is a degree-nine vertex paying exactly one five. Attainment of that row in a minimal violation is unknown.

### Accounting in a subgraph-minimal violation

Puleo’s vertex and edge reductions make any subgraph-minimal violation robust and irreducible. These are the hypotheses of the neighborhood-union lemma used below. [Reduction at a small link component](low-vertex-reductions.md#local)

Write $H=\{v:d(v)\ge8\}$ and $L=\{v:d(v)\le6\}$. The minimum degree is five, $L$ is independent, and the vertices outside $H\cup L$ have degree seven. For $h\in H$, write $d=d(h),\,j=|N(h)\cap H|,\,\ell=|N(h)\cap L|$. A vertex $h$ subsumes $v$ when $hv$ is an edge and $N[v]\subseteq N[h]$. Let $f$ count the fives subsumed by $h$. A five receives $2/3$ from each subsumer, a nonthin six receives $1/4$ from each subsumer, and a six with octahedral link receives $1/6$ from each neighbor. All surpluses $s(v)$ above seven after these transfers are nonnegative. Each five with clique link has exactly five high subsumers, has surplus $4/3$, and returns $4/15$ along each of its five edges. Let $s'$ be the adjusted surplus. The repayments give $s'(v)\ge0$ everywhere, $s'(h)\ge s(h)$ on $H$, and $\sum_v s'(v)=2|E|-7|V|$. These identities hold with arbitrary intersections between the neighborhoods of different fives. [Puleo, Lemmas 2.6–2.8](https://arxiv.org/pdf/1308.2211v3#page=5) · [Checked rebate calculation](donor-lemmas.md#rebate)

For $v\notin H$ let $r(v)=|N(v)\cap H|$. The checked low-link results give $r(v)\ge3$, with $r=3$ only for fives whose three high neighbors all subsume them. Every nonthin six has at least four high subsumers. Put
$$
 w(h)=1+\sum_{v\in N(h)\setminus H}\frac1{r(v)}.
$$
Each nonhigh vertex distributes a total of one, so $\sum_{h\in H}w(h)=|V|$. At most $f$ of the contributing neighbors can send $1/3$, while the others send at most $1/4$. Consequently
$$
 w(h)\le 1+\frac{d-j}{4}+\frac f{12},\qquad w(h)\le1+\frac{d-j}{3}.
$$
Every eight pays no charge and has at most four neighbors outside $H$. It cannot subsume a five, so $w/s'\le2$. [Nonhigh-neighbor theorem](seven-links.md#three-high) · [No payment from an eight](donor-lemmas.md#high-donors) · [Unrestricted degree-eight cone audit](donor-lemmas.md#eight)

### The mixed degree-nine row

Suppose a nine $h$ subsumes a five $x$ and a nonthin six $z$. Put $X=N(x)$, $Z=N(z)$, $W=\{h\}\cup(N(h)\setminus\{x,z\})$. The independence of $L$ and subsumption give $X\cup Z\subseteq W$. If $|X\cup Z|\le7$, the neighborhood-union lemma of Botler–Fernandes–Gutiérrez would force both low vertices to have degree five. Hence
$$
          X\cup Z=W,\qquad |W|=8,\qquad |X\cap Z|=3.
$$
Every nonhigh member of $W$ is a seven, since each is a neighbor of $x$ or $z$. The set $W\cap H$ has $j+1$ elements. The six has at least four high subsumers, so $j\ge3$. If $j=3$, then $Z$ contains every high vertex of $W$. Four high neighbors of $x$ would put four vertices in $X\cap Z$. Therefore $r(x)=3$ follows from $j=3$, the hypothesis of the checked 64-mask exclusion. The surviving mixed rows all have $j\ge4$. A direct replay of the separate reviewer's checker on the frozen bank verified 64 reductions, 507 packed triangles, 3,010 internal rooted triangles, 925 internal purchases and 56 exit purchases. [BFG, Lemma 3.3](https://arxiv.org/pdf/2002.07925v2#page=4) · [Actual local witnesses and all ambient exits](donor-lemmas.md#nine)

Here $s'\ge2-2/3-1/4=13/12$. For $j\ge5$ the weight bound gives $w\le25/12$. Suppose $j=4$. The bound $w\le7/3$ uses $1/3$ from $x$, $1/4$ from $z$, and $1/4$ from each of the three remaining sevens. If $r(x)\ge4$, the first contribution saves at least $1/12$. If $r(z)\ge5$, the second saves at least $1/20$. In the remaining case, $r(x)=3$ and $r(z)=4$. Every high neighbor of each low is then its subsumer. Their high neighborhoods cover all five highs of $W$ and share exactly $3+4-5=2$ of them. The third member $y$ of $X\cap Z$ is a seven. Every subsumer of $x$ and every subsumer of $z$ is adjacent to $y$, so $r(y)\ge5$. Its contribution saves at least $1/20$. This proves uniformly
$$
 \frac{w}{s'}\le\frac{7/3-1/20}{13/12}=\frac{137}{65}<\frac{17}{8}.
$$
The diagram shows the tight cardinality case for this calculation. The other possible high-count pairs at $j=4$ are $(3,5)$ and $(4,4)$. The bound for $j\ge5$ is $25/13$.

### Complete donor comparison

The columns give simultaneous safe bounds on $w$ from above, $s'$ from below, and their ratio from above. The degree-ten rows with $j\ge3$ assume some low is subsumed. For degrees eleven and twelve, the last three paired rows also assume some low is subsumed. Entries on either side of a slash in the paired degree column correspond to the separate lines in the exact receipt. The two tail rows give the maxima of their decreasing ratios at $d=13$. [Exact 28-row receipt](donor-bounds.md#mixed)

| Degree | Condition | Upper weight | Lower surplus | Upper ratio |
| --- | --- | ---: | ---: | ---: |
| 8 | All | $2$ | $1$ | $2$ |
| 9 | No payment | $13/4$ | $2$ | $13/8$ |
| 9 | One five | $17/6$ | $4/3$ | **$17/8$** |
| 9 | One six | $5/2$ | $7/4$ | $10/7$ |
| 9 | Two sixes | $5/2$ | $3/2$ | $5/3$ |
| 9 | Two fives | $33/20$ | $6/5$ | $11/8$ |
| 9 | Mixed, $j=4$ | $137/60$ | $13/12$ | $137/65$ |
| 9 | Mixed, $j\ge5$ | $25/12$ | $13/12$ | $25/13$ |
| 10 | No subsumed low, no thin neighbor | $13/3$ | $3$ | $13/9$ |
| 10 | No subsumed low, some thin neighbor | $3$ | $2$ | $3/2$ |
| 10 | Some subsumed low, $j\le2$ | $11/3$ | $7/3$ | $11/7$ |
| 10 | $j\ge3,\ f\le1,\ \ell\le3$ | $17/6$ | $11/6$ | $17/11$ |
| 10 | $j\ge3,\ f\le1,\ \ell=4$ | $17/6$ | $7/4$ | $34/21$ |
| 10 | $j\ge3,\ f=2,\ \ell\le3$ | $35/12$ | $17/12$ | $35/17$ |
| 10 | $j\ge3,\ f=2,\ \ell=4$ | $35/12$ | $28/15$ | $25/16$ |
| 10 | Three subsumed fives | $7/3$ | $23/15$ | $35/23$ |
| 11 / 12 | $j\le2$ | $14/3,\ 5$ | $10/3,\ 13/3$ | $7/5,\ 15/13$ |
| 11 / 12 | $j\ge3$, no subsumed low | $3,\ 13/4$ | $13/6,\ 3$ | $18/13,\ 13/12$ |
| 11 / 12 | $j\ge3,\ \ell=d-6$ | $19/6,\ 41/12$ | $13/6,\ 3$ | $19/13,\ 41/36$ |
| 11 / 12 | $j\ge3,\ \ell\le d-7,\ f\le d-8$ | $13/4,\ 43/12$ | $7/4,\ 25/12$ | $13/7,\ 43/25$ |
| 11 / 12 | $j\ge3,\ \ell=f=d-7$ | $10/3,\ 11/3$ | $28/15,\ 11/5$ | $25/14,\ 5/3$ |
| $d\ge13$ | $j\le2$ | $1+d/3$ | $d-7-2/3$ | $\le1$ |
| $d\ge13$ | $j\ge3$ | $(4d-3)/12$ | $(d-7)/3$ | $\le49/24$ |

**Degree nine.** A nine has no thin neighbors and subsumes at most two lows. Subsuming a five supplies at least two high peers. Subsuming a nonthin six supplies at least three. If two fives are subsumed, their verified union-seven property and BFG's lemma make both links cliques. Each five has $r=5$ and gives a rebate. The donor has at least six high peers and at most one remaining neighbor contributing $1/4$, so $w\le1+2/5+1/4=33/20$ and $s'\ge2-4/3+8/15=6/5$. For a single paid five, equality in $17/8$ needs $j=2$, $r(x)=3$ at this five, and $r=4$ at all six other nonhigh neighbors. [Degree-nine restrictions](donor-lemmas.md#nine-budget) · [Remaining single-payment bounds](donor-lemmas.md#fractional)

**Bounds on the number and cost of payments.** If any low is subsumed, Puleo gives $\ell\le d-6$. Its entire open neighborhood lies in $\{h\}\cup(N(h)\setminus L)$. At $\ell=d-6$ this set has seven vertices, and the checked BFG triple reduction permits at most two subsumed lows. Each of the other low neighbors costs at most $1/6$. If any adjacent thin six occurs, its octahedral link gives at least four high peers of $h$. A subsumed nonthin six gives at least three high peers. With $j\le2$, two subsumed fives must share the donor and its two high peers, making their union have size at most seven. The two forced clique links would give at least four high peers, a contradiction. Thus $j\le2$ costs at most $2/3$. For every $d\ge10$, the inherited bound is $s'\ge s\ge(d-7)/3$. Indeed, with $\ell\le d-7$ the loss is at most $2(d-7)/3$. With $\ell=d-6$ the loss is at most $4/3+(d-8)/6=d/6$. Without any subsumed low the loss is also at most $d/6$. [Puleo, Lemma 2.7(g)](https://arxiv.org/pdf/1308.2211v3#page=6) · [BFG triple reduction and charge proof](low-vertex-reductions.md#local)

**Degree ten.** If no low is subsumed, the presence of a thin neighbor forces $j\ge4$, at most six thin payments, and $f=0$. Otherwise the donor keeps the entire surplus of three. With some subsumed low and $j\le2$, at least two high peers must exist and cost is at most $2/3$. For $j\ge3$ and $f\le1$, loss is at most $2/3+2/4$ when $\ell\le3$. At $\ell=4$ the bound is $2/3+1/4+2/6$, allowing two subsumed lows. With $f=2,\ell\le3$ the loss is at most $4/3+1/4$. With $f=2,\ell=4$ the two fives have neighborhoods in one seven-set and both are clique-link fives, so $s'\ge3-4/3-2/6+8/15$. Three fives require $\ell=3$. Their open neighborhoods are five-subsets of a common eight-set. Three complementary triples cannot be pairwise disjoint, so two neighborhoods have union at most seven. BFG makes both links cliques and their union has size seven, supplying six high peers, two rebates and $w\le1+4/3$. Four subsumed fives cannot occur at ten. [Three-five neighborhood proof](donor-lemmas.md#high-donors)

**Degrees eleven and twelve.** With $j\ge3$, $w\le(d+1)/4+f/12$. If there is no subsumed low, $f=0$ and the loss is at most $d/6$. If there is a subsumed low and $\ell=d-6$, at most two lows are subsumed and the loss is at most $4/3+(d-8)/6$. For $\ell\le d-7,\ f\le d-8$, the bound $2f/3+(\ell-f)/4$ increases in both arguments. It is therefore at most $2(d-8)/3+1/4$. The remaining possibility is $\ell=f=d-7$, so all these four or five lows are subsumed fives. Their open neighborhoods are five-subsets of a common eight-set. Among any three complementary triples two meet, forcing two clique-link fives and hence $s'\ge(d-7)/3+8/15$. This proves every paired row, including the case $f=0$.

**The tail and strictness.** For $d\ge13,\ j\le2$, the ratio is at most $(d+3)/(3d-23)$, decreasing from $1$. For $j\ge3$, one always has $f\le d-6$, by the low-neighbor bound if $f>0$. Consequently
$$
 \frac{w}{s'}\le\frac{4d-3}{4(d-7)}
 =1+\frac{25}{4(d-7)}\le\frac{49}{24}<\frac{17}{8}.
$$
All rows with $d\ge11$ are strictly below $17/8$. Kandasamy's maximum-degree-ten theorem supplies at least one such vertex in a subgraph-minimal violation. Since every high has positive adjusted surplus, summing yields
$$
 |V|=\sum_{h\in H}w(h)
    <\frac{17}{8}\sum_{h\in H}s'(h)
    \le\frac{17}{8}(2|E|-7|V|).
$$
Its average degree must exceed $7+8/17=127/17$. Every subgraph inherits the asserted maximum-average-degree bound, proving the inclusive endpoint. This uses Kandasamy's global theorem at preprint level. The improvement over $209/28$ is $3/476$. [Kandasamy, Theorem 1.1](https://arxiv.org/html/2610.15269v1#S1)
