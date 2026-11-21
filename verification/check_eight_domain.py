"""Check every exclusion from the complete eight-vertex link catalogue."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")


from collections import Counter
from itertools import combinations
from pathlib import Path
import json

from eight_link import edge, neighbors, read_graph6


V = tuple(range(8))
PAIRS = tuple(combinations(V, 2))
BIT = {e: 1 << i for i, e in enumerate(PAIRS)}
SPOKES = [
    [(q, sum(BIT[e] for e in PAIRS if set(e).intersection(q))) for q in combinations(V, k)]
    for k in range(5)
]


def matchings(remaining):
    if not remaining:
        yield (), 0
        return
    a, *rest = remaining
    yield from matchings(rest)
    for i, b in enumerate(rest):
        for small, mask in matchings(rest[:i] + rest[i + 1:]):
            yield ((a, b),) + small, BIT[a, b] | mask


MATCHINGS = sorted(matchings(V), key=lambda item: -len(item[0]))


def bit_mask(rim):
    return sum(BIT[pair] for pair in rim)


def components(rim):
    remaining = set(V)
    partition = []
    while remaining:
        component = {min(remaining)}
        pending = list(component)
        while pending:
            contacts = neighbors(rim, pending.pop()) - component
            pending.extend(contacts)
            component.update(contacts)
        remaining -= component
        partition.append(component)
    return partition


def wke_witness(rim):
    graph = bit_mask(rim)
    for matching, used in MATCHINGS:
        if used & ~graph:
            continue
        for spokes, hit in SPOKES[len(matching)]:
            if graph & ~(hit | used) == 0:
                return {"M": matching, "D": [], "Q": spokes}
    raise AssertionError(("missing WKE witness", rim))


def check_star(rim, certificate):
    # Remove packed spokes and all purchases. Other spokes may survive.
    root = 8
    matching = [edge(*pair) for pair in certificate["M"]]
    assert len(matching) and len(set(v for pair in matching for v in pair)) == 2 * len(matching)
    rim_faces = [tuple(sorted(t)) for t in certificate["D"]]
    spokes = set(certificate["Q"])
    assert len(spokes) == len(certificate["Q"])
    packing = [(*pair, root) for pair in matching] + rim_faces
    used = [edge(a, b) for t in packing for a, b in combinations(t, 2)]
    assert len(used) == len(set(used)) == 3 * len(packing)
    cone = rim | {(v, root) for v in V}
    assert set(used) <= cone
    bought = {e for e in used if root not in e} | {(v, root) for v in spokes}
    removed_spokes = {e for e in used if root in e}
    assert bought <= cone and len(bought) <= 2 * len(packing)
    assert set(used) <= bought | removed_spokes
    for a, b in rim:
        face = {(a, b), (a, root), (b, root)}
        assert not (face & removed_spokes) or face & bought


def cover_catalogue(names, atlas):
    positive = atlas["positive"]
    retained = set(atlas["surviving"])
    assert len(retained) == len(atlas["surviving"])
    assert retained.isdisjoint(positive) and retained | set(positive) <= set(names)
    screening = Counter()
    for name in names:
        rim = read_graph6(name)
        degrees = [len(neighbors(rim, v)) for v in V]
        if name in retained:
            screening["retained"] += 1
        elif name in positive:
            check_star(rim, positive[name])
            screening["explicit_partial_star"] += 1
        elif min(degrees) <= 1:
            screening["triangle_free_or_unique_triangle_spoke"] += 1
        elif len(parts := components(rim)) > 1:
            piece = min(parts, key=len)
            assert 2 <= len(piece) <= 4
            part_rim = {e for e in rim if set(e) <= piece}
            witness = wke_witness(part_rim)
            check_star(rim, witness)
            screening["WKE_component"] += 1
        else:
            witness = wke_witness(rim)
            check_star(rim, witness)
            screening["WKE_full_link"] += 1
    return screening


if __name__ == "__main__":
    data = Path(__file__).resolve().parent / "data"
    names = (data / "graph8.g6").read_text().splitlines()
    atlas = json.loads((data / "STAR_ATLAS.json").read_bytes())
    assert len(names) == len(set(names)) == 12346
    print(json.dumps(cover_catalogue(names, atlas), sort_keys=True))
