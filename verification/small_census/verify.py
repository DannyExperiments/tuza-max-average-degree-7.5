"""Check the persisted physical witnesses directly, using sets of vertex pairs."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")

import gzip
import json
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from xml.etree import ElementTree


HERE = Path(__file__).resolve().parent
INPUT = HERE.parent / 'data' / 'graph8.g6'
PAIRS = tuple((a, b) for b in range(8) for a in range(b))


def edge_set(mask):
    assert 0 <= mask < 2**len(PAIRS)
    return frozenset(e for k, e in enumerate(PAIRS) if mask & (1 << k))


def graph_edges(code):
    assert code[0] == 'G' and len(code) == 6
    bits = ''.join(format(ord(char) - 63, '06b') for char in code[1:])
    assert len(bits) == 30 and bits[-2:] == '00'
    return frozenset(edge for edge, flag in zip(PAIRS, bits) if flag == '1')


def clique(vertices):
    return frozenset(combinations(sorted(vertices), 2))


def verify_figure():
    svg = ElementTree.parse(HERE / 'covers.svg').getroot()
    for typ, cover in [('K4', {'ab', 'cd'}), ('K5', {'ab', 'cd', 'ce', 'de'})]:
        panel = svg.find(f".//*[@id='{typ}']")
        positions = {v.get('data-vertex'): (v.get('cx'), v.get('cy'))
                     for v in panel.findall('.//{*}circle')}
        assert len(positions) == int(typ[1])
        drawn = set()
        for line in panel.findall('.//{*}line'):
            pair = line.get('data-edge')
            assert tuple(positions[v] for v in pair) == tuple(
                (line.get('x'+k), line.get('y'+k)) for k in ('1', '2'))
            assert pair not in drawn
            drawn.add(pair)
        assert drawn == {''.join(pair) for pair in clique(positions)}
        bought = {line.get('data-edge') for line in panel.findall("./{*}g[@class='bought']/{*}line")}
        assert bought == cover
        assert all(any(set(edge) <= set(triangle) for edge in bought)
                   for triangle in combinations(positions, 3))


def main():
    verify_figure()
    summary = json.loads((HERE / 'CHECKS.json').read_text())
    raw = INPUT.read_bytes()
    packed_rows = (HERE / 'certificates.jsonl.gz').read_bytes()
    rows = gzip.decompress(packed_rows)
    assert sha256(raw).hexdigest() == summary['sha256']
    assert sha256(packed_rows).hexdigest() == summary['certificate_gzip_sha256']
    assert sha256(rows).hexdigest() == summary['deterministic_certificate_stream_sha256']
    codes = raw.decode('ascii').splitlines()
    evidence = rows.splitlines()
    assert len(codes) == len(evidence) == len(set(codes)) == 12346
    strict_count = positive_count = edge_count = zero_count = 0
    triples = tuple(clique(v) for v in combinations(range(8), 3))
    for code, row in zip(codes, evidence):
        source_code, blocks = json.loads(row)
        assert source_code == code
        graph = graph_edges(code)
        faces = {triangle for triangle in triples if triangle <= graph}
        old_support = frozenset()
        seen_faces = set()
        literals = []
        strict = False
        for support_mask, pack_masks, cover_mask, typ in blocks:
            support, cover = edge_set(support_mask), edge_set(cover_mask)
            pack = [edge_set(mask) for mask in pack_masks]
            assert not old_support & support and support <= graph
            old_support |= support
            local = {face for face in faces if face <= support}
            assert local and frozenset.union(*local) == support
            assert all(triangle in local for triangle in pack)
            assert all(not (a & b) for a, b in combinations(pack, 2))
            assert cover <= support and all(cover & face for face in local)
            seen_faces.update(local)
            if typ == 'cut':
                assert len(cover) < 2 * len(pack)
                strict_count += 1
                strict = True
                continue
            vertices = {v for edge in support for v in edge}
            assert typ == 'K' + str(len(vertices)) and len(vertices) in (4, 5)
            assert clique(vertices) == support and len(cover) == 2 * len(pack)
            assert len(pack) == len(vertices) - 3
            literals.append((vertices, cover))
        assert seen_faces == faces
        if not strict and not faces:
            zero_count += 1
        if strict or not faces:
            continue
        positive_count += 1
        optimum = sum(len(cover) for _, cover in literals)
        for i, (vertices, _) in enumerate(literals):
            rest = {edge for j, (_, cover) in enumerate(literals) if j != i for edge in cover}
            for target in clique(vertices):
                witness = rest | {target} | clique(vertices.difference(target))
                assert target in witness and witness <= graph and len(witness) == optimum
                assert all(face & witness for face in faces)
                edge_count += 1
    assert (strict_count, zero_count, positive_count, edge_count) == (14088, 410, 142, 1008)
    print(f'{len(evidence):,} graph rows verified, {strict_count:,} strict component witnesses, '
          f'{zero_count} triangle-free graphs, {positive_count} positive tight graphs, '
          f'{edge_count:,} active-edge minimum covers.')


if __name__ == '__main__':
    main()
