import sys
import bisect
import heapq

N,D = map(int,input().split())
input = sys.stdin.readline
graph = [[] for _ in range(D+1)]
nodes = []
distance = [10000] * 10001

graph[0].append([0,0])
graph[0].append([D,D])
graph[D].append([D,0])
graph[D].append([D,D])

distance[D] = D
distance[0] = 0

nodes.append(0)
nodes.append(D)


for i in range(N):

    start,end,cost = map(int,input().split())    
    graph[start].append([end,cost]) ## 그래프로 연결
    graph[end].append([start,cost]) ## 그래프로 연결 지름길끼리 연결

    if not start in nodes: 
        index_l = bisect.bisect_left(nodes,start)
        left = nodes[index_l]
        right = nodes[index_l+1]
        s_l_cost = start-left
        s_r_cost = right-start
        nodes.insert(index_l,start)
        graph[left].append([start,s_l_cost])
        graph[start].append([left,s_l_cost])
        graph[right].append([start,s_r_cost])
        graph[start].append([right,s_r_cost])        
              
    if not end in nodes:
        index_l = bisect.bisect_left(nodes,end)
        left = nodes[index_l]
        right = nodes[index_l+1]
        s_l_cost = end-left
        s_r_cost = right-end
        nodes.insert(index_l,end)
        graph[left].append([start,s_l_cost])
        graph[start].append([left,s_l_cost])
        graph[right].append([start,s_r_cost])
        graph[start].append([right,s_r_cost])

def dijkstra(start):
    q = []

    heapq.heappush(0,start)

    while(q):
        dist,now = heapq.heappop(q)
        if(dist > distance[graph[now][0]]):
            continue

        for data in graph[now]: ## [연결된 위치, 코스트]
            if distance[data[0]] > dist + data[1]:
                distance[data[0]] = dist + data[1]
                heapq.heappush(q,distance[data[0]],data[0])

dijkstra(0)

print(distance[D])