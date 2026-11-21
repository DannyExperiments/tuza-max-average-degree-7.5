"""Exact pair-reduction decision on a fixed cross-free ten-vertex local graph."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")


from itertools import combinations
import json
from time import monotonic

import pair_domain as D
from pathlib import Path
from pair_witness import indices, store_one, transport, tri_edges, verify


def clique_at_least(weights, compatible, target):
    order_mask = sum(1 << i for i, w in enumerate(weights) if w > 0)
    nodes = 0

    def solve(candidates, need):
        nonlocal nodes
        nodes += 1
        if need <= 0:
            return []
        if not candidates:
            return None
        # Partition the compatible-triangle graph into independent color
        # classes. A packing can take at most one member of each class.
        rest, bounds, vertices = candidates, [], []
        upper = 0
        while rest:
            current = rest
            class_max = 0
            while current:
                bit = current & -current
                i = bit.bit_length() - 1
                current &= ~bit & ~compatible[i]
                rest ^= bit
                class_max = max(class_max, weights[i])
                vertices.append(i)
                bounds.append(upper + class_max)
            upper += class_max
        for i, bound in zip(reversed(vertices), reversed(bounds)):
            if bound < need:
                return None
            answer = solve(candidates & compatible[i], need - weights[i])
            if answer is not None:
                return [i] + answer
            candidates ^= 1 << i
        return None

    return solve(order_mask, target), nodes


def solve_graph(key, cross_mask=0):
    cross = {e for i, e in enumerate(D.CROSS) if (cross_mask >> i) & 1}
    edges = D.graph(key) | cross
    spokes = sorted(D.BASE)
    pindex = {e: i for i, e in enumerate(spokes)}
    triangles = [t for t in combinations(range(10), 3) if tri_edges(t) <= edges]
    edges_of = [tri_edges(t) for t in triangles]
    # Try weight-bearing endpoint triangles first in the coloring order.
    compat = [sum(1 << j for j, f in enumerate(edges_of) if e.isdisjoint(f))
              for e in edges_of]
    forced_data = [(set(e) - D.BASE, sum(1 << pindex[f] for f in e & D.BASE))
                   for t, e in zip(triangles, edges_of) if t[0] < 2]
    sym = [p for p, tab in D.transforms() if D.transform(key, tab) == key and
           transport(cross, p) == cross]
    spoke_perms = [[1 << pindex[D.edge(p[a], p[b])] for a, b in spokes] for p in sym]
    unseen = set(range(1 << len(spokes)))
    candidates = []
    while unseen:
        mask = min(unseen)
        q = list(indices(mask))
        unseen -= {sum(p[i] for i in q) for p in spoke_perms}
        star = {spokes[i] for i in q}
        forced = set()
        for rim, spoke_mask in forced_data:
            if mask & spoke_mask:
                continue
            if not rim:
                break
            forced.update(rim)
        else:
            weights = [2 - len(e - D.BASE - forced) for e in edges_of]
            candidates.append((len(star) + len(forced), star, forced, weights))
    nodes = 0
    for rank, (target, star, forced, weights) in enumerate(sorted(candidates, key=lambda x: x[0])):
        picked, count = clique_at_least(weights, compat, target)
        nodes += count
        if picked is not None:
            packing = [triangles[i] for i in picked]
            cover = star | forced | (set().union(*(edges_of[i] for i in picked)) - D.BASE)
            verify(key, packing, cover, cross_mask=cross_mask)
            return {"key": key, "cross_mask": cross_mask, "nodes": nodes, "spoke_orbits_examined": rank + 1,
                    "eligible_spoke_orbits": len(candidates),
                    "certificate": store_one(key, (0, 1), packing, cover, ["weighted clique"])}
    return {"key": key, "cross_mask": cross_mask, "nodes": nodes, "eligible_spoke_orbits": len(candidates),
            "spoke_orbits_examined": len(candidates), "no_pair_reduction": True}


if __name__ == "__main__":
    start = monotonic()
    out = []
    for key in (8372190, 8372223, 8388607):
        actions = [p for p, tab in D.transforms() if D.transform(key, tab) == key]
        unseen = set(range(16))
        while unseen:
            rep = min(unseen)
            chosen = {e for i, e in enumerate(D.CROSS) if (rep >> i) & 1}
            images = {}
            for p in actions:
                edges = transport(chosen, p)
                image = sum(1 << i for i, e in enumerate(D.CROSS) if e in edges)
                images[image] = p
            assert set(images) <= unseen
            unseen -= images.keys()
            result = solve_graph(key, rep)
            result["cross_mask_orbit"] = sorted(images)
            if "certificate" in result:
                row = result["certificate"]
                for mask, p in images.items():
                    pack = transport(row["packing"], p)
                    cover = transport(row["cover"], p)
                    verify(key, pack, cover, cross_mask=mask)
            out.append(result)
            print(key, rep, result["cross_mask_orbit"], "YES" if "certificate" in result else "NO",
                  result["nodes"], f"{monotonic() - start:.2f}s", flush=True)
    (Path(__file__).resolve().parent / "data" / "PAIR_EXACT.json").write_text(json.dumps(out, indent=2) + "\n")
