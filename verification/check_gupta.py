"""Independent, standard-library checks of the seven-link bridge and codegree-four catalogue."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")

from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "data" / "gupta-c4-v1.json"
SOURCE_DIGEST = "c51ad4aded53ca0ef7b20536a4008345d0f6f84e453441433e105d290319375f"
CORE = tuple(combinations(range(4), 2))
SIDE = tuple((i, j) for j in (4, 5) for i in range(4)) + ((4, 5),)


def pairs(mask, order):
    return {edge for i, edge in enumerate(order) if mask & (1 << i)}


def bits(edges, order):
    return sum(1 << i for i, edge in enumerate(order) if edge in edges)


def mapped(edges, mapping):
    return {tuple(sorted((mapping[a], mapping[b]))) for a, b in edges}


def adjacency(n, edges):
    row = [0] * n
    for a, b in edges:
        row[a] |= 1 << b
        row[b] |= 1 << a
    return tuple(row)


def connected(row):
    seen = 1
    while True:
        more = seen
        for a, near in enumerate(row):
            if seen & (1 << a):
                more |= near
        if seen == more:
            return seen == (1 << len(row)) - 1
        seen = more


SIZE = tuple(bin(i).count("1") for i in range(128))


@lru_cache(None)
def wke(row):
    """Enumerate the cover Q first. All edges outside Q are forced into the matching."""
    n = len(row)
    full = (1 << n) - 1

    @lru_cache(None)
    def maximum_matching(available):
        if not available:
            return 0
        sing = available & -available
        v = sing.bit_length() - 1
        rest = available ^ sing
        best = maximum_matching(rest)
        neighbors = row[v] & rest
        while neighbors:
            mate = neighbors & -neighbors
            best = max(best, 1 + maximum_matching(rest ^ mate))
            neighbors ^= mate
        return best

    for size in range(n // 2 + 1):
        for subset in combinations(range(n), size):
            outside = full ^ sum(1 << v for v in subset)
            ends = 0
            for v in range(n):
                if not (outside & (1 << v)):
                    continue
                near = row[v] & outside
                if near & (near - 1):
                    break
                if near:
                    ends |= 1 << v
            else:
                if SIZE[ends] // 2 + maximum_matching(full ^ ends) >= size:
                    return True
    return False


def seven_link_bridge():
    """All graphs on seven vertices arise by adjoining one vertex to a six-vertex orbit."""
    order = tuple(combinations(range(6), 2))
    perm = list(permutations(range(6)))
    unseen = set(range(1 << len(order)))
    bases = 0
    tested = 0
    nonwke = 0
    least = 7
    while unseen:
        edges = pairs(min(unseen), order)
        unseen.difference_update(bits(mapped(edges, p), order) for p in perm)
        bases += 1
        for tips in range(64):
            row = adjacency(7, edges | {(a, 6) for a in range(6) if tips & 1 << a})
            tested += 1
            if connected(row) and not wke(row):
                nonwke += 1
                least = min(least, sum(SIZE[neighbors] >= 4 for neighbors in row))
    assert bases == 156 and tested == bases * 64 and least >= 3
    return dict(six_vertex_isomorphism_classes=bases, seven_vertex_extensions=tested,
                connected_nonwke_extensions_with_repetitions=nonwke, least_degree_four_vertices=least)


def catalogue():
    raw = SOURCE.read_bytes()
    assert sha256(raw).hexdigest() == SOURCE_DIGEST
    data = json.loads(raw)
    assert tuple(map(tuple, data["core_bit_order"])) == CORE
    assert tuple(map(tuple, data["side_bit_order"])) == SIDE
    assert data["vertex_labels"] == dict(common=[2, 3, 4, 5], left_exclusive=[6, 7],
                                         right_exclusive=[8, 9], u=0, v=1)
    # Recover every labelled compatible side pair on one representative for each core.
    perm = list(permutations(range(4)))
    cores = {min(bits(mapped(pairs(m, CORE), p), CORE) for p in perm) for m in range(64)}
    bycore = defaultdict(set)
    witnesses = Counter()
    checks = 0
    for record in data["records"]:
        core, left, right = (record[k] for k in ("core_mask", "left_side_mask", "right_side_mask"))
        assert (left, right) not in bycore[core]
        bycore[core].add((left, right))
        part = pairs(core, CORE)
        common = (2, 3, 4, 5)
        edges = {(0, 1)} | {(hub, t) for hub in (0, 1) for t in common}
        edges.update({(0, 6), (0, 7), (1, 8), (1, 9)})
        edges.update(mapped(part, common))
        edges.update(mapped(pairs(left, SIDE), common + (6, 7)))
        edges.update(mapped(pairs(right, SIDE), common + (8, 9)))
        bought = {tuple(sorted(e)) for e in record["cover"]}
        packed = [set(combinations(sorted(t), 2)) for t in record["packing"]]
        used = set().union(*packed)
        assert len(used) == 3 * len(packed) and used <= edges and bought <= edges
        assert len(bought) <= 2 * len(packed)
        assert all(edge in bought for edge in used if min(edge) >= 2)
        cross = tuple(product((6, 7), (8, 9)))
        hub_faces = [set(combinations(t, 2)) for t in combinations(range(10), 3) if t[0] <= 1]
        for choice in range(16):
            ambient = edges | pairs(choice, cross)
            assert all(face & bought for face in hub_faces if face <= ambient)
            checks += 1
        witnesses[core] += 1
    assert set(bycore) <= cores
    pair_total = 0
    for core in sorted(cores):
        common_edges = pairs(core, CORE)
        actions = [p for p in perm if mapped(common_edges, p) == common_edges]
        sides = {}
        for mask in range(512):
            private = pairs(mask, SIDE)
            # The opposite hub is vertex 6 of this seven-link and sees exactly the four common tips.
            row = adjacency(7, common_edges | private | {(x, 6) for x in range(4)})
            if connected(row) and not wke(row):
                sides[mask] = [sum(v in e for e in private) for v in range(4)]
        expected = {(s, t) for s, ds in sides.items() for t, dt in sides.items()
                    if all(a + b + sum(i in edge for edge in common_edges) <= 5
                           for i, (a, b) in enumerate(zip(ds, dt)))}
        pair_total += len(expected)
        images = {}
        for m in sides:
            for p in actions:
                images[m, p] = [bits(mapped(pairs(m, SIDE), p + z), SIDE) for z in [(4, 5), (5, 4)]]
        covered = set()
        for s, t in bycore[core]:
            orbit = set()
            for p in actions:
                for a, b in product(images[s, p], images[t, p]):
                    orbit.update(((a, b), (b, a)))
            assert not (covered & orbit)
            covered.update(orbit)
        assert covered == expected, (core, len(covered), len(expected))
    assert len(data["records"]) == 1144 and checks == 16 * 1144
    return dict(sha256=SOURCE_DIGEST, core_types=len(cores), records=len(data["records"]),
                compatible_labelled_side_pairs_on_representative_cores=pair_total,
                ambient_cross_edge_choices_checked=checks, records_by_core=dict(sorted(witnesses.items())))


if __name__ == "__main__":
    result = dict(link_bridge=seven_link_bridge(), codegree_four=catalogue())
    print(json.dumps(result, indent=2))
