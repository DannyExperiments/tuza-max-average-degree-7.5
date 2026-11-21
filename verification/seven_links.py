"""Check all unlabelled seven-rims and every choice of high positions."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")


from collections import Counter
from hashlib import sha256
from itertools import combinations, permutations, product
from math import factorial
from pathlib import Path
import json


HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
CATALOGUE = DATA / "graph7.g6"
BANK = DATA / "SEVEN_CENSUS.json"
VERTICES = tuple(range(7))
PAIRS = tuple(combinations(VERTICES, 2))
BIT = {e: 1 << i for i, e in enumerate(PAIRS)}


def edge(a, b):
    return (a, b) if a < b else (b, a)


def graph6(word):
    assert len(word) == 5 and word[0] == "F"
    digits = "".join(f"{ord(c)-63:06b}" for c in word[1:])
    assert set(digits[21:]) == {"0"}
    return frozenset((i, j) for j in VERTICES for i in range(j)
                     if digits[j*(j-1)//2+i] == "1")


def canonical(edges, neighborhoods):
    # The order lists old labels at new positions. Every isomorphism preserves
    # degree, so a common sorted degree order loses no identifications.
    blocks = [[v for v in VERTICES if len(neighborhoods[v]) == degree]
              for degree in range(7)]
    codes = Counter()
    for parts in product(*(permutations(block) for block in blocks if block)):
        old = tuple(v for part in parts for v in part)
        image = sum(BIT[i, j] for i,j in PAIRS if edge(old[i], old[j]) in edges)
        codes[image] += 1
    code = min(codes)
    return code, codes[code]


def all_matchings(unused):
    if not unused:
        yield 0, 0
        return
    a, *others = unused
    yield from all_matchings(others)
    for b in others:
        for chosen, size in all_matchings([v for v in others if v != b]):
            yield chosen | BIT[edge(a,b)], size+1


MATCHINGS = list(all_matchings(VERTICES))
assert len(MATCHINGS) == 232
OUTSIDE = [[sum(BIT[a,b] for a,b in PAIRS if a not in subset and b not in subset)
            for subset in combinations(VERTICES, size)] for size in range(4)]


def is_wke(graph):
    # Pad the bought-spoke set to the size of its matching.
    return any(not (graph & outside & ~matching)
               for matching, size in MATCHINGS if graph & matching == matching
               for outside in OUTSIDE[size])


def verify_cone(edges, record):
    apex = 7
    cone = edges | {(v,apex) for v in VERTICES}
    packed = [tuple(sorted(t)) for t in record["D"]]
    packed.extend(tuple(sorted((a,b,apex))) for a,b in record["M"])
    used = [e for t in packed for e in combinations(t,2)]
    assert len(set(used)) == len(used) == 3*len(packed)
    bought = {e for e in used if apex not in e} | {(v,apex) for v in record["Q"]}
    assert set(used) | bought <= cone
    assert len(bought) <= 2*len(packed)
    assert all(set(combinations((a,b,apex),2)) & bought for a,b in edges)
    return len(edges)


def main():
    catalogue = CATALOGUE.read_bytes()
    words = catalogue.decode().splitlines()
    certificates = json.loads(BANK.read_text())["witnesses"]
    seen, positive = set(), set()
    stages = Counter()
    marking_counts = Counter()
    results = []
    for word in words:
        edges = graph6(word)
        graph = sum(BIT[e] for e in edges)
        nbr = [{v if w == i else w for v,w in edges if i in (v,w)}
               for i in VERTICES]
        code, aut = canonical(edges, nbr)
        assert code not in seen
        seen.add(code)
        stages["labelled_orbit_mass"] += factorial(7)//aut
        stages["rim_types"] += 1
        reached = {0}
        for _ in VERTICES:
            reached |= set.union(*(nbr[v] for v in reached))
        if len(reached) < 7:
            continue
        stages["connected"] += 1
        if is_wke(graph):
            continue
        stages["connected_non_WKE"] += 1
        if word in certificates:
            positive.add(word)
            stages["root_triangles_on_positive_cones"] += verify_cone(edges, certificates[word])
            continue
        stages["after_40_positive_cones"] += 1
        wide = {v for v in VERTICES if len(nbr[v]) >= 4}
        assert len(wide) >= 5
        for r in range(8):
            for marked in combinations(VERTICES, r):
                stages["all_markings_after_cone_filter"] += 1
                high = set(marked)
                if not wide <= high:
                    continue
                stages["all_wide_positions_are_high"] += 1
                tri = [t for t in combinations(marked,3)
                       if set(combinations(t,2)) <= edges]
                spines = [e for e in edges if all(v in high for v in e)
                          and all(set(e) <= set(t) for t in tri)]
                if tri and not spines:
                    continue
                stages["surviving_markings"] += 1
                marking_counts[r] += 1
                # The zero-triangle case passes the screen without a marked
                # spine, even if the marked subgraph has no edges.
                assert tri and len(spines) == 1
                u,v = spines[0]
                nonhigh = set(VERTICES) - high
                missed = [d for d in nonhigh if {u,v}.isdisjoint(nbr[d])]
                assert missed and all(len(nbr[d]) == 3 for d in missed)
                results.append({"graph6":word,"edges":sorted(edges),"high_positions":marked,
                                "wide_positions":sorted(wide),"high_triangles":tri,
                                "only_spine":(u,v),"nonhigh_missing_both_ends":sorted(missed),
                                "automorphisms_of_unmarked_rim":aut})
    assert stages["rim_types"] == 1044 and stages["labelled_orbit_mass"] == 2**21
    assert positive == set(certificates) and len(positive) == 40
    assert len(results) == 2 and set(marking_counts) == {5,6}
    assert all(r["graph6"] == "FEzvO" and r["only_spine"] == (4,6) for r in results)
    receipt = {"catalogue_sha256":sha256(catalogue).hexdigest(),
               "positive_bank_sha256":sha256(BANK.read_bytes()).hexdigest(),
               "stages":dict(stages), "markings_by_high_count":dict(marking_counts),
               "survivors":results}
    (HERE/"SEVEN_REPLAY.json").write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print(json.dumps(dict(stages),sort_keys=True))


if __name__ == "__main__":
    main()
