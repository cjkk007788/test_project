import heapq
import sys

input = sys.stdin.readline()
INF = 1e9

n,m = map(int,input().split())

start = int(input()) ## 시작 위치 입력

graph = [[] for _ in range(n+1)] ## 벌택스의 갯수만큼 입력 받기

distance =[INF] *(n+1)
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append(b,c) ## a에서 b로향하는 간선 비용 == > c
    

def dijkstratheap(start):
    
    q= []

    heapq.heappush(q,(0,start)) ## (그 위치까지의 최단 거리, 시작위치 --> 간선 비용에 따라서 정렬 시작)
    ##heapq의 기본적인 정렬 값은 첫번째 인덱스의 값
    
    while(q):

        dist,now = heapq.heappop(q)

        if(dist > distance[graph[now][1]]):
            continue##우선순이 최고 순위인데 밀린 경우
        
        for data in graph[now]: ##now == > 현재의 간선 위치 --> 연결된 간선을 모두 검사
            if(distance[data[0]] > dist + data[1]):
                distance[data[0]] = dist + data[1]
                heapq.heappush(q,(distance[data[0]],data[0])) ## 그래프의 저장방식과 q의 저장방식이 반대이니 헷갈리지 말자

        
            