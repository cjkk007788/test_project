import heapq
import sys
INF = int(1e9)

input = sys.stdin.readline


n,m = map(int,input().split())


start = int(input())


graph = [[] for _ in range(n+1)]


for i in range(m+1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c)) ## a에서 b로가는 비용 c 저장

distance = [INF] * (m+1)

def dijkstra(start):

    distance[start] = 0
    q = []
    
    heapq.heappush(q,(0,start))


    while(q):
        
        dist,now  = heapq.heappop(q)

        if(dist > distance[now]):
            continue
        ##이미 결정된 곳은 그만

        for j in graph[now]:
            end,cost = j
            if(distance[end] > dist + cost):
                distance[end] = distance[now]+ cost
                heapq.heappush(q,(distance[end],end))

    