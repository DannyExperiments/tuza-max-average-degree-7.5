"""Independent verification of the six input witnesses after every private relabeling."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")


from collections import Counter, defaultdict
import hashlib
from itertools import combinations, permutations, product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PUBLIC = HERE / "data" / "COUNT_WITNESSES.json"
R = frozenset("hxy")
V = "hkxyapqbrs"
LEFT = frozenset("apq")
RIGHT = frozenset("brs")
PAIR = tuple(combinations(range(10), 2))
EDGE_MASK = {frozenset((V[i], V[j])): 1 << t for t, (i, j) in enumerate(PAIR)}


def mask(edges):
    ans = 0
    for e in edges:
        ans |= EDGE_MASK[frozenset(e)]
    return ans


def records(bank):
    # Fix h,k. Independently permute both private triples and exchange whole wings.
    result = {}
    for key, supplied in bank.items():
        missing = [{"P": tuple("pq"), "K": tuple("kp"), "C": None}[key[0]],
                   {"P": tuple("rs"), "K": tuple("kr"), "C": None}[key[1]]]
        for swapped in (False, True):
            first, second = ("brs", "apq") if swapped else ("apq", "brs")
            for p, q in product(permutations(first), permutations(second)):
                new = ("h", "k", "y" if swapped else "x", "x" if swapped else "y") + p + q
                image = dict(zip(V, new))
                holes = frozenset(frozenset(image[a] for a in e) for e in missing if e)
                if holes in result:
                    assert result[holes][0] == key
                    continue
                pack = [tuple(new[i] for i in t) for t in supplied["packing"]]
                cover = [tuple(new[i] for i in e) for e in supplied["cover"]]
                result[holes] = (key, pack, cover)
    return result


def expected_holes(private):
    possible = (None, *(frozenset(e) for e in combinations(sorted(private | {"k"}), 2)))
    assert len(possible) == 7
    return possible


def main():
    source = json.loads(PUBLIC.read_text())
    assert tuple(source["graph_labels"][v] for v in V) == tuple(range(10))
    assert {V[i] for i in source["removed_vertices"]} == R
    bank = source["witnesses"]
    assert set(bank) == {"PP", "KK", "CC", "KP", "CP", "CK"}
    data = records(bank)
    all_holes = {frozenset(e for e in pair if e) for pair in product(
        expected_holes(LEFT), expected_holes(RIGHT))}
    assert set(data) == all_holes and len(data) == 49

    # Each vertex signature specifies its side memberships. Adjacent vertices of
    # a common side are forced unless their precise hole was independently chosen.
    membership = {z: set() for z in V}
    for a in "hkxapq":
        membership[a].add("x")
    for a in "hkybrs":
        membership[a].add("y")
    glued = mask((u, v) for u, v in combinations(V, 2) if membership[u] & membership[v])
    cross_edges = tuple(sorted((a, b) for a in LEFT for b in RIGHT))
    cross_states = [mask(e for j, e in enumerate(cross_edges) if choice >> j & 1)
                    for choice in range(512)]
    all_triples = [(t, mask(combinations(t, 2))) for t in combinations(V, 3)]
    center_triangles = [edges for t, edges in all_triples if R.intersection(t)]
    exterior = mask(combinations(sorted(set(V) - R), 2))
    counts, sizes, ranges = Counter(), {}, defaultdict(set)
    for holes, (key, packing, cover) in data.items():
        base = glued & ~mask(holes)
        packing_masks = [mask(combinations(t, 2)) for t in packing]
        cover_mask = mask(cover)
        assert len(cover) == len(set(map(frozenset, cover)))
        assert len(cover) <= 2 * len(packing) and all(len(set(t)) == 3 for t in packing)
        assert cover_mask & base == cover_mask
        used = 0
        for tri in packing_masks:
            assert not used & tri and tri & base == tri
            used |= tri
        assert used & exterior & ~cover_mask == 0
        sizes[key] = [len(packing), len(cover)]
        for cross in cross_states:
            graph = base | cross
            remaining = graph & ~cover_mask
            obligations = sum(t & graph == t for t in center_triangles)
            # In G-X none of the rooted three-vertex cliques may remain.
            assert not any(t & remaining == t for t in center_triangles)
            # Test the three complete neighborhoods by all pair incidences.
            for center, expected in (("h", set(V) - {"h"}), ("x", set("hkapq")), ("y", set("hkbrs"))):
                actual = {v for v in V if v != center and graph & EDGE_MASK[frozenset((center, v))]}
                assert actual == expected
            ranges[key].add(obligations)
            counts[key] += 1
    assert sum(counts.values()) == 49 * 512
    receipt = {"source_sha256": hashlib.sha256(PUBLIC.read_bytes()).hexdigest(),
               "labelled_hole_choices": len(data), "total_graphs_checked": sum(counts.values()),
               "by_shape": {key: {"packing_cover_sizes": sizes[key], "graphs": counts[key],
                                  "actual_triangles_meeting_deleted": sorted(ranges[key])}
                            for key in sorted(bank)}}
    (HERE / "union_eight.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
