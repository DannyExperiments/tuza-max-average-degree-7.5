"""Independent literal replay of the mixed degree-nine donor reductions."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")


from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json


HERE = Path(__file__).resolve().parent
BANK = HERE / 'data' / 'MIXED_NINE.json'
V = set(range(10))
H, A, B, C, X, Z, P, Q, R, T = range(10)
OPTIONS = ((C,P),(C,Q),(P,R),(P,T),(Q,R),(Q,T))


def side(u, v):
    return tuple(sorted((u, v)))


def edges(t):
    return set(combinations(sorted(t), 2))


def graph(mask):
    # h,a,b are all adjacent to the other nine vertices in the display.
    universal = {e for e in combinations(sorted(V), 2) if {H,A,B}.intersection(e)}
    base = {(X,P),(X,Q),(C,Z),(Z,R),(Z,T),(C,R),(C,T)}
    return universal | base | {e for i,e in enumerate(OPTIONS) if mask & (1 << i)}


def triangles(g, vertices, roots):
    return [t for t in combinations(sorted(vertices), 3) if roots.intersection(t) and edges(t) <= g]


def check(row):
    mask = row['mask']
    g = graph(mask)
    degree = [sum(v in e for e in g) for v in sorted(V)]
    assert (degree[H], degree[X], degree[Z]) == (9,5,6)
    assert all(degree[v] <= 7 for v in (P,Q,R,T))
    roots = set(row['roots'])
    private = {P,Q,R,T}
    assert roots and roots <= private | {H,X,Z}
    assert len(roots) == len(row['roots'])
    packing = row['packing']
    used = [e for t in packing for e in edges(t)]
    assert packing and all(len(set(t)) == len(t) == 3 for t in packing)
    assert len(used) == len(set(used)) == 3*len(packing)
    assert set(used) <= g
    cover = {side(u,v) for u,v in row['internal']}
    assert len(cover) == len(row['internal']) and cover <= g
    assert {e for e in used if roots.isdisjoint(e)} <= cover
    obligations = triangles(g, V, roots)
    assert all(cover & edges(t) for t in obligations)
    exits = sum(7-degree[v] for v in roots & private)
    assert exits == row['exits']
    budget = 2*len(packing) - len(cover) - exits
    assert budget >= 0
    # Realize arbitrary shared exits in two extremal ways, then permit every
    # outside-to-outside and unbounded-high-to-outside edge in each control.
    exterior_counts = {}
    for shared in (True,False):
        exterior = set()
        purchases = set(cover)
        enlarged = set(g)
        for v in sorted(private):
            for i in range(7-degree[v]):
                new = 10 + (0 if shared else 4*(v-P)) + i
                e = side(v,new)
                enlarged.add(e)
                exterior.add(new)
                if v in roots:
                    purchases.add(e)
        enlarged.update(combinations(sorted(exterior), 2))
        enlarged.update(side(o,k) for o in exterior for k in (A,B,C))
        actual = triangles(enlarged, V | exterior, roots)
        assert len(purchases) == len(cover)+exits
        assert all(purchases & edges(t) for t in actual)
        exterior_counts['shared' if shared else 'disjoint'] = len(actual)-len(obligations)
    return {'mask':mask, 'roots':sorted(roots), 'edges':len(g), 'packing':len(packing),
            'internal_purchases':len(cover), 'exit_purchases':exits, 'budget_slack':budget,
            'internal_root_triangles':len(obligations), 'exterior_root_triangles_in_controls':exterior_counts}


def main():
    raw = BANK.read_bytes()
    data = json.loads(raw)
    assert len(data) == 64 and {r['mask'] for r in data} == set(range(64))
    assert len({frozenset(graph(m)) for m in range(64)}) == 64
    rows = [check(r) for r in sorted(data,key=lambda r:r['mask'])]
    hist = {k:dict(sorted(Counter(r[k] for r in rows).items())) for k in
            ('packing','internal_purchases','exit_purchases','budget_slack')}
    roots = Counter(','.join(map(str,r['roots'])) for r in rows)
    total = {k:sum(r[k] for r in rows) for k in ('packing','internal_purchases','exit_purchases','internal_root_triangles')}
    total['exterior_root_triangles_in_shared_control'] = sum(r['exterior_root_triangles_in_controls']['shared'] for r in rows)
    total['exterior_root_triangles_in_disjoint_control'] = sum(r['exterior_root_triangles_in_controls']['disjoint'] for r in rows)
    result = {'bank_sha256':sha256(raw).hexdigest(), 'labels':'h,a,b,c,x,z,p,q,r,t',
              'optional_edges':OPTIONS, 'totals':total,'histograms':hist,'root_sets':dict(sorted(roots.items())), 'rows':rows}
    (HERE/'MIXED_NINE_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'}))


if __name__ == '__main__':
    main()
