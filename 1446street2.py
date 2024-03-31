import sys
import heapq
INF = 10001
input = sys.stdin.readline
N,D = map(int,input().split())

inputs = []

graph = [{} for _ in range(10001)]
nodes = []

for i in range(N):
    start ,end ,cost = map(int,input().split())
    if(end<=D):
        inputs.append([start,end,cost])
        nodes.append(start)
        nodes.append(end)
    else:
        continue

nodes.append(0)
nodes.append(D)
graph[0][D] = D

nodes = list(set(nodes))
nodes = sorted(nodes,reverse=False)


for i in range(len(nodes)-1):
    graph[nodes[i]][nodes[i+1]] = nodes[i+1]-nodes[i]

for i in range(len(inputs)):
    start = inputs[i][0]
    end = inputs[i][1]
    cost = inputs[i][2]
    if (end in graph[start]):
        graph[start][end] = min(graph[start][end], cost)
    else:
        graph[start][end] = cost

distance = [INF] * 10001

def dijkstra(start):
    
    q =[]
    
    heapq.heappush(q,(0,start)) ## 그 위치까지의 비용
    distance[start] = 0

    while(q):
        dist,now = heapq.heappop(q)
        if(dist > distance[now]): ## 이미 갱신 된경우 넘어간다.
            continue
        for target in graph[now]:
            if(distance[target]> dist + graph[now][target]):
                distance[target] = dist + graph[now][target]
                heapq.heappush(q,(distance[target],target))

dijkstra(0)
print(distance[D])