"""Read saved records and check each actual graph with every private cross set."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")


from collections import Counter
from itertools import combinations, product
from pathlib import Path
import gzip
import json


HERE = Path(__file__).resolve().parent / "data"
PAIRS = tuple(combinations(range(10), 2))
BITS = {e: 1 << i for i, e in enumerate(PAIRS)}
C, A, B = (2, 3, 4, 5), (6, 7), (8, 9)
CORE = tuple(combinations(C, 2))
RIM = CORE + tuple((i, j) for j in A for i in C) + (A,)
RIM += tuple((i, j) for j in B for i in C) + (B,)


def mask(edges):
    return sum(BITS[e] for e in set(tuple(sorted(pair)) for pair in edges))


BASE = mask([(0, 1)] + [(u, c) for u in (0, 1) for c in C] + [(0, a) for a in A]
            + [(1, b) for b in B])
TRI = {t: mask(combinations(t, 2)) for t in combinations(range(10), 3)}
CROSSES = [mask(e for i, e in enumerate(product(A, B)) if (m >> i) & 1) for m in range(16)]


def read_zipped(name):
    return json.loads(gzip.decompress((HERE / name).read_bytes()))


def check_one(record):
    key = record["key"]
    assert record["roots"] == [0, 1]
    graphs = [BASE | mask(e for i, e in enumerate(RIM) if (key >> i) & 1) | c
              for c in CROSSES]
    selected = mask(record["cover"])
    packed = [TRI[tuple(sorted(t))] for t in record["packing"]]
    used = 0
    for tri in packed:
        assert not (used & tri)
        used |= tri
    assert not (used & ~BASE & ~selected)
    assert bin(selected).count("1") <= 2 * len(packed)
    root_tri = [v for t, v in TRI.items() if t[0] <= 1]
    for graph in graphs:
        assert not ((used | selected) & ~graph)
        assert all(v & selected or v & ~graph for v in root_tri)
    return len(graphs)


def check_special_rim():
    # h=0; s,t=1,2; L=3,4,5; R=6,7,8.
    parts = [(0,), (1, 2), (3, 4, 5), (6, 7, 8)]
    edges = {e for a, part in enumerate(parts) for other in parts[a + 1:] for e in product(part, other)}
    x = mask(set(product(parts[2], parts[3])) | {(0, 1), (0, 2)})
    p = [(1, 3+i, 6+i) for i in range(3)] + [(2, 3+i, 6+(i+1) % 3) for i in range(3)]
    placed = [TRI[t] for t in p]
    roots = mask(e for e in edges if 1 in e or 2 in e)
    assert len(placed) == 6 and bin(x).count("1") == 11
    assert all(a & b == 0 for a, b in combinations(placed, 2))
    assert not ((sum(placed) | x) & ~mask(edges)) and not (sum(placed) & ~roots & ~x)
    faces = [z for t, z in TRI.items() if (1 in t or 2 in t) and not z & ~mask(edges)]
    assert all(z & x for z in faces)
    return {"packing": p, "cover_size": 11, "triangles_meeting_the_pair": len(faces)}


def main():
    transferred = read_zipped("PAIR_TRANSFER.json.gz")
    one = read_zipped("PAIR_ONE_DEFECT.json.gz")
    generated = read_zipped("PAIR_DIRECT.json.gz")
    receipts = json.loads((HERE / "PAIR_RECEIPT.json").read_text())
    remaining = json.loads((HERE / "PAIR_EXACT.json").read_text())
    rows = {r["key"]: r for r in transferred + generated}
    assert len(rows) == len(transferred) + len(generated) == 3283
    assert len(one) == 986 and all(rows[r["key"]] == r for r in one)
    checks = sum(check_one(r) for r in rows.values())
    failed = {r["key"] for r in remaining}
    assert failed.isdisjoint(rows) and len(failed) == 3
    assert {r["key"] for r in generated} | failed == set(receipts["missing_keys"])
    assert checks == 16 * 3283
    last = {}
    for key in sorted(failed):
        yes, no = [], []
        for r in remaining:
            if key != r["key"]:
                continue
            (no if r.get("no_pair_reduction") else yes).extend(r["cross_mask_orbit"])
        assert sorted(yes + no) == list(range(16))
        last[key] = {"successful_cross_masks": sorted(yes), "failed_cross_masks": sorted(no)}
    print(json.dumps({"unconditional_pair_orbits": len(rows), "actual_graph_checks": checks,
                      "one_6_defect_orbits": len(one), "exceptional_cross_decisions": last,
                      "multipartite_pair": check_special_rim()}, indent=2))


if __name__ == "__main__":
    main()
