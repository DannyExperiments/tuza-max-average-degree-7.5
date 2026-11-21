"""Independently price every subset of five neighbors of degree at most seven."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")


from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

from eight_link import ALL, RIM, ROOT, check_boundary, check_optimal, graph_data, internal_requirements, literal_packing, parts


HERE = Path(__file__).resolve().parent
DATA = HERE / "data"


def main():
    stars_file, cuts_file = DATA/"STAR_ATLAS.json", DATA/"MARKED_CUT.json"
    stars = json.loads(stars_file.read_bytes())["surviving"]
    source = json.loads(cuts_file.read_bytes())
    proposed_file = DATA/"MIXED_LOW.json"
    proposed = json.loads(proposed_file.read_bytes())
    assert set(stars) == source.keys() == proposed.keys() and len(stars) == 203
    counts, all_margins, real_margins, chosen_sizes = (Counter() for _ in range(4))
    tight = {}
    optimality = Counter()
    for name in stars:
        rim, cone, faces, exits_at_eight = graph_data(name)
        exits = {z: exits_at_eight[z] - 1 for z in RIM}
        packing = source[name]["packing"]
        literal_packing(cone, packing)
        optimality[check_optimal(cone, faces, packing)] += 1
        budget = 2*len(packing)
        costs, purchases = {}, {}
        for size in range(6):
            for subset in combinations(RIM, size):
                chosen = {ROOT, *subset}
                rest = set(ALL) - chosen
                inside = {e for e in cone if set(e) <= chosen or set(e) <= rest}
                cost = len(inside) + sum(exits[z] for z in subset)
                assert cost == 7*size + 2*sum(set(e)<=rest for e in rim) - len(rim)
                costs[subset], purchases[subset] = cost, inside
        rows = {tuple(row["marks"]):row for row in proposed[name]}
        assert len(proposed[name]) == 56 and rows.keys() == set(combinations(RIM,5))
        for marked in combinations(RIM, 5):
            row = rows[marked]
            choices = parts(marked)
            counts["five_marked_placements"] += 1
            counts["subset_evaluations"] += len(choices)
            selected = min(choices, key=lambda s: (costs[s], len(s), s))
            margin = budget - costs[selected]
            all_margins[margin] += 1
            assert margin >= 0
            if any(exits[z] < 0 for z in marked):
                assert row["overdegree"] in marked and exits[row["overdegree"]] < 0
                counts["impossible_mark_of_internal_degree_eight"] += 1
                continue
            assert tuple(row["chosen"]) == selected and row["bound"] == costs[selected]
            counts["locally_degree_feasible"] += 1
            real_margins[margin] += 1
            chosen_sizes[len(selected)] += 1
            if margin == 0:
                tight.setdefault(name,[]).append("".join(map(str,marked)))
            outside = sum(exits[z] for z in selected)
            counts["purchased_exits_at_degree_seven"] += outside
            counts["internal_rooted_faces"] += internal_requirements(
                cone, faces, selected, packing, purchases[selected], outside)
            counts["exterior_faces_in_stress_graphs"] += check_boundary(rim, marked, selected, exits)
    assert sum(real_margins.values()) + counts["impossible_mark_of_internal_degree_eight"] == len(stars)*56
    result = {"counts":counts, "all_formal_budget_margins":all_margins,
              "degree_feasible_budget_margins":real_margins, "selected_sizes_among_feasible":chosen_sizes,
              "tight_feasible_markings":tight, "packing_optimality_proofs":optimality,
              "five_marked_table_sha256":sha256(proposed_file.read_bytes()).hexdigest(),
              "star_bank_sha256":sha256(stars_file.read_bytes()).hexdigest(),
              "cone_packing_sha256":sha256(cuts_file.read_bytes()).hexdigest()}
    (HERE/"MIXED_LOW_AUDIT.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k != "tight_feasible_markings"},sort_keys=True))


if __name__ == "__main__":
    main()
