import sys
input = sys.stdin.readline
INF = int(1e9)

N,M = map(int,input())

graph = [[INF for _ in range(N+1) for _ in range(N+1)]]



for i in range(M):
    a,b = map(int, input())
    graph[a][b] = 1
    graph[b][a] = 1

X,K = map(int,input().split())


for i in range(N+1):
    graph[i][i] = 0


for k in range(N+1):
    for a in range(N+1):
        for b in range(N+1):
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])


if(graph[X][K] == INF or graph[K][X] == INF):
    print(-1)
else:
    print(graph[X][K] + graph[K][X])



