"""Exact router, partition and donor checks for both proposed coefficients."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")

from fractions import Fraction as F
from itertools import combinations
import json


def set_partitions(items):
    if not items:
        yield ()
        return
    first, *rest = items
    for tail in set_partitions(rest):
        yield ((first,), *tail)
        for i, part in enumerate(tail):
            yield (*tail[:i], (first, *part), *tail[i+1:])


def incidence_receipt():
    # The first part to test is the one containing the focal mixed nine 0.
    rows = {}
    for name, n, focal_size, choices in (
            ('A from five', 3, 2, {2,3}), ('C from five', 4, 3, {3}),
            ('C from six', 4, 3, {2,3}), ('B from six', 5, 3, {3})):
        all_parts = list(set_partitions(list(range(n))))
        possible = [p for p in all_parts if all(len(b) in choices for b in p)
                    and len(next(b for b in p if 0 in b)) == focal_size]
        assert not possible
        rows[name] = dict(partitions=len(all_parts), compatible=len(possible))
    # Vertices labelled 0,1,2,3 are mixed. Label 4 is the unique outsider.
    triples = list(combinations(range(5),3))
    found = []
    for size in range(len(triples)+1):
        for family in combinations(triples,size):
            if all(sum(v in t for t in family) == 1 for v in range(4)):
                found.append(family)
    assert len(found)==3 and all(sum(4 in t for t in f)==2 for f in found)
    return dict(nonexistent_partitions=rows, B_unique_outsider_families=found)


def ratios():
    old = F(81,40)
    baseline = {
        'limiting': (F(11,5)-F(1,160))/F(13,12),
        'eight': max(1+F(8-j,4)+F(j,160) for j in range(4,9)),
        'nine single five': F(159,80)+F(8,160)/F(4,3),
        'nine mixed j>=5': F(129,65)+F(7,160)/F(13,12),
        'nine others': F(5,3)+F(9,160)/F(2,3),
        'ten delicate': F(168,85)+F(10,160)/F(4,3),
        'ten others': F(191,105)+F(10,160),
        'eleven plus': F(69,35)+F(33,640)}
    assert max(baseline.values())==old
    # Ratios below include the upper receipt per adjacent high. When using
    # an absolute numerator, divide the complete numerator by minimum surplus.
    new = {
        'L': (F(11,5)-F(1,30))/F(13,12),
        'eight': F(2), # high with no subsumed low receives nothing
        'nine, single five, j=2': F(39,20)+F(2,30)/F(4,3),
        'nine, single five, j>=3': max(
            (1+F(9-j,4)+F(3*f3,20)-F(bool(f3),10)+F(j,30))/F(4,3)
            for j in range(3,9) for f3 in (0,1)),
        'nine, mixed j>=5, four or more highs at five': max(
            (1+F(9-j,4)+F(j,30))/F(13,12) for j in range(5,8)),
        'nine, mixed, three plus >=5': (1+F(1,3)+F(1,5)+F(2,5)+F(1,15)+F(5,30))/F(13,12),
        'nine, mixed, three plus four': (1+F(1,3)+F(1,4)+F(2,6)+F(1,15)+F(5,30))/F(13,12),
        'nine other': F(5,3)+F(9,30),
        'ten two fives j=3': F(183,100)+F(3,30)/F(5,3),
        'ten two fives j>=4': max(
            (1+F(10-j,4)+F(3*f3,20)-F(bool(f3),10)+F(j,30))/F(17,12)
            for j in range(4,9) for f3 in (0,1,2)),
        'ten remaining j<=7': F(191,105)+F(7,30)/F(4,3),
        'ten remaining j>=8': (1+F(2,3)+F(2,15)+F(10,30))/F(4,3),
        'd>=11 j<=2': F(71,50)+F(2,30)/F(4,3),
        'd>=11 no low subsumed': F(69,35)}
    assert max(new.values())==2
    # Every residual high-degree gap is affine in k=d-7. A positive value at
    # four and a positive first difference establish strictness at every k>=4.
    gaps = {
        'ell=k+1': lambda k: 2*F(5*k-7,6)-(F(k+8,4)+F(3,10)+F(1,10)),
        'ell<=k, f<=k-1, f3>0': lambda k: F(16*k-61,60),
        'ell<=k, f<=k-1, f3=0': lambda k: F(25*k-76,60),
        'ell=f=k': lambda k: F(16*k-23,60)}
    gaps = {name: {'at_k4':str(gap(4)), 'slope':str(gap(5)-gap(4))}
            for name,gap in gaps.items()}
    assert all(F(row['at_k4'])>0 and F(row['slope'])>0 for row in gaps.values())
    return dict(coefficient_81_over_40={k:str(v) for k,v in baseline.items()},
                coefficient_2={k:str(v) for k,v in new.items()}, high_degree_gaps=gaps,
                final_threshold=str(7+1/F(2)), prior_threshold=str(7+1/old),
                increment_over_989_132=str(F(15,2)-F(989,132)))


if __name__ == '__main__':
    print(json.dumps(dict(incidences=incidence_receipt(), accounting=ratios()),indent=2,sort_keys=True))
