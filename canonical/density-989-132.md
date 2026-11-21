# The counting estimate at 989/132

<a id="count"></a>

~~~text
             the only high peers of a nine h          a shared five x
                         a — b                         high triangle S
                          \ /                         h₁ — h₂
                           h                            \  /
                 x, p, q, t₁,t₂,t₃,t₄                    h₃

            p and q each see x,h,a,b.             A limiting four-high six
            The edge pq is absent.                meets S in two subsumers.
~~~

**Result.** Every finite simple graph $G$ with $\operatorname{mad}(G)\le989/132$ satisfies $\tau_\triangle(G)\le2\nu_\triangle(G)$. The limiting single-five nine in the previous proof has six seven-neighbors of high-neighbor count at least five. A second consequence of the same seven-link classification lowers the mixed-nine bound. Distributing the counting unit at its five across the three high subsumers then gives the coefficient $132/65$. The bound is inclusive. The inclusive endpoint uses Kandasamy’s maximum-degree-ten preprint.   · [Prior unrestricted accounting](donor-bounds.md#mixed)

### 1. What the old equality case actually forces

Work in a subgraph-minimal violation. A high vertex has degree at least eight, and a low has degree five or six. Let $H$ be the high set, $r(v)=|N(v)\cap H|$, and $j(h)=|N(h)\cap H|$. Write $h$ subsumes $x$ when $hx$ is an edge and $N[x]\subseteq N[h]$. The lows form an independent set. Every five has at least three high subsumers, and every nonthin six has at least four. A thin six has octahedral link with six high neighbors. Every seven has at least four high neighbors and at least five spokes whose endpoints have four or more common neighbors. Call such a spoke *wide*. If a seven $p$ has exactly four high neighbors, their induced graph is either $K_4$ or $C_4$, including when $p$ has a low neighbor. [Puleo, Lemmas 2.6–2.8](https://arxiv.org/pdf/1308.2211v3#page=5) · [Complete quartet statement and independent seven-link audit](seven-links.md#quartet)

Suppose the nine $h$ has precisely two high peers $a,b$, and its only charge payment is to a five $x$. Its three high subsumers must be $h,a,b$, so $ab$ is an edge. Apart from $x$ every nonhigh neighbor of $h$ is a seven. Another five would either be subsumed by $h$ or have three distinct high subsumers adjacent to $h$. A nonthin six adjacent to $h$ would require at least three other high peers of $h$. A thin six would give at least four from its octahedral link. Smaller degrees are excluded by robustness.

For any such seven $p$, its high quartet, if $r(p)=4$, contains $h$. A $K_4$ would give $h$ three high peers. In an induced $C_4$ its two neighbors must be $a,b$, yet those two are adjacent. Hence **all six sevens satisfy $r\ge5$**. This argument applies to any high vertex whose two high peers are adjacent, with the conclusion on its degree-seven neighbors. Under the old counting weight, the single-five donor satisfies
$$
              w(h)\le 1+\frac13+\frac65=\frac{38}{15},
   \qquad \frac{w(h)}{s'(h)}\le\frac{19}{10}.
$$
The result bounds every donor of this type even if its local configuration occurs.

**Example.** Start with a high triangle $h,a,b$, all joined to the five $x$ and six vertices $p,q,t_1,\ldots,t_4$. Join $x$ to $p,q$. On those six vertices use $K_{3,3}-pq$ with parts $\{p,t_1,t_2\},\{q,t_3,t_4\}$. Join an additional vertex $k$ to all six and attach a fresh $K_9$ meeting the rest only at $k$. Give the graph exactly these edges. The 19-vertex, 76-edge graph has three degree-nine subsumers, degree five at $x$, and degree seven with $r=4$ at all six designated vertices. Just changing the three shares of $x$ leaves the three donors' combined weight $17/2$ and combined surplus $4$, so their maximum ratio is at least $17/8$. Each seven's high quartet is $K_3$ plus the isolated $k$ and violates the verified quartet rule. This identifies exactly what a redistribution of $x$ alone could miss in an ordinary graph. [Verification](../verification/check_count.py)

### 2. The additional information carried by a five-neighbor

**Lemma.** If a seven $p$ adjacent to a five $x$ has $r(p)=4$, it has a nonthin six neighbor $z$ subsumed by all four vertices of $N(p)\cap H$.

A seven cannot subsume a five. In the five-link the missing edges form a matching of size at most one. The edge $px$ therefore has exactly three common tips. With five wide spokes and four high neighbors, some wide spoke from $p$ must lead to a nonhigh vertex $t$. It cannot lead to a five, since codegree four would make $p$ its subsumer. If $t$ is a seven, the verified five- and six-tip pair reductions exclude codegrees five and six. For codegree four the complete pair classification leaves three possible rooted support classes, each with four high common tips and all four endpoint-private vertices adjacent to all four common tips. Here $x$ is private at $p$, because a common tip would be high. Adjacency from $x$ to every common tip would give $px$ four common neighbors. The remaining possibility is a six $t$, necessarily nonthin since a thin six has only high neighbors. Its four or more high subsumers all neighbor $p$, hence are exactly $N(p)\cap H$. This proves the lemma. The three representative masks were decoded for the complete private-to-tip incidences. [Pair catalog and three exceptional graphs](paired-sevens.md#pair) · [Five- and six-tip checks](paired-sevens.md#gupta) · [Verification](../verification/check_count.py)

In particular, if $h$ subsumes $x$ and $p\in N(x)$ has degree seven and $r(p)=4$, then $h$ subsumes a nonthin six adjacent to $p$. If $h$ pays only one nonthin six $z$, every seven in $N(x)\setminus N(z)$ has $r\ge5$.

### 3. The old mixed-nine row

Suppose $h$ is a nine paying both a five $x$ and a nonthin six $z$. There are no other payments. The audited mixed-nine result gives $j\ge4$ and
$$
 X=N(x),\quad Z=N(z),\quad
 X\cup Z=\{h\}\cup(N(h)\setminus\{x,z\}),\quad |X\cap Z|=3 .
$$
The union consists of eight vertices. Every nonhigh vertex in it is a seven by low independence. For $j\ge5$ retain $w\le25/12$. At $j=4$ the union has five highs and three sevens. The three possible high-count pairs and their weight bounds are as follows. [Old proof, diagram and 64-case dependency](donor-bounds.md#mixed)

| $r(x),r(z)$ | Seven-neighbor consequence | $w$ at most | $w/s'$ at most |
| --- | --- | ---: | ---: |
| $3,4$ | Of the two sevens in $X$, one lies in $X\cap Z$ and sees all five high subsumers. The other lies outside $Z$ and has $r\ge5$ by §2. | $67/30$ | $134/65$ |
| $3,5$ | Both sevens in $X$ lie outside $Z$, hence both have $r\ge5$. | $131/60$ | $131/65$ |
| $4,4$ | The only seven in $X$ lies outside $Z$, hence has $r\ge5$. | $11/5$ | $132/65$ |

Indeed the number of common highs is $r(x)+r(z)-5$, at most three. This leaves precisely the three listed pairs. In the first row both sets of high neighbors consist entirely of subsumers of their respective lows, so their common seven neighbors their whole high union. Each remaining unaccounted seven sends at most $1/4$. In all rows $s'\ge13/12$.

For comparison, excluding only the original single-five equality would save at least $1/20$ at that vertex and give $w/s'\le167/80$. Excluding all its $j=2$ occurrences would instead retain only $j\ge3$ with $w/s'\le31/16$. **Either hypothesis alone**, with the old mixed bound $137/65$, gives the same inherited cutoff $1024/137=7+65/137$. Section 1 proves the required saving at the full $j=2$ row, and §2 improves the mixed coefficient to $134/65$, giving $1003/134$ even before reallocating any weight. All degrees at least eleven were already bounded by $49/24<134/65$. [Complete prior comparison](donor-bounds.md#mixed)

### 4. A redistribution with three actual high subsumers

Call a donor of the first mixed row in §3 a marked nine. Each such $h$ is associated with its unique five $x$, which has precisely three high neighbors $S=N(x)\cap H$, all subsumers of $x$. At the target $C=132/65$, the deficit $w(h)-Cs'(h)$ is at most $67/30-11/5=1/30$.

For a marked $h$, its paid six $z_h$ sees exactly two vertices of $S$, including $h$. Both subsume $z_h$, because all four of its high neighbors are subsumers. If all three vertices of $S$ were marked, the sets $N(z_h)\cap S$ for the distinct paid sixes would partition $S$ into pairs. Indeed any overlap at a marked donor would force it to pay two different sixes as well as $x$, contradicting the two-low bound at nine. Hence at most two members of $S$ are marked.

If exactly one is marked, reduce the weight sent by $x$ to it by $1/30$ and add $1/60$ to each of the other two shares. If two are marked, reduce each of the two shares by $1/30$ and add $1/15$ to the third. All original shares are $1/3$. This independently preserves the total weight of each five. Denote the resulting weight at a high vertex by $\widehat w$. Marked donors receive no transfers from a different five because they subsume exactly one. Any other donor subsuming $f$ fives can receive at most $f/15$ across all its fives.

A mixed nine of type $(4,4)$ cannot receive a transfer, because it subsumes only its own five, whose $r$ is four. A mixed nine $g$ of type $(3,5)$ can receive at most $1/60$. For if it were the third subsumer of a five shared by two marked donors $h_1,h_2$, consider their paid sixes. If $z_1\ne z_2$, the other member of $N(z_i)\cap S$ must be $g$ for each $i$, or a marked donor would pay both sixes. Then $g$ pays $x,z_1,z_2$, impossible. If $z_1=z_2=z$, the other six $z_g$ with $r(z_g)=5$ is distinct from $z$ and sees every member of $S$, since all five available highs belong to $N(z_g)$. At least four of its five high neighbors subsume it. Thus at least one of $h_1,h_2$ subsumes $z_g$ as well as $z$, again impossible. Those alternatives cover every identification of the paid sixes. In these three delicate rows the final weights are bounded by
$$
 \frac{67}{30}-\frac1{30}
 =\frac{131}{60}+\frac1{60}
 =\frac{11}{5}
 =\frac{132}{65}\frac{13}{12}.
$$

### 5. Absorbing transfers at every degree

Puleo's adjusted surplus $s'$ is the conserved nonnegative charge above seven after returning $4/15$ along each incidence of a clique-link five. Write $\ell$ for the number of low neighbors at a high donor, and $f$ for its number of subsumed fives. Previously,
$w\le1+(d-j)/4+f/12$ and $w\le1+(d-j)/3$. If some low is subsumed then $\ell\le d-6$. When $\ell=d-6$, the seven-set reduction permits at most two subsumed lows. At $j\le2$ the loss from an initial surplus of $d-7$ is at most $2/3$ and $f\le1$. [Original charge and counting bounds](donor-lemmas.md#fractional) · [Verified surplus return](donor-lemmas.md#rebate)

**Ten paying two fives.** The only previously delicate ten had $j=3,\ f=2,\ \ell\le3$. Suppose it also subsumes a nonthin six $z$. Its three subsumed lows $x_1,x_2,z$ have open neighborhoods inside one eight-set $W=\{h\}\cup(N(h)\setminus\{x_1,x_2,z\})$, with exactly four high vertices $U$. The set $N(z)$ contains all four highs and two sevens. Each $N(x_i)\cup N(z)$ equals $W$ by BFG's low-neighbor union lemma, since the degrees differ. Thus each $N(x_i)$ contains the same two vertices of $W\setminus N(z)$, along with three vertices of $U$. The two fives consequently have intersection of size at least four, or union of size at most six, contrary to the same lemma. This excludes the third nonthin-six payment. There is also no thin adjacency when $j=3$. Thus $s'\ge5/3$. At $j\ge4$ with $f=2,\ell\le3$, $w\le8/3$ and $s'\ge17/12$. In the other ten rows the previous ratio is at most $34/21$, one has $f\le3$, and $s'\ge1$, so even adding $1/5$ to this ratio is sufficient. [BFG, Lemma 3.3](https://arxiv.org/pdf/2002.07925v2#page=4) · [Original ten rows](donor-bounds.md#mixed)

**All $d\ge11$.** Put $k=d-7\ge4$. The following bounds already include the maximum possible receipt $f/15$. For $j\le2$, divide $1+d/3+1/15$ by $d-7-2/3$, obtaining at most $71/50$. For $j\ge3$, one has $w\le(k+8)/4+f/12$.

- With no subsumed low, there is no incoming transfer and the total payment is at most $d/6$. The ratio is at most $3(k+8)/(2(5k-7))\le18/13$.
- With $\ell=k+1$ and some subsumed low, $f\le2$ and $s'\ge(5k-7)/6$, since the loss is at most $4/3+(k-1)/6$. Now $\widehat w\le(k+8)/4+3/10$, for ratio at most $99/65$.
- With $\ell\le k,\ f\le k-1$, the loss is at most $2f/3+(k-f)/4$, giving $s'\ge(9k-5f)/12$. Using $\widehat w\le(k+8)/4+f(1/12+1/15)$, the ratio increases with $f$ and is at most $(24k+111)/(20k+25)\le69/35$.
- If $\ell=f=k$, the $k$ low neighbors are all subsumed fives. Their five-element neighborhoods lie in one eight-set. Among any three of the complementary triples two meet, so BFG gives clique links at two fives and a seven-vertex union. Its six high vertices besides $h$ all neighbor $h$. Thus $j\ge6,\ s'\ge k/3+8/15$ and $\widehat w\le5/4+2k/5$. The ratio is at most $171/112$.

Each displayed rational function of $k$ decreases for $k\ge4$, so these numerical maxima occur at $k=4$. The cases include every possibility and give $\widehat w/s'\le69/35<132/65$ for $d\ge11$.

| Donor and condition | Upper bound on $\widehat w/s'$ |
| --- | ---: |
| Eight | $2$ |
| Nine, no subsumed five or two clique fives | $5/3$ |
| Nine, only one five, $j=2$ or $j\ge3$ | $39/20,\ 159/80$ |
| Nine, mixed with $j\ge5$ | $129/65$ |
| Nine, mixed with $j=4$, all three cases | **$132/65$** |
| Ten, two subsumed fives, $\ell\le3$, $j=3$ or $j\ge4$ | $183/100,\ 168/85$ |
| Ten, remaining rows | $191/105$ |
| Every degree at least eleven | $69/35$ |

For the single-five nine with $j\ge3$, use $w\le31/12$, $s'\ge4/3$ and a receipt of at most $1/15$. With $j=2$ use §1. For a mixed nine with $j\ge5$, add $1/15$ to $25/12$. A nine with two subsumed fives has two clique-link fives, neither of which participates in the redistribution. An eight subsumes no five and receives nothing. These observations account for the remaining table entries. [Verification](../verification/check_count.py)

**Strictness.** The redistributed weight still satisfies $\sum_{h\in H}\widehat w(h)=|V|$, and $\sum_v s'(v)=2|E|-7|V|$. A minimal violation has a donor of degree at least eleven by Kandasamy, so at least one comparison with $C=132/65$ is strict. Therefore $|V|< C(2|E|-7|V|)$, implying average degree strictly greater than $7+65/132=989/132$. A graph of maximum average degree at most this value passes its bound to every subgraph. The remaining potential equality rows in the pointwise accounting are mixed nines with $j=4$; realizability of those rows and the unrestricted conjecture remain open. [Kandasamy, Theorem 1.1](https://arxiv.org/abs/2610.15269)
