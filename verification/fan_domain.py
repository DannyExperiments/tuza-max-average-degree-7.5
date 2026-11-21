"""Reconstruct the complete residual seven-link domain from the catalogue and physical witnesses."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")


from collections import Counter
from hashlib import sha256
from math import factorial
import runpy


def decode(word):
    bits = ''.join(format(ord(c) - 63, '06b') for c in word[1:])
    return {(i,j) for j in range(7) for i in range(j) if bits[j*(j-1)//2+i] == '1'}


def full_domain(progress, bank):
    # Reuse only the already-audited catalogue, WKE and triangle-certificate primitives.
    audit = runpy.run_path(str(progress / 'seven_links.py'))
    catalogue = progress / 'data/graph7.g6'
    seen, residual, verified = set(),set(),set()
    stages = Counter()
    for word in catalogue.read_text().splitlines():
        edges = decode(word)
        assert edges == audit['graph6'](word)
        adjacent = [{b if v == a else a for a,b in edges if a == v or b == v} for v in range(7)]
        canonical, symmetry = audit['canonical'](edges,adjacent)
        assert canonical not in seen
        seen.add(canonical)
        stages['labelled_graphs'] += factorial(7)//symmetry
        reached = {0}
        for _ in range(7):
            reached |= set.union(*(adjacent[v] for v in reached))
        if len(reached) < 7:
            continue
        stages['connected'] += 1
        code = sum(audit['BIT'][edge] for edge in edges)
        if audit['is_wke'](code):
            continue
        stages['connected_non_wke'] += 1
        if word in bank['witnesses']:
            verified.add(word)
            stages['positive_root_triangles'] += audit['verify_cone'](edges,bank['witnesses'][word])
        else:
            residual.add(word)
    assert len(seen) == 1044 and stages['labelled_graphs'] == 2**21
    assert verified == set(bank['witnesses']) and len(verified) == 40
    assert residual == set(bank['unresolved_closed_neighborhoods']) and len(residual) == 77
    return sorted(residual),dict(stages),sha256(catalogue.read_bytes()).hexdigest()
