import sys
input = sys.stdin.readline
INF = int(1e9)

def get_smallest_node():

    minvalue = INF
    index = 0 ##인덱스는 걍 초기화

    for i in range(1, n+1):
        if(not visitedAry[i] and distance[i] < minvalue):
            index = i
   
    return index

def dijkstra(start):

    visitedAry[start] = True
    distance[start] = 0 ##시작위치이므로

    for j in graph[start]:##첫노드는 걍 시작
        distance[j[0]] = j[1] ##시작위치에서 연결된 거리값을 갱신
    
    for k in range(n-1):##마지막 노드는 할필요 없으니 시작노드 제외하고 n-1
        now = get_smallest_node()
        visitedAry[now] = True

        for j in graph[now]:
            distance[j[0]] = min(distance[j[0]],distance[now] + j[1]) ##그래프 갱신

        


n,m = map(int(),input().split) ## n은 노드의 개수 / m 은 간선의 개수


graph = [[] for _ in range(n+1)]
visitedAry = [False for _ in range(n+1)]
distance = [1e9 for _ in range(n+1)]
start = int(input("시작노드 입력하세요==> ")) ##


print("graph 정보를 입력하세요--> 노드 / 연결된 노드 / 간선 비용")
for i in range(m): ## 간선 정보 저장
    
    a,b,c = map(int(), input().split()) ##중복입력은 하지 않는다. 딱 간선 개수만큼 입력한다.
    ## 중복입력은 필요없다!
 

dijkstra(start)


for i in range(1, n+1):

    if(distance[i] != 1e9):
        print(distance[i])
    else:
        print("갈 수 없음")



    
        

    