"""Verify the seven-link size filter and replay the pair inputs to the high quartet theorem."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")


from collections import Counter
from functools import lru_cache
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from pathlib import Path
import gzip
import json


HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
V = tuple(range(7))


def module(name,path):
    spec = spec_from_file_location(name,path)
    obj = module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def read(path):
    return json.loads(path.read_bytes())


def edge(i,j):
    return (i,j) if i<j else (j,i)


def graph6(name):
    assert ord(name[0])-63==7
    word = "".join(format(ord(c)-63,"06b") for c in name[1:])
    assert not any(c=="1" for c in word[21:])
    return frozenset((i,j) for j in V for i in range(j) if word[j*(j-1)//2+i]=="1")


def wke(rim):
    @lru_cache(None)
    def max_matching(vertices):
        if not vertices:
            return 0
        first,*other=vertices
        return max([max_matching(tuple(other))]+[
            1+max_matching(tuple(v for v in other if v!=mate))
            for mate in other if edge(first,mate) in rim])
    # For fixed bought spokes Q, every rim edge avoiding Q must be in M.
    for k in range(4):
        for q in combinations(V,k):
            forced=[e for e in rim if set(e).isdisjoint(q)]
            endpoints={v for e in forced for v in e}
            if len(endpoints)==2*len(forced) and (
                    len(forced)+max_matching(tuple(v for v in V if v not in endpoints))>=k):
                return True
    return False


def verify_star(rim, row):
    matching = {edge(*e) for e in row["M"]}
    assert len(matching)==len(row["M"]) and len({v for e in matching for v in e})==2*len(matching)
    pack = [tuple(sorted(t)) for t in row["D"]]+[(*e,7) for e in matching]
    flat = [e for t in pack for e in combinations(t,2)]
    graph = rim | {(v,7) for v in V}
    assert len(flat)==len(set(flat))==3*len(pack) and set(flat)<=graph
    bought = {e for e in flat if 7 not in e} | {(v,7) for v in row["Q"]}
    assert bought<=graph and len(bought)<=2*len(pack)
    assert all({(a,b),(a,7),(b,7)} & bought for a,b in rim)
    return len(rim)


def seven_link():
    reps=DATA/"graph7.g6"
    record=read(DATA/"catalog-verification.json")["7"]
    assert record["sha256"]==sha256(reps.read_bytes()).hexdigest() and record["sum_of_labelled_orbits"]==2**21
    names=reps.read_text().splitlines()
    assert len(set(names))==len(names)==record["representatives"]==1044
    witnesses=read(DATA/"SEVEN_CENSUS.json")["witnesses"]
    necessary,hist,checks=[],Counter(),0
    for n in names:
        rim=graph6(n)
        adjacency=[{b if a==v else a for a,b in rim if v in (a,b)} for v in V]
        component={0}
        for _ in V:
            component|=set().union(*(adjacency[v] for v in component))
        if len(component)<7 or wke(rim):
            assert n not in witnesses
            continue
        large=sum(len(neigh)>=4 for neigh in adjacency)
        hist[large]+=1
        if large<=4:
            necessary.append(n)
            assert n in witnesses
        if n in witnesses:
            checks+=verify_star(rim,witnesses[n])
    archived=read(DATA/"FOUR_HIGH_AUDIT.json")["atlas"]
    assert necessary==archived["necessary_rows"] and hist=={int(k):v for k,v in archived["non_WKE_by_large_degrees"].items()}
    return {"types":len(names),"connected_non_WKE_by_large_spokes":hist,
            "necessary_small_classes":len(necessary),"positive_stars":len(witnesses),
            "root_triangles_checked":checks,"catalogue_sha256":record["sha256"]}


def four_tip():
    # Reuse the independent prior referee's complete 192-symmetry domain and literal positive verifier.
    old=module("prior_pair_referee",HERE/"audit_pairs.py")
    keys,sided=old.domain()
    done=set()
    for filename in ("PAIR_TRANSFER.json.gz","PAIR_DIRECT.json.gz"):
        records=json.loads(gzip.decompress((DATA/filename).read_bytes()))
        for record in records:
            i=record["key"]
            assert i in keys and i not in done
            old.verify(record)
            done.add(i)
    exceptions={}
    for key in sorted(keys.keys()-done):
        edges=old.fixed|old.chosen(old.slots,key)
        core=frozenset(e for e in edges if set(e)<=set(old.tips))
        total=sorted(sum(v in e for e in edges) for v in old.tips)
        clue=sorted(sum(v in e for e in core) for v in old.tips)
        assert min(total)>=8 and clue in ([2]*4,[3]*4)
        assert all(edge(c,p) in edges for c in old.tips for p in old.left+old.right)
        private_edges=[edge(*side) in edges for side in (old.left,old.right)]
        if clue==[2]*4:
            assert private_edges==[False,False]
        # A simple 2-regular graph on four vertices is the induced four-cycle.
        exceptions[key]={"core_degrees":clue,"full_local_tip_degrees":total,
                         "all_private_vertices_see_every_tip":True,"private_pairs_are_edges":private_edges}
    assert set(exceptions)=={8372190,8372223,8388607}
    return {"connected_non_WKE_one_sides":sided,"labeled_full_pairs":sum(v[0] for v in keys.values()),
            "orbits":len(keys),"positive_orbits":len(done),"positive_completions":len(done)*16,
            "unpaid_exceptions":exceptions}


def main():
    gupta=module("gupta_pair_referee",HERE/"check_gupta_56.py")
    larger=[gupta.census(c) for c in (5,6)]
    assert json.loads(json.dumps(larger))==read(DATA/"GUPTA_56_REPLAY.json")
    result={"seven_link":seven_link(),"four_tip":four_tip(),
            "larger_tip_core_counts":[[d["core_vertices"],d["labelled_cores"],d["isomorphism_classes"]] for d in larger]}
    (HERE/"QUARTET_CHECK.json").write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print(json.dumps(result,sort_keys=True))


if __name__=="__main__":
    main()
