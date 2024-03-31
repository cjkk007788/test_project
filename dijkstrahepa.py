import heapq
import sys

input = sys.stdin.readline()
INF = 1e9

n,m = map(int,input().split())

start = int(input()) ## 시작 위치 입력

graph  =  [[] for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c)) ## 간선비용 저장시에 2-3 3-2 모두 입력해야한다. 간선의 양방향을 표시 2->3 이랑 3->2가 값이 다를 수 있으므로 한번만 입력 x

distance = [INF] * (n+1) ##초기값 무한으로 초기화

def dijkstra(start):
    q=[]

    heapq.heappush(q,(0,start)) ## 우선순위 큐에는 방문할 노드의 순번이 정해진다. 의미있는건 우선순위 큐의 최상단 노드뿐

    while(q):

        dist,now = heapq.heappop()

        if(dist<distance[now]): ##이미 방문한 노드라면 나간다. 뽑혔는데 작다라는 건 이미 뽑혔었다. 
            continue
        
        for k in graph[now]:##방문했으니 인접 노드의 간선비용을 계산해서 distance값들을 최신화 한다.
            distance[k[0]] = min(distance[k[0]],dist+[k[1]]) ##dist -->현재 방문한 노드까지 최단 거리
            heapq.heappush(q,(distance[k[0]],k[1]))
        
