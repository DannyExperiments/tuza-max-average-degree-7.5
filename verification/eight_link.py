"""Ordinary edges, cones, packings and exterior purchases for eight-vertex links."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")


from functools import lru_cache
from itertools import combinations

ROOT = 8
RIM = tuple(range(8))
ALL = tuple(range(9))


def edge(a, b):
    return (a, b) if a < b else (b, a)


def read_graph6(word):
    n = ord(word[0]) - 63
    digits = (bit for char in word[1:] for bit in format(ord(char) - 63, "06b"))
    pairs = ((a, b) for b in range(n) for a in range(b))
    return frozenset(pair for pair, bit in zip(pairs, digits) if bit == "1")


def neighbors(edges, root):
    return {b if a == root else a for a, b in edges if root in (a, b)}


def parts(vertices):
    return [p for size in range(len(vertices) + 1) for p in combinations(vertices, size)]


def sides(triangle):
    assert len(triangle) == len(set(triangle)) == 3
    return frozenset(combinations(sorted(triangle), 2))


def graph_data(name):
    rim = read_graph6(name)
    cone = rim | {(z, ROOT) for z in RIM}
    faces = {t: sides(t) for t in combinations(ALL, 3) if sides(t) <= cone}
    exits = {z: 8 - sum(z in e for e in cone) for z in RIM}
    return rim, cone, faces, exits


def literal_packing(cone, packing):
    all_used = [e for t in packing for e in sides(t)]
    used = set(all_used)
    assert len(used) == len(all_used) == 3 * len(packing) and used <= cone
    return used


def check_optimal(cone, faces, packing):
    """Branch on an ordinary graph edge after the uncovered-edge parity test."""
    target = len(packing) + 1
    index = {e: 1 << i for i, e in enumerate(sorted(cone))}
    incident = [sum(index[e] for e in cone if v in e) for v in ALL]
    face_masks = [sum(index[e] for e in f) for f in faces.values()]
    options = {bit: [f for f in face_masks if f & bit] for bit in index.values()}
    full = sum(index.values())
    def count(bits):
        return bin(bits).count("1")
    def cap(mask):
        odds = sum(count(around & mask) % 2 for around in incident)
        return (count(mask) - odds // 2) // 3

    @lru_cache(None)
    def possible(mask, need):
        if not need:
            return True
        if cap(mask) < need:
            return False
        pivot, choices = min(
            ((bit, [f for f in triangles if not f & ~mask])
             for bit, triangles in options.items() if bit & mask),
            key=lambda item: len(item[1]))
        return (any(possible(mask ^ f, need - 1) for f in choices)
                or possible(mask ^ pivot, need))

    assert not possible(full, target)
    return "parity" if cap(full) < target else "edge_branch"


def internal_requirements(cone, faces, selected, packing, purchases, outside_cost):
    region = {ROOT, *selected}
    outside = set(ALL) - region
    used = literal_packing(cone, packing)
    assert purchases <= cone and all(e in purchases for e in used if set(e) <= outside)
    checked = [es for t, es in faces.items() if region.intersection(t)]
    assert all(purchases & es for es in checked)
    assert len(purchases) + outside_cost <= 2 * len(packing)
    return len(checked)


def check_boundary(rim, triple, selected, exits):
    """Real exterior with maximally shared exits, dense rim contacts and an exterior clique."""
    region = {ROOT, *selected}
    outside_vertices = tuple(range(9, 18))
    outer_neighbors = {z: set(outside_vertices[:exits[z]]) if z in triple else set(outside_vertices)
                       for z in RIM}
    bought = {edge(z, t) for z in selected for t in outer_neighbors[z]}
    assert len(bought) == sum(exits[z] for z in selected)
    # Both kinds of face with vertices outside the cone: two exterior vertices,
    # or one exterior vertex and a second, adjacent rim vertex. The root has no exit.
    actual = {tuple(sorted((z, t, u))) for z in selected for t, u in combinations(outer_neighbors[z], 2)}
    for z, w in rim:
        if {z, w} & region:
            actual.update((z, w, t) for t in outer_neighbors[z] & outer_neighbors[w])
    assert all(sides(t) & bought for t in actual)
    return len(actual)
