"""Independent exhaustive census of labelled endpoint links and witness replay."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")

from itertools import combinations, permutations
from pathlib import Path
from collections import Counter
import gzip
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
BANKS = HERE / "data"
tips = tuple(range(2, 6))
left = (6, 7)
right = (8, 9)
def pair(a, b):
    return (min(a, b), max(a, b))

core = tuple(combinations(tips, 2))
def side(spokes):
    return tuple((v, s) for s in spokes for v in tips) + (spokes,)
slots = core + side(left) + side(right)
def chosen(es, mask):
    return {e for i, e in enumerate(es) if (mask >> i) & 1}
fixed = {(0, 1)} | {(u, v) for u in (0, 1) for v in tips} | {(0, a) for a in left} | {(1, b) for b in right}
cross = tuple((a, b) for a in left for b in right)

def good_sides():
    # Each bit of a truth table represents a different graph on one endpoint link.
    # Construct the full WKE truth table from the union of witness subcubes.
    opt = slots[:15]
    other_hub = 1
    vertices = (other_hub,) + tips + left
    base = {(other_hub, c) for c in tips}
    possible = set(opt) | base
    states = 2 ** len(opt)
    all_states = (1 << states) - 1
    columns = []
    for i in range(len(opt)):
        size = 1 << i
        period = (1 << (2 * size)) - 1
        columns.append((all_states // period) * (((1 << size) - 1) << size))
    witness_table = 0
    for k in range(4):
        for match in combinations(possible, k):
            if len({v for e in match for v in e}) != 2 * k:
                continue
            match = set(match)
            required = all_states
            for i, e in enumerate(opt):
                if e in match:
                    required &= columns[i]
            for q in combinations(vertices, k):
                q = set(q)
                if any(e not in match and q.isdisjoint(e) for e in base):
                    continue
                fits = required
                for i, e in enumerate(opt):
                    if e not in match and q.isdisjoint(e):
                        fits &= all_states ^ columns[i]
                witness_table |= fits
    good = [[] for _ in range(64)]
    wke = witness_table.to_bytes(states // 8, 'little')
    for mask in range(states):
        if (wke[mask//8] >> (mask%8)) & 1:
            continue
        graph = base | chosen(opt, mask)
        seen = {other_hub}
        while True:
            grown = seen | {v for e in graph if seen.intersection(e) for v in e}
            if grown == seen:
                break
            seen = grown
        if len(seen) == 7:
            good[mask % 64].append(mask >> 6)
    return good

def tables():
    # An eight-element swap of left/right private labels acts separately on each side.
    core_labels = tuple(combinations(range(4), 2))
    side_labels = tuple((v, a) for a in (4,5) for v in range(4)) + ((4,5),)
    def remap(es, perm):
        bits = [1 << es.index(pair(perm[a],perm[b])) for a,b in es]
        out = [0]
        for value in range(1,1 << len(es)):
            bit = value & -value
            out.append(out[value-bit] | bits[bit.bit_length()-1])
        return out
    result = []
    for cp in permutations(range(4)):
        ctab = remap(core_labels, cp)
        for lp in permutations((4,5)):
            ltab = remap(side_labels, cp + lp)
            for rp in permutations((4,5)):
                rtab = remap(side_labels, cp + rp)
                result.append((ctab,ltab,rtab))
    return result

def domain():
    good=good_sides()
    allowed = {c+(a<<6)+(b<<15) for c, sides in enumerate(good)
               for a in sides for b in sides}
    pending = allowed.copy()
    keys = {}
    perm_tables = tables()
    while pending:
        code=pending.pop()
        c,a,b=code&63,(code>>6)&511,code>>15
        orbit=set()
        for ct,lt,rt in perm_tables:
            x,y=lt[a],rt[b]
            val=ct[c]
            orbit.add(val+(x<<6)+(y<<15))
            orbit.add(val+(y<<6)+(x<<15))
        assert orbit <= allowed
        assert len((orbit-{code}) & pending)==len(orbit)-1
        pending.difference_update(orbit)
        key=min(orbit, key=lambda item: (item & 63, item))
        rim=chosen(slots,key)
        profile=tuple(sorted(n for v in tips if (n:=sum(v in edge for edge in rim))>5))
        keys[key]=(len(orbit),profile)
    assert sum(orbit for orbit,_ in keys.values())==len(allowed)
    return keys, sum(map(len,good))

graph_pairs=tuple(combinations(range(10),2))
bitnum={e:1<<i for i,e in enumerate(graph_pairs)}
def mask_edges(edges):
    return sum(bitnum[pair(*e)] for e in set(tuple(pair(*e)) for e in edges))
def face_bits(triple):
    assert len(set(triple))==3 and len(triple)==3
    return mask_edges(combinations(triple,2))
def verify(rec):
    code = rec["key"]
    assert set(rec["roots"])=={0,1}
    graph=mask_edges(fixed | chosen(slots,code))
    cover=mask_edges(rec["cover"])
    assert cover & graph == cover and bin(cover).count('1')==len(rec["cover"])
    assert bin(cover).count('1')<=2*len(rec["packing"])
    used=0
    for face in rec["packing"]:
        fm=face_bits(face)
        assert fm & graph==fm and not used & fm
        used |= fm
    incident=mask_edges(e for e in graph_pairs if 0 in e or 1 in e)
    assert (used & ~(cover|incident))==0
    # Checking every possible hub triangle in the maximally cross-augmented
    # graph proves hitting on all sixteen subgraphs. Replay each independently.
    for cross_mask in range(16):
        enlarged = graph | cross_bits[cross_mask]
        assert all((tm & enlarged)!=tm or (tm & cover) for tm in hub_faces)

cross_bits=[mask_edges(chosen(cross,c)) for c in range(16)]
hub_faces=[face_bits(t) for t in combinations(range(10),3) if 0 in t or 1 in t]
if __name__=="__main__":
    keys, sided=domain()
    receipt={"good_labelled_one_sided_links":sided,"total_classes":len(keys),
             "total_labelled":sum(x[0] for x in keys.values()),"banks":{}}
    counts=Counter(p for n,p in keys.values())
    receipt["profiles"]={str(k):v for k,v in sorted(counts.items())}
    done=set()
    files=sys.argv[1:] or ["PAIR_ONE_DEFECT.json.gz","PAIR_TRANSFER.json.gz","PAIR_DIRECT.json.gz"]
    for name in files:
        raw=(BANKS/name).read_bytes()
        records=json.loads(gzip.decompress(raw))
        present={r["key"] for r in records}
        assert len(present)==len(records) and present<=keys.keys()
        if "ONE_DEFECT" in name:
            assert present=={k for k,(n,p) in keys.items() if p==(6,)}
        for record in records:
            verify(record)
        receipt["banks"][name]={"orbits":len(present),"labelled":sum(keys[k][0] for k in present),
                                "all_cross_checks":len(present)*16,"sha256":hashlib.sha256(raw).hexdigest()}
        done.update(present)
    missing = sorted(keys.keys() - done)
    receipt["remaining"]={k: {"labelled":keys[k][0], "tip_degrees_away_from_hubs":keys[k][1]} for k in missing}
    receipt["complete_for_at_most_two_defects"] = all(len(keys[k][1]) > 2 for k in missing)
    receipt["complete_for_at_most_three_defects"] = all(len(keys[k][1]) > 3 for k in missing)
    print(json.dumps(receipt,indent=2))
