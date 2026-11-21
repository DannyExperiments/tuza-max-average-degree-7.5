"""Check the five-neighbor inequality and a concrete cubic component reduction."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")


from collections import Counter
from itertools import combinations, product
from pathlib import Path
import json


def sides(vertices):
    return set(combinations(sorted(vertices),2))


def five_neighbors():
    w = range(5)
    pairs = tuple(combinations(w,2))
    counts = Counter()
    for mask in range(1 << len(pairs)):
        edges = {e for i,e in enumerate(pairs) if mask & (1<<i)}
        if any(sides(t) <= edges for t in combinations(w,3)):
            continue
        alpha = max(n for n in range(6) if any(not (sides(s) & edges) for s in combinations(w,n)))
        bound = 2*len(edges) + 2*max(3,alpha)
        assert bound <= 18
        counts[bound] += 1
    return {'triangle_free_labeled_graphs':sum(counts.values()), 'degree_sum_upper_bounds':dict(sorted(counts.items()))}


def component():
    a = {0,1,2,3}
    left, right = {4,5,6}, {7,8,9}
    b = left | right
    four_cycle = {(0,1),(1,2),(2,3),(0,3)}
    cubic = set(product(sorted(left),sorted(right)))
    edges = four_cycle | cubic | set(product(sorted(a),sorted(b)))
    assert {v for v in a|b if sum(v in e for e in edges)>=8} == a
    assert all(sum(v in e for e in edges)==7 for v in b)
    bought = four_cycle | cubic
    packing = [((i+j)%3,4+i,7+j) for i in range(3) for j in range(3)]
    occupied = [e for t in packing for e in sides(t)]
    assert len(occupied) == len(set(occupied)) == 27 and set(occupied)<=edges
    assert all(b.intersection(e) for e in occupied)
    obligations = [t for t in combinations(sorted(a|b),3) if b.intersection(t) and sides(t)<=edges]
    assert all(sides(t) & bought for t in obligations) and len(bought) <= 2*len(packing)
    return {'degree_eight_vertices':sorted(a),'degree_seven_vertices':sorted(b),'root_triangles':len(obligations),
            'used_triangles':packing,'bought_edges':sorted(bought),'budget_slack':2*len(packing)-len(bought)}


if __name__ == '__main__':
    result = {'five_neighbor_check':five_neighbors(), 'C4_join_K33':component()}
    (Path(__file__).resolve().parent/'TREE_REVIEW.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['five_neighbor_check'], 'example root triangles',result['C4_join_K33']['root_triangles'])
