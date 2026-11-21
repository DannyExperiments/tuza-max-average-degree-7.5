"""Exhaust the seven-rim around one six without using any seven-link catalogue."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")


from collections import defaultdict
from itertools import combinations
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
V = tuple(range(7))       # tetrahedron 0..3, six 4, optional positions 5,6
PAIRS = tuple(combinations(V,2))
BIT = {e:1 << j for j,e in enumerate(PAIRS)}


def mask(edges):
    return sum(BIT[e] for e in edges)


def local_certificate(rim):
    all_edges = mask(rim)
    tris = []
    for t in combinations(V,3):
        need = mask(combinations(t,2))
        if need & all_edges == need:
            tris.append((t,need))
    matchings = []
    for m in range(3,0,-1):
        for matching in combinations(sorted(rim),m):
            if len({v for e in matching for v in e}) == 2*m:
                matchings.append((m,matching,mask(matching)))
    hit = {n: [(Q,mask(e for e in rim if e[0] in Q or e[1] in Q))
               for k in range(n+1) for Q in combinations(V,k)] for n in range(4)}
    groups = [[] for _ in range(4)]
    for k in range(4):
        for T in combinations(tris,k):
            used = 0
            for _,e in T:
                if e & used:
                    break
                used |= e
            else:
                groups[k].append((tuple(t for t,_ in T),used))
    for m,M,edges_m in matchings:
        for k in range(m+1):
            for T,edges_t in groups[k]:
                if edges_m & edges_t:
                    continue
                reserved = edges_m | edges_t
                for Q,covered in hit[m-k]:
                    if covered | reserved != all_edges:
                        continue
                    packing = [(*e,7) for e in M]+list(T)
                    purchases = [e for e in PAIRS if BIT[e] & reserved]+[(v,7) for v in Q]
                    return packing,purchases
    return None


def check_certificate(rim, data):
    pack,cover = data
    actual = rim | {(v,7) for v in V}
    used = [e for t in pack for e in combinations(sorted(t),2)]
    assert len(set(used))==len(used)==3*len(pack)
    assert set(used)|set(cover) <= actual
    assert {e for e in used if 7 not in e} <= set(cover)
    assert all(set(combinations((*e,7),2)) & set(cover) for e in rim)
    assert len(cover) <= 2*len(pack)


def construct(X,Y,rs):
    edges = set(combinations(range(5),2))
    edges.update((v,5) for v in X)
    edges.update((v,6) for v in Y)
    if rs:
        edges.add((5,6))
    return edges


def six_and_seven_component():
    # Tetrahedron 0..3 joined to K3,3 on (4,5,6),(7,8,9), with edge 4-7
    # subdivided by 10. Its six degree-seven vertices and one six see this Q alone.
    corners = set(range(4))
    component = set(range(4,11))
    internal = set(combinations(range(4),2))
    colors = {(u,v):(u-4+v-7)%3 for u in range(4,7) for v in range(7,10)}
    del colors[4,7]
    colors[4,10] = 0
    colors[7,10] = 3
    E = internal | set(colors) | {(a,b) for a in corners for b in component}
    N = {v:{w for w in range(11) if tuple(sorted((v,w))) in E} for v in range(11)}
    assert {v for v in N if len(N[v])>=8}==corners
    assert [len(N[v]) for v in range(4,11)]==[7]*6+[6]
    assert N[10]==corners|{4,7} and 7 not in N[4]
    T = {t for t in combinations(range(11),3) if set(combinations(t,2))<=E}
    P = [(color,u,v) for (u,v),color in sorted(colors.items())]+[(0,1,2)]
    C = set(colors)|internal
    used = [e for t in P for e in combinations(t,2)]
    assert set(P)<=T and len(used)==len(set(used))==3*len(P)
    assert {e for e in used if not component.intersection(e)}<=C
    assert all(C & set(combinations(t,2)) for t in T)
    assert len(C)<=2*len(P)
    return {"edges":sorted(E),"triangles":len(T),"packing":P,"cover":sorted(C)}


def verify():
    groups = defaultdict(list)
    corners = tuple(range(4))
    for rs in (False,True):
        subsets = [set(X) for k in range(4) if 2<=k+int(rs)<=3 for X in combinations(corners,k)]
        for X in subsets:
            for Y in subsets:
                key = (int(rs),*sorted([len(X),len(Y)]),len(X & Y))
                groups[key].append((X,Y))
    rows = []
    survivors = []
    for key,instances in sorted(groups.items()):
        rs = bool(key[0])
        X,Y = instances[0]
        representative = construct(X,Y,rs)
        certificate = local_certificate(representative)
        if certificate:
            check_certificate(representative,certificate)
        else:
            survivors.append(key)
        # Build an explicit isomorphism for every labeled member.  The four membership
        # classes on Q determine all incidences, allowing the two other slots to swap.
        for XX,YY in instances:
            swaps = len(X)!=len(XX)
            left,right = (YY,XX) if swaps else (XX,YY)
            mapping = {4:4,5:6 if swaps else 5,6:5 if swaps else 6,7:7}
            for inside_x in (False,True):
                for inside_y in (False,True):
                    src = [v for v in corners if (v in X)==inside_x and (v in Y)==inside_y]
                    dst = [v for v in corners if (v in left)==inside_x and (v in right)==inside_y]
                    assert len(src)==len(dst)
                    mapping.update(zip(src,dst))
            convert = lambda t: tuple(sorted(mapping[v] for v in t))
            actual = construct(XX,YY,rs)
            assert {convert(e) for e in representative}==actual
            if certificate:
                check_certificate(actual,tuple([convert(t) for t in C] for C in certificate))
        rows.append({"rs_and_sizes_and_overlap":key,"representative_X":sorted(X),"representative_Y":sorted(Y),
                     "multiplicity":len(instances),"certificate":certificate})
    assert survivors==[(1,2,2,0)]
    return {"rows":rows,"orbits":len(rows),"labeled":sum(len(x) for x in groups.values()),
            "certified_labeled":sum(len(v) for k,v in groups.items() if k not in survivors),
            "survivors":survivors,"mixed_actual_control":six_and_seven_component()}


if __name__ == "__main__":
    result=verify()
    (HERE/"FAN_LINK.json").write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print({k:v for k,v in result.items() if k not in {"rows","mixed_actual_control"}})
    control=result["mixed_actual_control"]
    print(len(control["edges"]),control["triangles"],len(control["packing"]),len(control["cover"]))
