"""Count fan edge sets directly, and test actual ordinary graphs at the exceptional books."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")


from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, permutations
from pathlib import Path
import json
import runpy


HERE=Path(__file__).resolve().parent



def edge(x,y):
    return tuple(sorted((x,y)))


def links(edges):
    N=defaultdict(set)
    for a,b in edges:
        N[a].add(b)
        N[b].add(a)
    return N


def triangle_edges(t):
    return set(combinations(sorted(t),2))


def triangles(edges):
    N=links(edges)
    return sorted((a,b,c) for a,b in sorted(edges) for c in N[a]&N[b] if b<c)


def all_fans(edges):
    """A center and a path on its neighbors specify the chosen seven edges."""
    N=links(edges)
    result=[]
    for center in sorted(N):
        hood=N[center]
        for b in sorted(hood):
            for c in sorted(N[b]&hood):
                for x in (N[b]&hood)-{c}:
                    for z in (N[c]&hood)-{x,b}:
                        if x<z:
                            result.append((center,x,b,c,z))
    return sorted(result)


def marking_counts():
    source=HERE/'data/SEVEN_CENSUS.json'
    verified=runpy.run_path(str(HERE/'fan_domain.py'))
    words,domain,sha=verified['full_domain'](HERE,json.loads(source.read_text()))
    counts=Counter()
    free=[]
    for word in words:
        column_bits=''.join(f'{ord(c)-63:06b}' for c in word[1:])
        E={(i,j) for j in range(7) for i in range(j) if column_bits[j*(j-1)//2+i]=='1'}
        N=links(E)
        fans=all_fans(E)
        # A separate brute path check includes extra chords on the four path vertices.
        brute=[(a,*p) for a in range(7) for p in permutations(N[a],4) if p[0]<p[3]
               and all(edge(u,v) in E for u,v in zip(p,p[1:]))]
        assert sorted(brute)==fans
        wide={v for v in range(7) if len(N[v])>=4}
        for m in range(128):
            high={v for v in range(7) if m & (1<<v)}
            if not wide<=high:
                continue
            n=sum(set(f)<=high for f in fans)
            counts[n]+=1
            if n==0:
                free.append((word,sorted(set(range(7))-high)))
    assert sum(counts.values())==159 and counts[0]==5 and counts[4]==9
    assert all(counts[n]==0 for n in (1,2,3))
    return {'unmarked_domain':domain,'catalogue_sha256':sha,'zero_fan_rows':free,
            'ordinary_fans_per_marking':dict(sorted(counts.items()))}


def solve(faces):
    uses=defaultdict(int)
    for i,t in enumerate(faces):
        for e in triangle_edges(t):
            uses[e]|=1<<i
    conflicts=[uses[a,b]|uses[b,c]|uses[a,c] for a,b,c in faces]
    @lru_cache(None)
    def pack(mask):
        if not mask:
            return ()
        i=(mask & -mask).bit_length()-1
        return max((faces[i],)+pack(mask & ~conflicts[i]),pack(mask & ~(1<<i)),key=len)
    @lru_cache(None)
    def cover(mask):
        if not mask:
            return ()
        i=(mask & -mask).bit_length()-1
        return min(((e,)+cover(mask & ~uses[e]) for e in sorted(triangle_edges(faces[i]))),key=len)
    full=(1<<len(faces))-1
    P,C=pack(full),cover(full)
    used=[e for t in P for e in triangle_edges(t)]
    assert len(used)==len(set(used))==3*len(P)
    assert all(set(C)&triangle_edges(t) for t in faces)
    return P,C


def next_support_check():
    vertices=range(6)
    bit={e:1<<i for i,e in enumerate(combinations(vertices,2))}
    triple_masks={t:sum(bit[e] for e in combinations(t,2)) for t in combinations(vertices,3)}
    types={'cone':['012','023','034','045'],'bent':['012','123','234','345'],
           'paw':['012','013','014','035']}
    catalogue={}
    for name,tris in types.items():
        E={e for t in tris for e in combinations(map(int,t),2)}
        cases=[(name,E)]+([('bent+extreme_edge',E|{(0,5)})] if name=='bent' else [])
        for label,edges in cases:
            for p in permutations(vertices):
                code=sum(bit[tuple(sorted((p[a],p[b])))] for a,b in edges)
                assert catalogue.get(code,label)==label
                catalogue[code]=label
    result=Counter()
    for code in range(1<<15):
        tris=[t for t,m in triple_masks.items() if m&code==m]
        if len(tris)!=4 or len({v for t in tris for v in t})!=6:
            continue
        N={t:{u for u in tris if u!=t and triple_masks[t]&triple_masks[u]} for t in tris}
        count=sum(1 for t in tris for x,z in combinations(N[t],2) if z not in N[x])
        if count==2:
            result[catalogue[code]]+=1
    assert sum(result.values())==len(catalogue)
    return dict(sorted(result.items()))


def attachments(two_bases):
    support=set('abcxz')
    core={edge(*s) for s in ('ax','ab','ac','az','xb','bc','cz')}
    roots=set()
    if two_bases:
        for i,(v,tips) in enumerate((('b','xc'),('c','bz'))):
            y,k,s,t=(f'{v}{i}' for v in 'ykst')
            roots.add(y)
            # Both seven-rims present their own exceptional base, missing only k-a.
            core|={edge(y,p) for p in ['a',v,s,t,k,*tips]}|{edge(s,t)}
            core|={edge(h,q) for h in (*tips,k) for q in ('a',v,s,t)}-{edge('a',k)}
    else:
        for y,vertices in [('m','abc'),('l','ax'),('j','xb'),('p','cz'),('o','za')]:
            roots.add(y)
            core|={edge(y,p) for p in vertices}
    N=links(core)
    owners=[v for v in sorted(N) for _ in range((7 if v in roots else 8)-len(N[v]))]
    left=[f'K{i:02}' for i in range(len(owners))]
    right=[f'R{i}' for i in range(8)]
    E=core|{edge(v,w) for v,w in zip(owners,left)}|{edge(v,w) for v in left for w in right}
    N=links(E)
    high={v for v in N if len(N[v])>=8}
    assert set(N)-high==roots and all(len(N[v])==7 for v in roots)
    A=all_fans({e for e in E if set(e)<=high})
    assert len(A)==1 and A[0][0]=='a' and set(A[0])==support
    F=triangles(E)
    assert F==triangles(core)
    outside={s:sorted((N[s[0]]&N[s[1]])-support) for s in ('ax','ab','ac','az','xb','bc','cz')}
    assert all(outside.values())
    contacts={v:sorted(N[v]&support) for v in roots}
    if two_bases:
        assert set(contacts['y0'])==set('abcx') and set(contacts['y1'])==set('abcz')
        assert max(len(v) for v in contacts.values())==4
        safeU={edge(*s) for s in ('ax','bc')}
        safeV={edge(*s) for s in ('az','bc')}
        assert safeU & safeV=={edge('b','c')}
        for y,M in [('y0',safeU),('y1',safeV)]:
            assert all(tuple(sorted((*e,y))) in F for e in M)
    else:
        assert set(contacts['m'])==set('abc') and max(len(v) for v in contacts.values())==3
    P,C=solve(F)
    return {'vertices':len(N),'edges':len(E),'triangles':len(F),'core_edges':sorted(core),
            'reservoir_left_owners':owners,'high_fans':A,'exterior_tip_sets':outside,
            'nonhigh_contacts':contacts,'packing':P,'cover':C,'nu_tau':(len(P),len(C))}


if __name__=='__main__':
    marked=marking_counts()
    controls={'middle_only':attachments(False),'both_exceptional_bases':attachments(True)}
    check=next_support_check()
    (HERE/'two_fans.json').write_text(json.dumps({'markings':marked,'controls':controls,'two_fan_supports':check},
                                              indent=2,sort_keys=True)+'\n')
    print(marked['zero_fan_rows'], marked['ordinary_fans_per_marking'][4])
    print({name:(row['vertices'],row['edges'],row['triangles'],row['nu_tau']) for name,row in controls.items()})
    print(check)
