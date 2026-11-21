"""Check both two-root certificates, including actual exterior triangles."""

if not __debug__:
    raise SystemExit("Verification requires Python without -O or -OO.")


from collections import Counter
from itertools import combinations, product
from pathlib import Path
import json


def edge(a,b):
    return tuple(sorted((a,b)))


def sides(face):
    return {edge(a,b) for a,b in combinations(face,2)}


def all_faces(edges):
    adj = {}
    for a,b in edges:
        adj.setdefault(a,set()).add(b)
        adj.setdefault(b,set()).add(a)
    return {(a,b,c) for a,b in edges for c in adj[a] & adj[b] if b<c}


def rim(word):
    bits=''.join(format(ord(i)-63,'06b') for i in word[1:])
    return {(i,j) for j in range(7) for i in range(j) if bits[j*(j-1)//2+i]=='1'}


def project(root,labels):
    return {edge(root,v) for v in labels} | {edge(labels[i],labels[j]) for i,j in rim('FEzvO')}


def verify(cert, edges, faces):
    roots={'y','z'}
    packed=[tuple(sorted(p)) for p in cert['packed']]
    bought={edge(*p) for p in cert['cover']}
    used=[p for f in packed for p in sides(f)]
    assert set(packed)<=faces and len(set(used))==len(used)==15
    assert bought<=edges and len(bought)==10
    assert all(sides(f)&bought for f in faces if roots & set(f))
    assert all(p in bought for p in used if roots.isdisjoint(p))


def finite(first,second):
    cross=[edge(a,b) for a in 'uvc' for b in 'std']
    rejected_by_high_condition=0
    checked=0
    for exchanged in (False,True):
        ny='abczuhv'
        nz='badysht' if exchanged else 'abdysht'
        required=project('y',ny) | project('z',nz)
        preliminary=all_faces(required)
        mandatory_roots={f for f in preliminary if 'y' in f or 'z' in f}
        assert len(mandatory_roots)==23
        for mask in range(512):
            graph=required | {p for i,p in enumerate(cross) if mask & (1<<i)}
            faces=all_faces(graph)
            assert {f for f in faces if 'y' in f or 'z' in f}==mandatory_roots
            verify(first,graph,faces)
            verify(second,graph,faces)
            for c_high,d_high in product((False,True),repeat=2):
                high=set('abhuvst') | ({'c'} if c_high else set()) | ({'d'} if d_high else set())
                high_faces=[f for f in faces if set(f)<=high]
                count=Counter(e for f in high_faces for e in sides(f))
                if any(sum(count[e]>=2 for e in sides(f))>=2 for f in high_faces):
                    rejected_by_high_condition+=1
                checked+=1
    assert checked==4096
    return {'status_and_alignment_and_cross_rows':checked,'topological_rows':1024,
            'marking_rows_already_violating_high_condition':rejected_by_high_condition,
            'root_triangles_in_every_row':23}


def exterior(first,second):
    graph=project('y','abczuhv')|project('z','abdysht')
    graph|={edge('X','c'),edge('X','h'),edge('L','a'),edge('L','s')}
    for i in range(5):
        graph.add(edge('L',f'r{i}'))
    # Identify each intended high vertex with a vertex of its own private K8,8.
    # These triangle-free attachments preserve both complete root neighborhoods.
    make_high=sorted(set('abcdhstuvX')|{f'r{i}' for i in range(5)})
    for v in make_high:
        left=[v]+[f'{v}-l{i}' for i in range(7)]
        right=[f'{v}-r{i}' for i in range(8)]
        graph|={edge(a,b) for a,b in product(left,right)}
    deg=Counter(v for e in graph for v in e)
    high={v for v in deg if deg[v]>=8}
    assert set(deg)-high=={'y','z','L'} and all(deg[v]==7 for v in ('y','z','L'))
    faces=all_faces(graph)
    high_faces=sorted(f for f in faces if set(f)<=high)
    count=Counter(e for f in high_faces for e in sides(f))
    assert all(sum(count[e]>=2 for e in sides(f))<=1 for f in high_faces)
    bought={edge(*p) for p in first['cover']}
    assert tuple(sorted('Xch')) in high_faces and tuple(sorted('Las')) in faces
    assert edge('c','h') in bought and edge('a','s') in bought
    verify(first,graph,faces)
    verify(second,graph,faces)
    return {'vertices':len(deg),'edges':len(graph),'triangles':len(faces),'high_triangles':high_faces,
            'nonhigh_degrees':{v:deg[v] for v in ('y','z','L')},'exterior_bought_high_face':'Xch',
            'exterior_bought_low_face':'Las'}


if __name__=='__main__':
    here=Path(__file__).resolve().parent
    first=json.loads((here/'data/path_pair_1.json').read_text())
    second_template=json.loads((here/'data/path_pair_2.json').read_text())['templates']['st-uv']
    second={'packed':second_template['packing'],'cover':second_template['bought']}
    result={'first':first,'second':second,'finite':finite(first,second),
            'exterior_control':exterior(first,second)}
    (here/'path_pair_check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['finite'])
    print(result['exterior_control'])
