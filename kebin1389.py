import sys
import heapq
INF = int(1e9)

input  = sys.stdin.readline

N,M = map(int,input().split())

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
distance = [INF] * (N+1)


for i in range(M): ## 친구 관계 입력하는 것
    start,end = map(int,input().split())
    graph[start][end] = 1
    graph[end][start] = 1



def dijkstra(start,graph):
    
    distance2 = [INF] * (N+1)
    q = []
    
    heapq.heappush(q,(0,start)) ## distace 값과 현재 위치

    distance2[start] = 0

    while(q):##q가 빌때 동안
        
        dist,now = heapq.heappop(q)

        if(distance2[now] < dist):
            continue##이미 갱신된 경우 넘어간다.

        for k in range(1,N+1): #그래프 크기 만큼
            if(graph[now][k] == 0):
                continue##연결이 안된 경우는 넘어가기
            else:
                if(distance2[k] > dist + 1):##현재 위치를 거쳐가는게 더짧으면 거리테이블 초기화
                    distance2[k] = dist+ 1
                    heapq.heappush(q,(distance2[k],k))
    
    sum = 0
    for i in range(1,N+1):
        sum = sum + distance2[i]        
    return sum

min_sum = INF
min_index = 0
for k in range(1,N+1):
    dk = dijkstra(k,graph)
    if(min_sum > dk):
        min_index = k
        min_sum = dk


print(min_index)
