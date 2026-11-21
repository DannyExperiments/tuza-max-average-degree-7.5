"""Replay the positive seven-link, four-tip, and twin-root certificates using actual edges."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")


from collections import Counter
from hashlib import sha256
from itertools import combinations, permutations, product
from math import factorial
from pathlib import Path
import json


HERE = Path(__file__).resolve().parent / "data"
V = tuple(range(7))
ALL = tuple(combinations(V, 2))
BIT = {e: 1 << i for i, e in enumerate(ALL)}
ATLAS_SHA256 = "5a878f1a46606da4733df250bf9a412d6ae0b3c73c2112e25d66ba00ae565b56"


def edge(a, b):
    return tuple(sorted((a, b)))


def triangle(vertices):
    return set(combinations(sorted(vertices), 2))


def check_reduction(vertices, edges, roots, packing, bought):
    used = set()
    assert bought <= edges and len(bought) <= 2 * len(packing)
    for t in packing:
        actual = triangle(t)
        assert len(actual) == 3 and actual <= edges and not (actual & used)
        assert all(roots.intersection(e) or e in bought for e in actual)
        used |= actual
    obligations = [triangle(t) for t in combinations(vertices, 3)
                   if roots.intersection(t) and triangle(t) <= edges]
    assert all(t & bought for t in obligations)
    return len(obligations)


def all_matchings(vertices):
    if not vertices:
        yield (0, 0)
        return
    first, later = vertices[0], vertices[1:]
    yield from all_matchings(later)
    for i, v in enumerate(later):
        for mask, n in all_matchings(later[:i] + later[i+1:]):
            yield (mask | BIT[first, v], n + 1)


def atlas():
    raw = (HERE / "graph7.g6").read_bytes()
    assert sha256(raw).hexdigest() == ATLAS_SHA256
    witnesses = json.loads((HERE / "SEVEN_CENSUS.json").read_text())["witnesses"]
    seen = set()
    orbit_sum = 0
    hist, covered, obligations = Counter(), Counter(), 0
    masks = sorted(all_matchings(V), key=lambda r: -r[1])
    assert len(masks) == len(set(masks)) == 232
    cover_masks = [[sum(BIT[e] for e in ALL if set(e) & set(q)) for q in combinations(V, k)]
                   for k in range(4)]
    required = []
    for name in raw.decode("ascii").splitlines():
        assert name[0] == "F"
        binary = "".join(f"{ord(c)-63:06b}" for c in name[1:])
        order = [(i, j) for j in V for i in range(j)]
        E = {e for e, flag in zip(order, binary) if flag == "1"}
        neighbors = [{u for u in V if edge(u, v) in E} for v in V]
        degrees = [len(n) for n in neighbors]
        degree_classes = [[v for v in V if degrees[v] == d] for d in sorted(set(degrees))]
        encodings = Counter()
        for order_blocks in product(*(permutations(block) for block in degree_classes)):
            image = sum(order_blocks, ())
            encoding = sum(BIT[i, j] for i, j in ALL if edge(image[i], image[j]) in E)
            encodings[encoding] += 1
        canonical = min(encodings)
        assert canonical not in seen
        seen.add(canonical)
        size, remainder = divmod(factorial(7), encodings[canonical])
        assert remainder == 0
        orbit_sum += size
        conn = {0}
        for _ in V:
            conn |= set().union(*(neighbors[v] for v in conn))
        mask = sum(BIT[e] for e in E)
        wke = any(m & mask == m and any(mask & ~(m | q) == 0 for q in cover_masks[k])
                  for m, k in masks)
        if len(conn) < 7 or wke:
            assert name not in witnesses
            continue
        large = sum(d >= 4 for d in degrees)
        hist[large] += 1
        if large <= 4:
            required.append(name)
            assert name in witnesses
        if name in witnesses:
            cert = witnesses[name]
            matching = [tuple(m) for m in cert["M"]]
            assert len({v for m in matching for v in m}) == 2*len(matching)
            faces = [tuple(t) for t in cert["D"]]
            packing = [(*m, 7) for m in matching] + faces
            bought = set(matching) | {edge(v, 7) for v in cert["Q"]}
            for t in faces:
                bought |= triangle(t)
            cone = E | {(v, 7) for v in V}
            obligations += check_reduction(range(8), cone, {7}, packing, bought)
            covered[large] += 1
    assert orbit_sum == 2**21 and len(seen) == 1044
    assert sum(hist.values()) == 117 and sum(covered.values()) == len(witnesses) == 40
    return {"catalogue_sha256": ATLAS_SHA256, "isomorphism_types": len(seen),
            "labelled_orbit_sum": orbit_sum, "non_WKE_by_large_degrees": dict(sorted(hist.items())),
            "certified_by_large_degrees": dict(sorted(covered.items())), "necessary_rows": required,
            "root_faces_verified_in_40_certificates": obligations}


def pairs():
    C, A, B = tuple(range(2, 6)), (6, 7), (8, 9)
    cross = tuple(product(A, B))
    basis = list(combinations(C, 2))
    for S in (A, B):
        basis += [(c, s) for s in S for c in C] + [S]
    base = {(0, 1)} | {(i, c) for i in (0, 1) for c in C} | {(0, a) for a in A} | {(1, b) for b in B}
    remaining = json.loads((HERE / "PAIR_AUDIT.json").read_text())["remaining"]
    graphs = {}
    for key in remaining:
        E = base | {e for i, e in enumerate(basis) if int(key) & (1 << i)}
        assert all((c, p) in E for c in C for p in A+B)
        core_degrees = sorted(sum(edge(c, v) in E for v in C) for c in C)
        assert core_degrees == ([2]*4 if key == "8372190" else [3]*4)
        assert ((A in E), (B in E)) == ((key == "8388607"), False)
        graphs[int(key)] = E
    assert sorted(graphs) == [8372190, 8372223, 8388607]
    cycle = graphs[8372190]
    records = json.loads((HERE / "PAIR_EXACT.json").read_text())
    checked = set()
    for row in records:
        if row["key"] != 8372190 or "certificate" not in row:
            continue
        cert = row["certificate"]
        crosses = {e for i, e in enumerate(cross) if row["cross_mask"] & (1 << i)}
        for swap, left, right in product((False, True), permutations(A), permutations(B)):
            image = ((1, 0) + C + right + left) if swap else ((0, 1) + C + left + right)
            mapped = {edge(image[u], image[v]) for u, v in crosses}
            X = {edge(image[u], image[v]) for u, v in cert["cover"]}
            P = [tuple(image[v] for v in t) for t in cert["packing"]]
            check_reduction(range(10), cycle | mapped, {0, 1}, P, X)
            checked.add(sum(1 << i for i, e in enumerate(cross) if e in mapped))
    assert checked == set(range(1, 16))
    return {"exception_masks": sorted(graphs), "C4_actual_cross_patterns_with_checked_pair_witness": sorted(checked)}


def twins():
    H, R, B = (0, 1, 2, 3), (4, 5, 6), (7, 8, 9)
    parts = (H[:2], H[2:], R, B)
    E = {edge(u, v) for i, part in enumerate(parts) for other in parts[i+1:] for u in part for v in other}
    J = H+B
    bought = {e for e in E if set(e) <= set(J)}
    packing = [(R[i], B[j], H[(i+j) % 3]) for i in range(3) for j in range(3)]
    faces = check_reduction(range(10), E, set(R), packing, bought)
    assert len(packing) == 9 and len(bought) == 16 and faces == 48
    for mask in range(1 << len(J)):
        attachments = {edge(v, 10) for i, v in enumerate(J) if mask & (1 << i)}
        assert check_reduction(range(11), E | attachments, set(R), packing, bought) == faces
    minimum_edges = {q: min(sum(not set(e).intersection(Q) for e in bought)
                            for Q in combinations(J, q)) for q in range(4)}
    assert minimum_edges == {0: 16, 1: 11, 2: 6, 3: 3}
    return {"full_group_edges": len(E), "packed": packing, "purchases": sorted(bought),
            "obligations": faces, "one_outside_vertex_patterns_checked": 128,
            "minimum_edges_after_q_deleted_rim_vertices": minimum_edges}


if __name__ == "__main__":
    result = {"atlas": atlas(), "four_tip_exceptions": pairs(), "group": twins()}
    (HERE / "FOUR_HIGH_AUDIT.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result["atlas"].items() if k != "necessary_rows"}))
    print("Necessary rows", len(result["atlas"]["necessary_rows"]), "group obligations", result["group"]["obligations"])
