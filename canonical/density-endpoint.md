# Density, including the endpoint 15/2

<a id="endpoint"></a>

~~~text
            h belongs to both groups
         five x                         six z
     three high subsumers         four high subsumers
        u  v  h                     h  i  j  k
         \ | /                       \ | | /
          p, q                       p, q
           the same two vertices of degree seven
       r(p), r(q) ≥ 6 because each sees the union
~~~

**Theorem.** For every finite simple graph $G$ with $\mathrm{mad}(G)\le15/2$, $\tau_\triangle(G)\le2\nu_\triangle(G)$. Here the maximum average degree is the maximum of $2|E(F)|/|V(F)|$ over all nonempty subgraphs $F$, and $\tau,\nu$ count triangle-cover edges and edge-disjoint triangles, respectively. The following proof extends the earlier $989/132$ derivation by $1/132$. It uses the earlier local certificates, including Gupta's degree-seven pair bank, and the maximum-degree-ten theorem for strictness. [Earlier proof](density-989-132.md#count) · [Endpoint arithmetic](../verification/check_endpoint.py)

### Starting inequalities

Take a subgraph-minimal violation $F$. Write $H=\{v:d(v)\ge8\}$. A low is a vertex of degree five or six. The minimum degree is at least five and the lows form an independent set. For any vertex $v$, write $r(v)=|N(v)\cap H|$, with the notation $j=r(h)$ at a high $h$. A vertex $h$ subsumes an adjacent $u$ if $N[u]\subseteq N[h]$. A nonthin six has at least four high subsumers. A thin six has an octahedral link, all six neighbors high, and no subsumer. Each five has at least three high subsumers. A donor subsuming a low has degree at least nine. For a seven, $r\ge4$. The earlier proof gives an adjusted vertex weight $\widehat w(h)$ and nonnegative adjusted surplus $s'(v)$ satisfying
$$
\sum_{h\in H}\widehat w(h)=|V(F)|,\qquad \sum_v s'(v)=2|E(F)|-7|V(F)|.
$$
Initially each high counts itself and each other vertex distributes one unit equally among its high neighbors. The previous adjustment only moves shares of a five with exactly three high neighbors, all subsumers. It increases any recipient by at most $1/15$ per such five. The old pointwise bounds and all lower bounds used below are recorded with their proofs and case split. [Old weight and donor table, §§3–5](density-989-132.md#count) · [Surplus at each kind of donor](donor-bounds.md#mixed) · [Puleo](https://arxiv.org/abs/1308.2211) · [Gupta](https://arxiv.org/abs/2608.06538)

We use two structural facts. First, each seven $p$ adjacent to a five $x$ has $r(p)\ge5$. If $r(p)=4$, the earlier seven-link lemma gives a nonthin six $z$ adjacent to $p$, subsumed by all four high neighbors of $p$. At least three subsumers of $x$ neighbor $p$, and so neighbor $z$. Then $p$ and those three highs lie in $N(x)\cap N(z)$, leaving $|N(x)\cup N(z)|\le 5+6-4=7$. Botler–Fernandes–Gutiérrez's low-neighborhood lemma excludes such a union for lows of unequal degree. Second, if a nine subsumes both a five $x$ and a nonthin six $z$, the same union is the full eight-element set $\{h\}\cup(N(h)\setminus\{x,z\})$. Their intersection has size three. Low independence implies all nonhigh members of the union are sevens. Thus $x,z$ are its only low neighbors. [Seven-link deduction, §2 and mixed-nine union, §3](density-989-132.md#count) · [Botler–Fernandes–Gutiérrez, Lemma 3.3](https://arxiv.org/pdf/2002.07925#page=4)

### Where the counting weight can go

Let $L$ consist of mixed nines as above having $j=4$. If $S_t=N(t)\cap H$, then $S_x\cup S_z=\{h\}\cup(N(h)\cap H)$ has size five. The possibilities $(|S_x|,|S_z|)$ are $A=(3,4)$, $B=(3,5)$, $C=(4,4)$, since the whole intersection has size three. Each $h\in L$ satisfies $\widehat w(h)\le11/5,\ s'(h)\ge13/12$ in the old proof.

**Recipient lemma.** Every $h\in L$ has a neighbor $b\in H\setminus L$ which subsumes a low.

For $A$, look across the three labels of $S_x$. If all belonged to $L$, their unique neighboring sixes would partition $S_x$ into sets of size two or three, obtained by intersection with the high sets at those sixes. These are genuine disjoint sets because each marked nine has exactly one adjacent six. The part through $h$ has size two, leaving one. Hence some $b\in S_x\setminus L$; all three labels subsume $x$. For $C$, look across the four labels of $S_z$. Its part through $h$ has size three. If all labels were in $L$, the corresponding fives would partition the set into parts of size at least two, leaving one. All four labels subsume $z$.

For $B$, look across the five labels of $S_z$. Each member in $L$ has a five whose three high neighbors all lie in $S_z$ and subsume that five. Five cannot split into triples. If two or more labels are outside $L$, one subsumes $z$, because at least four of the five subsume it. If there is a unique outsider $b$ and it is in none of the triples, the remaining four labels would split into triples. Indeed a marked label belongs to precisely one five. Therefore $b$ subsumes one of the fives. In all cases $b\ne h$ is adjacent to $h$ because $h$ subsumes the focal low. This proves the lemma even when $b$ fails to subsume that particular six. [Endpoint arithmetic](../verification/check_endpoint.py)

Choose one such $b$ per $h\in L$. Transfer $1/30$ of counting weight from $h$ to $b$, leaving $s'$ unchanged. Each member of $L$ now has weight at most $11/5-1/30=13/6\le2s'$. A recipient sees at most $j$ transfers, one per distinct high neighbor. It has degree at least nine. All nonrecipients outside $L$ already have $\widehat w\le2s'$. We verify the recipient inequality $\widehat w+j/30\le2s'$, with strict inequality in degree at least eleven.

Let $f_3$ count adjacent fives with exactly three high neighbors; each is subsumed. The original shares and first transfer give
$$
 \widehat w\le 1+(d-j)/4+3f_3/20-\mathbf{1}_{f_3>0}/10. \tag{1}
$$
An exceptional five can contribute an extra $1/3-1/4+1/15=3/20$. If one is present, its two nonhigh neighbors are sevens adjacent to $h$, each with $r\ge5$. This saves $2(1/4-1/5)=1/10$ once, even if several fives share them. At fixed $d,f_3$, the sum of this upper bound and $j/30$ decreases with $j$.

### Checking degrees eight, nine and ten

An eight subsumes no low, receives nothing and satisfies $\widehat w\le2s'$.

* **Nine subsuming one five with no subsumed six.** At $j=2$, the old ratio is at most $39/20$ with $s'\ge4/3$. The remaining margin is at least $1/15=2/30$. At $j\ge3$, (1) plus the transfer gives at most $53/20$ if $f_3=1$, and $13/5$ otherwise. Both are below $8/3$. A nine with no subsumed five or with two clique-link fives has old ratio at most $5/3$ and $s'\ge1$; even $9/30$ fits.
* **Mixed nine outside $L$.** Here $j\ge5,\ s'\ge13/12$. If $r(x)\ge4$, (1) gives at most $1+(9-5)/4+5/30=13/6$ after transfer. If $r(x)=3$, the two sevens $p,q$ next to the five both neighbor $h$; thus $j=5$ and the eight-element union consists of six highs and $p,q$. For $r(z)\ge5$, both sevens have $r\ge5$, and the transferred weight is at most $1+1/3+1/5+2/5+1/15+5/30=13/6$. If $r(z)=4$, its two seven-neighbors must be the very same $p,q$. Each sees all three high subsumers of $x$ and all four of $z$. Their union has six members, and both seven shares are at most $1/6$. The transferred weight is at most $1+1/3+1/4+2/6+1/15+5/30=43/20<13/6$.
* **Ten subsuming two fives with at most three low neighbors.** At $j=3$, the earlier ratio is at most $183/100$, $s'\ge5/3$, and $3/30$ fits. At $j\ge4$, $s'\ge17/12$. With $f_3>0$, (1) with $f_3\le2$ gives at most $1+6/4+3/10-1/10+4/30=17/6$, including the transfer. With $f_3=0$ the bound is smaller.
* **Other tens.** The old ratio is at most $191/105$ and every ten here has $s'\ge4/3$, directly from the complete surplus table (the three-five row has $s'\ge23/15$). For $j\le7$ the margin is at least $76/315>7/30$. For $j\ge8$ there are at most two nonhigh neighbors, each original share at most $1/3$ and each increment at most $1/15$. The transferred weight is at most $1+2/3+2/15+10/30<8/3$.

### All higher degrees and strictness

Put $k=d-7\ge4$. Write $\ell$ for the number of low neighbors and $f$ for the number of subsumed fives. The following starting bounds follow from the earlier unlimited-degree argument. [Old §5 and complete case hypotheses](density-989-132.md#count)

* For $j\le2$ the old ratio is at most $71/50$, with $s'\ge k-2/3$, so even $2/30$ leaves strict slack. With no subsumed low a vertex receives nothing, and the old degree-eleven-and-up maximum $69/35$ is strictly less than two.
* Suppose $j\ge3$ and some low is subsumed, so $\ell\le k+1$. If $\ell=k+1$, then $f\le2,\ s'\ge(5k-7)/6$. Formula (1), dropping its saving, gives at most $(k+8)/4+3/10+1/10$ including transfers. The difference to $2s'$ is at least $(85k-284)/60>0$.
* If $\ell\le k,\ f\le k-1$, then $s'\ge(9k-5f)/12$. For $f_3>0$, the $1/10$ saving cancels $3/30$ at the worst $j=3$. The resulting upper bound is $(k+8)/4+3f/20$. The difference to $2s'$ decreases with $f$ and is at least $(16k-61)/60>0$. If $f_3=0$, use $(k+8)/4+1/10$ and $2s'\ge(4k+5)/6$, leaving $(25k-76)/60>0$.
* If $\ell=f=k$, the earlier low-neighborhood argument forces $j\ge6,\ s'\ge k/3+8/15$. Apply (1) at $j=6$, dropping its saving. Including transfers gives at most $29/20+2k/5$, leaving $(16k-23)/60>0$.

All cases now give $w_{\rm final}(h)\le2s'(h)$. Kandasamy's theorem implies any violation has a vertex of degree at least eleven, where the bound is strict. Summing, using nonnegativity away from $H$, gives $|V(F)|<2(2|E(F)|-7|V(F)|)$. Thus $2|E(F)|/|V(F)|>15/2$, contradicting the maximum-average-degree hypothesis. [Kandasamy, Theorem 1.1](https://arxiv.org/abs/2610.15269)

The graph-level deductions use the stated structural reductions and finite local certificates. The Lean file checks the conditional numerical accounting.
