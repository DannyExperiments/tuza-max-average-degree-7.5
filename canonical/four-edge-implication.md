# One common maximum on a four-edge path

<a id="four"></a>

u —— a —— z —— b —— y
    first half     second half

The five vertices are distinct. In the graph being packed, u,z,y are pairwise nonadjacent. Other chords are allowed.

**Open test.** Let L be finite and simple, tight, with all its subgraphs satisfying Tuza. Suppose one minimum triangle edge cover avoids all four path edges. There is a maximum packing avoiding ua,az, and there is a possibly different maximum avoiding zb,by. Must there be one maximum avoiding all four? This is a sufficient target for full Tuza. Its truth is unknown.

**Single-edge avoidance and localization.** Let $H$ be tight and suppose every subgraph of $H$ satisfies Tuza. Both packing and covering numbers add over triangle components, where triangles belong to the same component when connected by shared edges. Each nonempty component is consequently tight. In a component $D$ of packing number $b$, deleting one edge leaves cover number at least $2b-1$. The hereditary inequality then gives a packing of size $b$ avoiding that edge. An edge in no triangle already belongs to no packing. If the two edges of a path cannot both be avoided by any maximum packing of $H$, they must therefore be active in the same component. Otherwise one can choose avoiding maxima separately in their respective components and take the union.

**Proof of sufficiency.** Any least violating graph G yields a hereditary tight graph H=G−uv with the same packing rank. For any tip w, no maximum of H avoids both uw and wv, since uvw would extend it in G. Single-edge avoidance in each tight component and additivity localize those legs in one component. Among all hereditary tight component subgraphs of G admitting such a blocked induced two-edge path, choose O of smallest packing rank s. Rename the path u−z−y. Deleting its two legs leaves a tight L of rank s−1, by the two-edge cover lift and heredity.

Fix one minimum cover C of L. On each deleted leg, some returning triangle must have both its old feet outside C. Otherwise C pays that whole book and buying the other leg covers O for 2s−1. If all choices of such uncovered pages across the two books had the same outside tip a, C plus the old edge za would cover O for 2s−1. Thus choose distinct outside tips a,b and obtain the displayed path disjoint from C. Each half is individually avoidable in L: failure would localize a blocked induced two-edge path in one hereditary tight component of rank less than s. A single maximum avoiding both halves would append the two distinct-tip pages, giving s+1 in O. This violates the asserted universal test. Hence that test, if proved, would exclude every least Tuza violation.

The two halves are selected using the same minimum cover. Their individual avoiding packings may differ. Their union can block every maximum while each half is avoidable in a five-vertex control when tightness is weakened. Universal simultaneous avoidance remains open.
