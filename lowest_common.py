import sys
sys.setrecursionlimit(int(1e5))
n = int(input())

parent = []*(n+1)##부모 노드의 정보 각각 노드마다 있을테니
d = [0] *(n+1)#각 노드까지의 깊이
c = [0]*(n+1) #각 노드까지의 깊이가 계산되었는지의 여부 visitedAry

graph = [[] for _ in range(n+1)]

for i in range(n-1): ## 트리구조 --> 노드의 개수 -1 = 간선의 개수
    a,b = map(int,input())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(p,depth):##p 현재 노드 depth == > 현재 깊이

    d[p] = depth
    for data in graph[p]:
        if(c[data]==True):
            continue
        else:
            c[data] = True
            parent[data] = p
            dfs(data,depth+1)

def find_parent(a):
    return parent[a]

def LCA(a,b):

    dfs(1,0) ## 루트노드는 1번 노드 (노드 개수를 N+1 개 만들었으니)## 깊이 테이블이 초기화 되었을 것이다.
    
    if(d[a]>d[b]):
        dist = d[a] - d[b]

        for i in range(dist):
            b = find_parent(b)
    else:
        dist = d[b]- d[a]
        parent_a = a
        for i in range(dist):
            a = find_parent(a)

        while(a != b):
            a = find_parent(a)
            b = find_parent(b)
        return a
        


