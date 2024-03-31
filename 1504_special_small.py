import heapq
import sys
input = sys.stdin.readline

INF = 2000000000

graph1 = [[] for _ in range(810)]

N, M = map(int,input().split())
distance1 = [INF] * 810
distance2= [INF] * 810
distance3 = [INF] * 810

def dijkstra(start,graph,distance):

    q = []
    distance[start] = 0
    heapq.heappush(q,(start,0))

    while(q):
        now, dist = heapq.heappop(q)

        if(dist > distance[now]):
            continue
        else:
            for end,cost in graph[now]:
                if(distance[end] > dist + cost):
                    distance[end] = dist + cost
                    heapq.heappush(q,(end,distance[end]))



for i in range(M):
    start,end,cost = map(int,input().split())
    graph1[start].append((end,cost)) ## a에서 b로 가는 비용 c
    graph1[end].append((start,cost)) ## a에서 b로 가는 비용 c

v1,v2 = map(int,input().split())

dijkstra(1,graph1,distance1)
dijkstra(v1,graph1,distance2)
dijkstra(v2,graph1,distance3)

if(distance1[v1] == INF or distance2[v2] == INF or distance3[N] == INF):
    answer = -1

else:
    answer1  = distance1[v1] + distance2[v2] + distance3[N]
    answer2 = distance1[v2] + distance3[v1] + distance2[N]
    answer = min(answer1,answer2)

print(answer)

