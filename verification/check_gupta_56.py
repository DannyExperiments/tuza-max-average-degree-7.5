"""Independent finite check of Gupta 2608.06538v1, Sections 6–8."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")


from collections import Counter, deque
from hashlib import sha256
from itertools import combinations
import json


def size(mask):
    return bin(mask).count("1")


def edge(a, b):
    return (a, b) if a < b else (b, a)


class Coordinates:
    def __init__(self, n):
        self.n = n
        self.pairs = list(combinations(range(n), 2))
        self.bit = {pair: 1 << i for i, pair in enumerate(self.pairs)}
        self.endpoints = [(1 << a) | (1 << b) for a, b in self.pairs]
        self.full = (1 << len(self.pairs)) - 1

    def encode(self, pairs):
        return sum(self.bit[pair] for pair in set(pairs))

    def decode(self, mask):
        return {pair for pair, bit in self.bit.items() if mask & bit}

    def matchings(self):
        # Each edge is offered once; the old list uses only earlier edges.
        result = [(0, 0)]
        for i, endpoints in enumerate(self.endpoints):
            result += [(m | (1 << i), vertices | endpoints)
                       for m, vertices in result if not vertices & endpoints]
        return result

    def orbits(self):
        # Adjacent transpositions generate every vertex permutation.
        swaps = []
        for v in range(self.n - 1):
            perm = list(range(self.n))
            perm[v], perm[v + 1] = perm[v + 1], perm[v]
            swaps.append([self.bit[edge(perm[a], perm[b])] for a, b in self.pairs])
        labels = [-1] * (self.full + 1)
        orbits = {}
        for rep in range(self.full + 1):
            if labels[rep] >= 0:
                continue
            labels[rep] = rep
            queue = deque([rep])
            orbit = []
            while queue:
                mask = queue.popleft()
                orbit.append(mask)
                positions = [i for i in range(len(self.pairs)) if (mask >> i) & 1]
                for image in swaps:
                    other = sum(image[i] for i in positions)
                    if labels[other] == -1:
                        labels[other] = rep
                        queue.append(other)
                    else:
                        assert labels[other] == rep
            orbits[rep] = orbit
        assert sum(map(len, orbits.values())) == self.full + 1
        return labels, orbits


def packing_table(c):
    # Each entry retains two colored matchings and an optional common tip.
    table = [None] * (c.full + 1)
    tip_mask = (1 << c.n) - 1
    match = c.matchings()
    for left, lverts in match:
        for right, rverts in match:
            if left & right:
                continue
            chosen = left | right
            free = tip_mask & ~(lverts | rverts)
            tip = (free & -free).bit_length() - 1
            score = size(chosen) + int(tip >= 0)
            if table[chosen] is None or score > table[chosen][0]:
                table[chosen] = (score, left, right, tip)
    # Max over feasible used sets contained in the allowed edge mask.
    for i in range(len(c.pairs)):
        bit = 1 << i
        for lo in range(0, c.full + 1, 2 * bit):
            for sub in range(lo, lo + bit):
                source, old = table[sub], table[sub | bit]
                if source is not None and (old is None or source[0] > old[0]):
                    table[sub | bit] = source
    return table


def covers(c):
    candidates = sorted(range(1 << c.n), key=lambda v: (size(v), v))
    incident = {v: sum(1 << i for i, ends in enumerate(c.endpoints) if ends & v)
                for v in candidates}
    return [next(v for v in candidates if not (mask & ~incident[v]))
            for mask in range(c.full + 1)]


def ambient(c, h, da=None, db=None, cross=True):
    u, v = c.n, c.n + 1
    graph = c.decode(h) | {edge(u, v)}
    graph |= {edge(k, x) for k in range(c.n) for x in (u, v)}
    if c.n == 5:
        a, b = c.n + 2, c.n + 3
        graph |= {edge(u, a), edge(v, b)}
        for x, contact in ((a, da), (b, db)):
            graph |= {edge(x, k) for k in range(c.n) if (contact >> k) & 1}
        if cross:
            graph.add(edge(a, b))
    return graph


def check_reduction(c, graph, triangles, cover):
    hubs = {c.n, c.n + 1}
    all_edges = []
    for tri in triangles:
        faces = set(combinations(sorted(tri), 2))
        assert len(faces) == 3 and faces <= graph
        all_edges.extend(faces)
    assert len(all_edges) == len(set(all_edges))
    assert all(e in cover for e in all_edges if hubs.isdisjoint(e))
    assert cover <= graph and len(cover) <= 2 * len(triangles)
    order = 9 if c.n == 5 else 8
    for tri in combinations(range(order), 3):
        if not hubs.isdisjoint(tri):
            faces = set(combinations(tri, 2))
            assert not faces <= graph or faces & cover


def verify_template(c, h, r, cover_mask, p):
    u, v = c.n, c.n + 1
    score, left, right, tip = p
    triangles = [(u, a, b) for a, b in c.decode(left)]
    triangles.extend((v, a, b) for a, b in c.decode(right))
    if tip >= 0:
        triangles.append((u, v, tip))
    assert score == len(triangles)
    cover = c.decode(r) | {edge(u, v)}
    cover |= {edge(k, hub) for k in range(c.n) if (cover_mask >> k) & 1
              for hub in (u, v)}
    if c.n == 5:
        cover |= {edge(u, u + 2), edge(v, v + 2)}
    check_reduction(c, ambient(c, h, 31, 31), triangles, cover)


def named_exceptions(c):
    if c.n == 6:
        return {c.full: "K6"}
    star = {(0, v) for v in range(1, 5)}
    disjoint = {(0, 1), (0, 2), (1, 2), (3, 4)}
    bowtie = star | {(1, 2), (3, 4)}
    return {0: "empty", c.encode(star): "K1,4", c.encode(disjoint): "K3 + K2",
            c.encode(bowtie): "bowtie", c.full: "K5"}


def check_side_links(c, exceptions):
    link = Coordinates(7)
    match = [(m, size(m)) for m, _ in link.matchings()]
    cover_candidates = []
    for q in range(1 << 7):
        if size(q) <= 3:
            avoiding = sum(1 << i for i, ends in enumerate(link.endpoints) if not q & ends)
            cover_candidates.append((size(q), avoiding))
    counts = Counter()
    for h, name in exceptions.items():
        for d in range(32):
            edges = c.decode(h) | {(x, 5) for x in range(5)}
            edges |= {(x, 6) for x in range(5) if (d >> x) & 1}
            le = link.encode(edges)
            if not d:
                assert all(6 not in e for e in edges)
                counts["isolated_private"] += 1
                continue
            match_in_link = [(m, k) for m, k in match if not m & ~le]
            is_wke = any(k >= qsize and not ((le & avoiding) & ~m)
                         for qsize, avoiding in cover_candidates for m, k in match_in_link)
            assert is_wke == (name != "K5")
            counts["connected_WKE" if is_wke else "connected_non_WKE"] += 1
    return dict(counts)


def check_fano(c):
    u, v = c.n, c.n + 1
    triangles = [(u, v, 0), (u, 1, 2), (u, 3, 4), (v, 1, 3), (v, 2, 4),
                 (0, 1, 4), (0, 2, 3)]
    cover = set(combinations(range(5), 2)) | {edge(u, v)}
    if c.n == 6:
        cover |= {edge(5, u), edge(5, v)}
        check_reduction(c, ambient(c, c.full), triangles, cover)
        return 1
    cover |= {edge(u, u + 2), edge(v, v + 2)}
    for da in range(32):
        for db in range(32):
            for cross in (False, True):
                check_reduction(c, ambient(c, c.full, da, db, cross), triangles, cover)
    return 2 * 32 * 32


def census(n):
    c = Coordinates(n)
    labels, orbits = c.orbits()
    vertex_cover = covers(c)
    packed = packing_table(c)
    side_cost = 3 if n == 5 else 1
    exception_names = {labels[h]: name for h, name in named_exceptions(c).items()}
    bad_labels = {}
    labelled_slack, orbit_slack, records = Counter(), Counter(), []
    exception_sizes = {}
    for h, orbit in orbits.items():
        r = h
        best = None
        while True:
            q = vertex_cover[h ^ r]
            slack = 2 * packed[r][0] - side_cost - size(r) - 2 * size(q)
            if best is None or slack > best[0]:
                best = (slack, r, q)
            if r == 0:
                break
            r = (r - 1) & h
        slack, r, q = best
        orbit_slack[slack] += 1
        labelled_slack[slack] += len(orbit)
        records.append([h, len(orbit), slack, r, q, *packed[r]])
        if slack >= 0:
            assert h not in exception_names
            verify_template(c, h, r, q, packed[r])
        else:
            name = exception_names[h]
            bad_labels.update((g, name) for g in orbit)
            exception_sizes[name] = len(orbit)
    assert set(exception_sizes) == set(exception_names.values())
    result = {"core_vertices": n, "labelled_cores": len(labels), "isomorphism_classes": len(orbits),
              "classes_with_literal_template_witness": len(orbits) - len(exception_sizes),
              "failed_template_labelled_counts": exception_sizes,
              "best_slack_labelled_counts": dict(sorted(labelled_slack.items())),
              "best_slack_unlabelled_counts": dict(sorted(orbit_slack.items())),
              "class_records_sha256": sha256(json.dumps(records, separators=(",", ":")).encode()).hexdigest(),
              "complete_core_fano_local_graphs_checked": check_fano(c)}
    if n == 5:
        result["exceptional_side_links"] = check_side_links(c, bad_labels)
    return result


if __name__ == "__main__":
    print(json.dumps([census(5), census(6)], indent=2))
