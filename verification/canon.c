// Read graph6 graphs on m vertices; augment by one vertex in all 2^m ways; canonize each (m+1)-vertex
// graph by an isomorphism-invariant equitable refinement followed by exhaustive search within cells;
// print the distinct canonical graphs (graph6). Graphs whose cell product exceeds LIMIT are printed with
// their own labelling (possible isomorphic duplicates, never a loss of coverage). Counts go to stderr.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#define LIMIT 40320
static int n; static uint16_t adj[16];
static int cellof[16], ncell;
static int order[16]; // vertices sorted by cell
static int cmpsig_n; static int sig[16][17];
static int cmpv(const void*a,const void*b){ int x=*(int*)a,y=*(int*)b; for(int i=0;i<=cmpsig_n;i++){ if(sig[x][i]!=sig[y][i]) return sig[x][i]-sig[y][i]; } return 0; }
static void refine(void){
    for(int v=0;v<n;v++) cellof[v]=__builtin_popcount(adj[v]);
    // compress
    int prev=-1;
    for(;;){
        // signature: old cell, then neighbour counts per cell value (cells indexed by value up to 16)
        int vals[17]; int nv=0; int seen[17]={0};
        for(int v=0;v<n;v++) if(!seen[cellof[v]]){seen[cellof[v]]=1;}
        for(int c=0;c<17;c++) if(seen[c]) vals[nv++]=c;
        cmpsig_n=nv;
        for(int v=0;v<n;v++){ sig[v][0]=cellof[v]; for(int k=0;k<nv;k++){ int c=vals[k],cnt=0; for(int w=0;w<n;w++) if(((adj[v]>>w)&1)&&cellof[w]==c) cnt++; sig[v][k+1]=cnt; } }
        int idx[16]; for(int v=0;v<n;v++) idx[v]=v;
        qsort(idx,n,sizeof(int),cmpv);
        int newc[16]; int c=0; newc[idx[0]]=0;
        for(int i=1;i<n;i++){ if(cmpv(&idx[i-1],&idx[i])!=0) c++; newc[idx[i]]=c; }
        int nc=c+1;
        for(int v=0;v<n;v++) cellof[v]=newc[v];
        for(int i=0;i<n;i++) order[i]=idx[i];
        if(nc==prev){ ncell=nc; break; }
        prev=nc;
    }
}
static uint64_t best; static int pos[16]; static int used[16];
static int cellstart[17], cellsize[17];
static uint64_t codeof(void){ uint64_t c=0; for(int j=1;j<n;j++) for(int i=0;i<j;i++){ c=(c<<1)|((adj[pos[i]]>>pos[j])&1); } return c; }
static void perm(int p){
    if(p==n){ uint64_t c=codeof(); if(c<best) best=c; return; }
    int cell=cellof[order[p]]; // the cell that position p belongs to (positions grouped by cell order)
    for(int i=cellstart[cell]; i<cellstart[cell]+cellsize[cell]; i++){ int v=order[i]; if(used[v]) continue; used[v]=1; pos[p]=v; perm(p+1); used[v]=0; }
}
static uint64_t *store; static size_t ns=0, cap=0; static long long fallback=0;
static void push(uint64_t c){ if(ns==cap){ cap=cap?cap*2:1<<20; store=realloc(store,cap*sizeof(uint64_t)); } store[ns++]=c; }
static int cmpu(const void*a,const void*b){ uint64_t x=*(uint64_t*)a,y=*(uint64_t*)b; return x<y?-1:x>y; }
static void canon(void){
    refine();
    memset(cellsize,0,sizeof cellsize);
    for(int i=0;i<n;i++) cellsize[cellof[order[i]]]++;
    cellstart[0]=0; for(int c=1;c<ncell;c++) cellstart[c]=cellstart[c-1]+cellsize[c-1];
    double prod=1; for(int c=0;c<ncell;c++){ for(int k=2;k<=cellsize[c];k++) prod*=k; }
    if(prod>LIMIT){ for(int i=0;i<n;i++) pos[i]=i; fallback++; push(codeof() | (1ULL<<62)); return; }
    best=~0ULL; memset(used,0,sizeof used); perm(0); push(best);
}
static void out(uint64_t c){
    int fb = (c>>62)&1; c &= ~(1ULL<<62);
    int nbits=n*(n-1)/2; char g6[32]; int k=0; g6[k++]=63+n; int bit=0,val=0;
    for(int t=nbits-1;t>=0;t--){ val=(val<<1)|((c>>t)&1); if(++bit==6){g6[k++]=63+val;bit=0;val=0;} }
    if(bit){ val<<=(6-bit); g6[k++]=63+val; } g6[k]=0; printf("%s\n",g6); (void)fb;
}
int main(void){
    char line[256]; int m=0;
    while(fgets(line,sizeof line,stdin)){
        m=line[0]-63; if(m<1||m>14) continue; n=m+1;
        uint16_t base[16]={0}; int idx=1,val=0,nb=0;
        for(int b=1;b<m;b++) for(int a=0;a<b;a++){ if(nb==0){ val=line[idx++]-63; nb=6; } int x=(val>>(nb-1))&1; nb--; if(x){ base[a]|=1<<b; base[b]|=1<<a; } }
        for(int s=0;s<(1<<m);s++){
            memcpy(adj,base,sizeof base); adj[m]=0;
            for(int a=0;a<m;a++) if((s>>a)&1){ adj[a]|=1<<m; adj[m]|=1<<a; }
            canon();
        }
    }
    qsort(store,ns,sizeof(uint64_t),cmpu);
    size_t u=0; long long ucanon=0, ufb=0;
    for(size_t i=0;i<ns;i++){ if(i==0||store[i]!=store[i-1]){ store[u++]=store[i]; if((store[i]>>62)&1) ufb++; else ucanon++; } }
    for(size_t i=0;i<u;i++) out(store[i]);
    fprintf(stderr,"n=%d generated=%zu distinct=%zu (canonical %lld, uncanonized %lld; fallback events %lld)\n",n,ns,u,ucanon,ufb,fallback);
    return 0;
}
