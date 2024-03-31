INF = int(1e9)

n = int(input()) ## 2노드의 갯수
m = int(input()) ## 간선의 갯수

graph = [[INF] * (n+1) for _ in range(n+1)] ##

## graph 구현할때 0번은 안쓴다고 생각하기 0행 0열은 안쓴다. 1번 노드 ~ N번노드 이게 편하지.
for a in range(1,n+1):
    graph[a][a] = 0

for _ in range(m): ##간선값을 저장
    a,b,c = map(int,input().split()) ##단일 간선일 수 있으므로 하나하나씩 입력 ex 1-->2로가는 비용, 2-->1로가는 비용 따로 입력
    graph[a][b] = c


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]== INF:
            print("갈 수 없습니다")
        else:
            print(graph[a][b], end = ' ')
    print()