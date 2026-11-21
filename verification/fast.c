// Fast census of triangle-connected tight graphs spanning exactly N vertices, N<=12.
// stdin: graph6 graphs on N-1 vertices; each is augmented by vertex N-1 in all 2^(N-1) ways.
// argv[1] (optional) = k, argv[2] = K : process only input lines with index % K == k (parallel shards).
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
static int N; static uint16_t adj[16], radj[16];
static int eid[16][16], ne; static int tri[300][3]; static uint64_t tmask[300]; static int nt;
static long long cand=0, nuexact=0, tauchecks=0, tight=0;
static int nu_best;
static void nu_rec(uint64_t used, int start, int cur){
    if(cur>nu_best) nu_best=cur;
    if(cur + (ne-__builtin_popcountll(used))/3 <= nu_best) return;
    for(int i=start;i<nt;i++){ if(tmask[i]&used) continue; nu_rec(used|tmask[i], i+1, cur+1); if(cur+1+(ne-__builtin_popcountll(used))/3 <= nu_best) return; }
}
static int greedy_lb(uint64_t hit){ uint64_t u=0; int c=0; for(int i=0;i<nt;i++){ if((tmask[i]&hit)||(tmask[i]&u)) continue; u|=tmask[i]; c++; } return c; }
static int hs(uint64_t hit,int k){ int i; for(i=0;i<nt;i++) if(!(tmask[i]&hit)) break; if(i==nt) return 1; if(k==0) return 0; if(greedy_lb(hit)>k) return 0;
    uint64_t e0=1ULL<<eid[tri[i][0]][tri[i][1]], e1=1ULL<<eid[tri[i][0]][tri[i][2]], e2=1ULL<<eid[tri[i][1]][tri[i][2]];
    return hs(hit|e0,k-1)||hs(hit|e1,k-1)||hs(hit|e2,k-1); }
static int par[64]; static int fnd(int x){ while(par[x]!=x){ par[x]=par[par[x]]; x=par[x]; } return x; }
static void analyse(void){
    int m=N-1; uint16_t nb=adj[m];
    // new vertex must lie in a triangle
    int ok=0; for(int u=0;u<m;u++) if(((nb>>u)&1) && (adj[u]&nb)){ ok=1; break; } if(!ok) return;
    for(int a=0;a<N;a++){ radj[a]=0; }
    for(int a=0;a<N;a++) for(int b=a+1;b<N;b++) if(((adj[a]>>b)&1) && (adj[a]&adj[b])){ radj[a]|=1<<b; radj[b]|=1<<a; }
    for(int a=0;a<N;a++) if(!radj[a]) return;
    ne=0; for(int a=0;a<N;a++) for(int b=a+1;b<N;b++) if((radj[a]>>b)&1){ eid[a][b]=eid[b][a]=ne++; }
    nt=0; for(int a=0;a<N;a++) for(int b=a+1;b<N;b++) if((radj[a]>>b)&1){ uint16_t c=radj[a]&radj[b]&~((1<<(b+1))-1); while(c){ int x=__builtin_ctz(c); c&=c-1;
        tri[nt][0]=a;tri[nt][1]=b;tri[nt][2]=x; tmask[nt]=(1ULL<<eid[a][b])|(1ULL<<eid[a][x])|(1ULL<<eid[b][x]); nt++; } }
    for(int e=0;e<ne;e++) par[e]=e;
    for(int i=0;i<nt;i++){ int x=fnd(eid[tri[i][0]][tri[i][1]]), y=fnd(eid[tri[i][0]][tri[i][2]]), z=fnd(eid[tri[i][1]][tri[i][2]]); par[x]=z; par[fnd(y)]=fnd(z); }
    int r=fnd(0); for(int e=1;e<ne;e++) if(fnd(e)!=r) return;
    cand++;
    // max cut by Gray code (vertex N-1 fixed on side 0)
    uint16_t S=0; int deg[16]; for(int v=0;v<N;v++) deg[v]=__builtin_popcount(radj[v]);
    int cut=0, best=0; uint16_t full=(1<<N)-1;
    for(int i=1;i<(1<<(N-1));i++){ int v=__builtin_ctz(i); int same = __builtin_popcount(radj[v] & (((S>>v)&1)? S : (uint16_t)(~S&full)));
        cut += 2*same - deg[v]; S ^= 1<<v; if(cut>best) best=cut; }
    int ub = ne - best;
    int lb = greedy_lb(0);
    if(ub < 2*lb) return;
    nuexact++; nu_best=lb; nu_rec(0,0,0); int nu=nu_best;
    if(ub < 2*nu) return;
    tauchecks++;
    if(hs(0,2*nu-1)) return;
    tight++;
    char g6[64]; int k=0; g6[k++]=63+N; int bit=0,val=0;
    for(int b=1;b<N;b++) for(int a=0;a<b;a++){ val=(val<<1)|((radj[a]>>b)&1); if(++bit==6){g6[k++]=63+val;bit=0;val=0;} }
    if(bit){ val<<=(6-bit); g6[k++]=63+val; } g6[k]=0; printf("HIT nu=%d %s\n",nu,g6); fflush(stdout);
}
int main(int argc,char**argv){
    int K=1,kk=0; if(argc>2){ kk=atoi(argv[1]); K=atoi(argv[2]); }
    char line[256]; long long ln=0;
    while(fgets(line,sizeof line,stdin)){
        int m=line[0]-63; if(m<1||m>14) continue; if((ln++)%K!=kk) continue; N=m+1;
        uint16_t base[16]={0}; int idx=1,val=0,nbits=0;
        for(int b=1;b<m;b++) for(int a=0;a<b;a++){ if(nbits==0){ val=line[idx++]-63; nbits=6; } int x=(val>>(nbits-1))&1; nbits--; if(x){ base[a]|=1<<b; base[b]|=1<<a; } }
        for(int s=0;s<(1<<m);s++){ memcpy(adj,base,sizeof base); adj[m]=0; for(int a=0;a<m;a++) if((s>>a)&1){ adj[a]|=1<<m; adj[m]|=1<<a; } analyse(); }
    }
    fprintf(stderr,"N=%d shard %d/%d: triangle-connected spanning candidates=%lld exact-nu=%lld tau-checks=%lld tight=%lld\n",N,kk,K,cand,nuexact,tauchecks,tight);
    return 0;
}
