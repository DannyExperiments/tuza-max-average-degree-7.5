"""Certificate census for the active-edge condition in the ordinary eight-vertex graph6.

Uses Python 3.9+ and the included graph6 catalogue.
"""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")

from collections import Counter
from hashlib import sha256
from itertools import combinations, permutations, product
from math import factorial
from operator import or_
from functools import reduce
from pathlib import Path
import gzip
import json


HERE = Path(__file__).resolve().parent
CATALOG = HERE.parent / 'data' / 'graph8.g6'
ORDER = 8
EDGES = [(a, b) for b in range(ORDER) for a in range(b)]
EDGE_BITS = {edge: 1 << k for k, edge in enumerate(EDGES)}

def pop(x):
    return bin(x).count('1')


def edge(a, b):
    return EDGE_BITS[tuple(sorted((a, b)))]


def clique_mask(vertices):
    return sum(edge(a, b) for a, b in combinations(vertices, 2))


TRIPLES = list(combinations(range(ORDER), 3))
FACES = [clique_mask(t) for t in TRIPLES]
ALL_CUT_COVERS = [sum(1 << k for k, (a, b) in enumerate(EDGES) if ((side >> a) & 1) == ((side >> b) & 1))
                  for side in range(1 << (ORDER - 1))]


def parse_graph6(line):
    assert line[0] - 63 == ORDER and len(line) == 6
    raw = 0
    available = 0
    for c in line[1:]:
        assert 63 <= c <= 126
        raw = (raw << 6) | (c - 63)
        available += 6
    padding = available - len(EDGES)
    assert raw & ((1 << padding) - 1) == 0
    return sum(1 << k for k in range(len(EDGES)) if raw & (1 << (available - 1 - k)))


def adjacency(g):
    neighbors = [0] * ORDER
    for k, (a, b) in enumerate(EDGES):
        if g & (1 << k):
            neighbors[a] |= 1 << b
            neighbors[b] |= 1 << a
    return neighbors


def certify_orbit(neighbors):
    # Initial vertex colours use both degree and the number of triangles at that vertex.
    keys = [(pop(row), sum(pop(row & neighbors[w]) for w in range(ORDER) if row & (1 << w)) // 2)
            for row in neighbors]
    while True:
        cells = {v:i for i, v in enumerate(sorted(set(keys)))}
        colors = [cells[k] for k in keys]
        refined = [(colors[v], tuple(sum(1 for w in range(ORDER)
                                          if colors[w] == j and neighbors[v] & (1 << w))
                                     for j in range(len(cells)))) for v in range(ORDER)]
        if len(set(refined)) == len(cells):
            break
        keys = refined
    classes = [[v for v in range(ORDER) if colors[v] == j] for j in range(len(cells))]
    best, multiplicity = None, 0
    for blocks in product(*(permutations(c) for c in classes)):
        order = tuple(v for block in blocks for v in block)
        code = sum(1 << k for k, (i, j) in enumerate(EDGES) if neighbors[order[i]] & (1 << order[j]))
        if best is None or code < best:
            best, multiplicity = code, 1
        elif code == best:
            multiplicity += 1
    assert factorial(ORDER) % multiplicity == 0
    return best, factorial(ORDER) // multiplicity


def components(faces):
    rest = list(faces)
    result = []
    while rest:
        cluster = [rest.pop()]
        support = cluster[0]
        i = 0
        while i < len(cluster):
            touching = [f for f in rest if f & cluster[i]]
            rest = [f for f in rest if not f & cluster[i]]
            cluster.extend(touching)
            support |= reduce(or_, touching, 0)
            i += 1
        result.append((support, tuple(sorted(cluster))))
    return sorted(result)


def greedy_pack(family):
    faces = list(family)
    pack = []
    while faces:
        f = min(faces, key=lambda t: sum(bool(t & s) for s in faces))
        pack.append(f)
        faces = [s for s in faces if not s & f]
    return tuple(pack)


def strict_certificate(support, faces):
    pack = greedy_pack(faces)
    cover = min((support & mask for mask in ALL_CUT_COVERS), key=pop)
    if pop(cover) >= 2 * len(pack):
        raise RuntimeError('No strict certificate for this component: ' + hex(support))
    return pack, cover, 'cut'


def literal_component(vertices, faces):
    # Provide a minimum cover for each specified active edge and one local maximum packing.
    a,b,c,d = vertices[:4]
    if len(vertices) == 4:
        pack = (clique_mask((a,b,c)),)
    else:
        e = vertices[4]
        pack = (clique_mask((a,b,c)), clique_mask((a,d,e)))
    witnesses = {}
    for a,b in combinations(vertices, 2):
        others = [v for v in vertices if v not in (a,b)]
        target = edge(a,b)
        cover = target | clique_mask(others)
        assert target & cover and pop(cover) == 2 * len(pack) and all(f & cover for f in faces)
        witnesses[target] = cover
    return pack, witnesses


def classify(g):
    faces = tuple(f for f in FACES if f & g == f)
    blocks = components(faces)
    local = []
    cliques = []
    strict = []
    for support, fam in blocks:
        verts = sorted({v for k,(a,b) in enumerate(EDGES) if support & (1 << k) for v in (a,b)})
        if len(verts) in (4,5) and support == clique_mask(verts):
            pack, witnesses = literal_component(verts, fam)
            cover = next(iter(witnesses.values()))
            cliques.append((len(verts), witnesses))
            kind = 'K' + str(len(verts))
        else:
            pack, cover, kind = strict_certificate(support, fam)
            strict.append(kind)
        assert all(f in fam for f in pack) and all(not (a & b) for a, b in combinations(pack, 2))
        assert cover & ~support == 0 and all(cover & f for f in fam)
        assert pop(cover) == 2*len(pack) if kind in ('K4','K5') else pop(cover) < 2*len(pack)
        local.append((support, list(pack), cover, kind))
    if not strict:
        for i, (_, witnesses) in enumerate(cliques):
            combined_fixed = reduce(or_, (v[2] for j, v in enumerate(local) if j != i), 0)
            for target, cover in witnesses.items():
                witness = cover | combined_fixed
                assert witness & target and all(witness & f for f in faces)
                assert pop(witness) == sum(2*len(v[1]) for v in local)
    return local, strict, sorted(k for k, _ in cliques)


def main():
    raw = CATALOG.read_bytes()
    lines = raw.splitlines()
    assert len(lines) == len(set(lines)) == 12346
    by_order = {n: Counter() for n in range(1, ORDER+1)}
    types = {n: Counter() for n in by_order}
    by_nu = {n: Counter() for n in by_order}
    orbit_sum, codes = 0, set()
    strategies = Counter()
    witness_digest = sha256()
    records = []
    for line in lines:
        g = parse_graph6(line)
        nbrs = adjacency(g)
        canonical, orbit = certify_orbit(nbrs)
        assert canonical not in codes
        codes.add(canonical)
        orbit_sum += orbit
        active_order = sum(bool(row) for row in nbrs)
        local, strict, cliques = classify(g)
        strategies.update(strict)
        triangle_support = reduce(or_, (v[0] for v in local), 0)
        record = [line.decode('ascii'), local]
        data = (json.dumps(record, separators=(',', ':')) + '\n').encode('ascii')
        records.append(data)
        witness_digest.update(data)
        for n in range(max(1,active_order), ORDER+1):
            row = by_order[n]
            row['graphs'] += 1
            if not strict:
                row['tight_including_zero'] += 1
                if not local:
                    row['triangle_free'] += 1
                    continue
                row['nonvacuous_tight'] += 1
                row['active_edge_instances'] += pop(triangle_support)
                row['eligible_edge_instances'] += pop(triangle_support)
                row['inactive_edge_instances_in_positive_tight_graphs'] += pop(g & ~triangle_support)
                types[n]['+'.join('K'+str(k) for k in cliques)] += 1
                by_nu[n][sum(len(v[1]) for v in local)] += 1
    assert orbit_sum == 1 << len(EDGES) and len(codes) == 12346
    assert [by_order[n]['graphs'] for n in by_order] == [1,2,4,11,34,156,1044,12346]
    evidence_path = HERE/'certificates.jsonl.gz'
    with evidence_path.open('wb') as file:
        with gzip.GzipFile(filename='', mode='wb', mtime=0, fileobj=file) as compressed:
            compressed.writelines(records)
    assert gzip.decompress(evidence_path.read_bytes()) == b''.join(records)
    result = {'catalog': str(CATALOG.name), 'sha256': sha256(raw).hexdigest(),
              'catalog_order': ORDER, 'nonisomorphic':len(codes),'labelled_orbit_sum':orbit_sum,
              'through_seven_positive':sum(by_order[n]['nonvacuous_tight'] for n in range(1,8)),
              'by_exact_order':{n:{**by_order[n],'support_type':types[n], 'positive_by_nu':by_nu[n]} for n in by_order},
              'strict_component_witness_methods_order_eight':strategies,
              'certificate_rows':len(records),
              'certificate_gzip_sha256':sha256(evidence_path.read_bytes()).hexdigest(),
              'deterministic_certificate_stream_sha256':witness_digest.hexdigest()}
    output = json.dumps(result, indent=2) + '\n'
    (HERE/'CHECKS.json').write_text(output)
    print(output, end='')


if __name__ == '__main__':
    main()
