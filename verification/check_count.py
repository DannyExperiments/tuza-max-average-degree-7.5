"""Replay the finite inputs and rational comparisons used by COUNT.md."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")


from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import json


HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
C = Q(132, 65)


def replay_archived_inputs():
    path = DATA / 'PAIR_FINAL.json'
    record = json.loads(path.read_text())
    keys = sorted(map(int, record['exceptional_cross_decisions']))
    assert record['unconditional_pair_orbits'] == 3283
    assert keys == [8372190, 8372223, 8388607]
    tips = range(2, 6)
    core_order = list(combinations(tips, 2))
    left = [(t, s) for s in (6, 7) for t in tips] + [(6, 7)]
    right = [(t, s) for s in (8, 9) for t in tips] + [(8, 9)]
    for key in keys:
        graph = {e for i, e in enumerate(core_order + left + right) if key & (1 << i)}
        core_degrees = sorted(sum(t in e for e in graph if max(e) <= 5) for t in tips)
        assert core_degrees in ([2] * 4, [3] * 4)
        assert all((t, s) in graph for s in range(6, 10) for t in tips)
    review = DATA / 'FOUR_HIGH_AUDIT.json'
    atlas = json.loads(review.read_text())['atlas']
    assert atlas['labelled_orbit_sum'] == 2**21
    assert all(atlas['non_WKE_by_large_degrees'][d] == atlas['certified_by_large_degrees'][d] for d in ('3', '4'))
    print('Pair witnesses: 3283 uniform pairs; decoded all three exceptions including every tip/private contact.')
    print('Seven-link receipt: 1044 types, labelled orbit sum 2^21, all 15 low-wide-degree non-WKE types certified.')


def control():
    hubs = ('h', 'a', 'b')
    left = ('p', 's1', 's2')
    right = ('q', 's3', 's4')
    rim = left + right
    exterior = tuple('v' + str(i) for i in range(8))
    edges = set()

    def add(u, v):
        edges.add(tuple(sorted((u, v))))

    for u, v in combinations(hubs, 2):
        add(u, v)
    for h in hubs:
        for t in ('x',) + rim:
            add(h, t)
    for p, q in product(left, right):
        if (p, q) != ('p', 'q'):
            add(p, q)
    for y in ('p', 'q'):
        add('x', y)
    for y in rim:
        add('k', y)
    for u, v in combinations((*exterior, 'k'), 2):
        add(u, v)

    universe = set().union(*edges)
    neighbors = {v: {b for a, b in edges if a == v} | {a for a, b in edges if b == v} for v in universe}
    high = {v for v in universe if len(neighbors[v]) >= 8}
    for h in hubs:
        assert len(neighbors[h]) == 9 and neighbors[h] & high == set(hubs) - {h}
        assert neighbors['x'] | {'x'} <= neighbors[h] | {h}
        assert sum((Q(1, len(neighbors[y] & high)) for y in neighbors[h] - high), Q(1)) == Q(17, 6)
    assert len(neighbors['x']) == 5 and set(hubs) == neighbors['x'] & high
    for y in rim:
        quartet = neighbors[y] & high
        assert len(neighbors[y]) == 7 and quartet == {*hubs, 'k'}
        assert {e for e in edges if set(e) <= quartet} == {tuple(sorted(e)) for e in combinations(hubs, 2)}
    assert (len(universe), len(edges)) == (19, 76)
    print('Actual control: 19 vertices, 76 edges; all three nines attain 17/8 before the quartet test.')


def support_checks():
    # Coordinates 0..7 form the common eight-set, 0..3 are the high vertices.
    eight = frozenset(range(8))
    high = frozenset(range(4))
    fives = [frozenset(s) for s in combinations(eight, 5) if 0 in s and len(high & set(s)) >= 3]
    sixes = [frozenset(s) for s in combinations(eight, 6) if high <= set(s)]
    tests = 0
    for z in sixes:
        eligible = [x for x in fives if x | z == eight]
        for a, b in product(eligible, repeat=2):
            tests += 1
            assert len(a & b) >= 4
    print('Degree-ten eight-set replay:', tests, 'ordered support triples, each contradicted by BFG.')

    # Possible high-subsumer payment sets on a fixed three-element set S.
    S = frozenset(range(3))
    two = [frozenset(s) for s in combinations(S, 2)]
    for z1, z2, z3 in product(two, repeat=3):
        assignments = {0: z1, 1: z2, 2: z3}
        if any(i not in a for i, a in assignments.items()):
            continue
        # A B-type nine pays exactly one six. Distinct projected supports
        # would be distinct sixes. Equal supports could only help consistency.
        assert any(assignments[i] != a for a in assignments.values() for i in a)
    # For two B nines and a candidate (3,5) recipient, each distinct six
    # can spend at most one of the three nines' available six payments.
    for b0, b1 in product(two, repeat=2):
        if 0 not in b0 or 1 not in b1:
            continue
        for recipient_support in [s for s in two + [S] if 2 in s]:
            projected = [b0] if b0 == b1 else [b0, b1]
            # The recipient six differs in ambient high-neighbor count.
            sets = [*projected, recipient_support]
            assert any(sum(i in a for a in sets) >= 2 for i in S)
    print('Three subsumers: three B simultaneous impossible; two B forbid a marginal (3,5) recipient.')


def numerical_table():
    base9 = Q(13, 12)
    signed = [
        ('8 all', Q(2)),
        ('9 one five, j=2, receipt at most 1/15', (Q(38, 15)+Q(1, 15))/Q(4, 3)),
        ('9 one five, j>=3, receipt at most 1/15', (Q(31, 12)+Q(1, 15))/Q(4, 3)),
        ('9 no subsumed five', Q(5, 3)),
        ('9 two clique fives, no receipt', Q(11, 8)),
        ('9 mixed, j>=5, receipt at most 1/15', (Q(25, 12)+Q(1, 15))/base9),
        ('9 mixed (3,4), sends 1/30', (Q(67, 30)-Q(1, 30))/base9),
        ('9 mixed (3,5), receipt at most 1/60', (Q(131, 60)+Q(1, 60))/base9),
        ('9 mixed (4,4), no receipt', Q(11, 5)/base9),
        ('10 two fives, ell<=3, j=3', (Q(35, 12)+Q(2, 15))/Q(5, 3)),
        ('10 two fives, ell<=3, j>=4', (Q(8, 3)+Q(2, 15))/Q(17, 12)),
        ('10 all remaining rows, conservative', Q(34, 21)+Q(1, 5)),
        ('d>=11 j<=2', (Q(14, 3)+Q(1, 15))/Q(10, 3)),
        ('d>=11 j>=3, no subsumed low', Q(18, 13)),
        ('d>=11 j>=3, ell=k+1', (Q(3)+Q(3, 10))/Q(13, 6)),
        ('d>=11 j>=3, ell<=k,f<=k-1', Q(24*4+111, 20*4+25)),
        ('d>=11 j>=3, ell=f=k', (Q(5, 4)+Q(2*4, 5))/(Q(4, 3)+Q(8, 15))),
    ]
    assert max(v for _, v in signed) == C
    assert max(v for name, v in signed if name.startswith('d>=11')) == Q(69, 35) < C
    assert 7+1/C == Q(989, 132)
    assert (Q(17, 6)-Q(1, 20))/Q(4, 3) == Q(167, 80) < Q(137, 65)
    assert 7+Q(65, 137) == Q(1024, 137) and 7+Q(65, 134) == Q(1003, 134)
    print('degree and receipt allowance | upper ratio')
    for name, ratio in signed:
        print(name, '|', ratio)
    print('unmodified mixed table cutoff:', Q(1024, 137))
    print('stronger seven/five transfer without redistributing:', Q(1003, 134))
    print('after redistributing the five counting unit:', Q(989, 132))


if __name__ == '__main__':
    replay_archived_inputs()
    control()
    support_checks()
    numerical_table()
