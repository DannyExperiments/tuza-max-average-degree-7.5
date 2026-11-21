"""Physical pair reductions and bit-mask iteration for the exceptional pair graphs."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")

from itertools import combinations

import pair_domain as D


def indices(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def tri_edges(t):
    return set(combinations(sorted(t), 2))


def transport(faces, permutation):
    return {tuple(sorted(permutation[i] for i in face)) for face in faces}


def verify(key, packing, cover, roots=(0, 1), cross_mask=None):
    roots = set(roots)
    low_graph = D.graph(key)
    high_graph = low_graph | set(D.CROSS)
    if cross_mask is not None:
        low_graph |= {e for i, e in enumerate(D.CROSS) if (cross_mask >> i) & 1}
        high_graph = low_graph
    used = [e for tri in packing for e in tri_edges(tri)]
    assert len(used) == 3 * len(packing) and len(set(used)) == len(used)
    assert set(used) <= low_graph and cover <= low_graph and len(cover) <= 2 * len(packing)
    assert all(e in cover for e in used if roots.isdisjoint(e))
    for tri in combinations(range(10), 3):
        if not roots.isdisjoint(tri):
            edges = tri_edges(tri)
            assert not edges <= high_graph or edges & cover, (key, tri)


def store_one(key, roots, packing, cover, via):
    return {"key": key, "roots": list(roots), "packing": sorted(packing),
            "cover": sorted(cover), "via": via}
