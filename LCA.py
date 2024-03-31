import sys
input = sys.stdin.readline
sys.setrecursionlimit((int(1e9)))

LOG = 21
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]


for i in range(m):

    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


parent = [ [0]* LOG for _ in range(n+1) ] ## 각 노드는 부모를 LOG깊이만큼 가질 수 있다.
d = [0] * (n+1)
c= [False] * (n+1)


def dfs(x,depth):

    d[x] = depth
    c[x] = True ## 방문처리

    for data in graph[x]:
        if(c[data] == True):
            continue
        parent[data][0] = x ##1번째 부모 초기화 끝
        dfs(x,depth+1)

def set_parent():
    dfs(1,0)

    for i in range(1,LOG+1): ## 부모노드 초기화
        for j in range(1, n+1):##노드마다 초기화 하는 것 1번 노드 ~ n번 노드까지
            parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(a,b):

    if d[a]> d[b]:
        a,b = b,a
    
    for i in range(LOG-1,-1,-1):
        d[b]-d[a] >= (1<<i) ## 2^i * 1
        b = parent[b][i] ## b 가 더 깊으니 이렇게하면 같아진다. 깊이가 같아진다.

    if a == b:
        return a
    
    for i in range(LOG-1,-1,-1):
        if(parent[a][i] == parent[b][i]):
            continue
        else:
            a= parent[a][i]
            b= parent[b][i]

    return parent[a][0]




            