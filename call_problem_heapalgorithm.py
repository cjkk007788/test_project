import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline


X,Y,Z = map(int,input().split()) #도시의 갯수 N , 통로의 갯수 M 시작 위치 Z

graph = [[] for _ in range(X+1)] ## [X,Y,Z] ==>이렇게 저장

for k in range(Y):
    a,b,c = map(int,input().split())    
    graph[a].append((b,c)) ## graph[a]에는 도착위치 (b(도착위치),c(간선 비용))

distance = [INF for _ in range(X+1)]
count = -1
max_time = 0

def dijkstrat(start):
    q = []
    
    heapq.heappush(q,(0,start)) ## 자기자신까지의 거리는 0
    distance[start] = 0

    while(q):
        
        dist,now = heapq.heappop(q)

        if(dist > distance[now]): ##이미 방문했었으면 넘어감
            continue
        ##방문 시작

        for data in graph[now]:##인접 간선 노드 확인
            if(distance[data[0]] > dist + data[1]):
                distance[data[0]] = dist + data[1] ##디스턴스 테이블 최신화
                heapq.heappush(q,(distance[data[0]],data[0]))

dijkstrat(Z)

for data in distance:
    if(data != INF):
        count = count +1
        max_time = max(max_time,data)
print(count,' ',max_time)
