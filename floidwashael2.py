INF = int(1e9)

n = int(input()) ## 2노드의 갯수
m = int(input()) ## 간선의 갯수

graph = [[INF for _ in range(n+1) for _ in range(n+1)]]


for j in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c ## a--> b로가는 비용 c 추가 ## 자기자신으로 가는것은 입력 안해도 괜찮

for a in range(n+1):
    graph[a][a] = 0 ## 자기자신으로 가는 간선 비용 0 


def floidwashael():
    
    for k in range(n+1):
        for a in range(n+1):
            for b in range(b+1):
                 graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

