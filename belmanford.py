import sys
input = sys.stdin.readline
INF = int(1e9)

START = 0
END = 1
COST =2


n,m = map(int,input().split()) ## n 노드 , m 간선의 개수

distance = [INF] *(n+1)

edges = []

for i in range(m):
    start,end,cost = map(int,input().split())
    edges.append([start,end,cost])



def belmanford(start): ## 밸만포드 알고리즘은 일단 최단경로를 만들어주면서 동시에 음의 순환이 발생하는지 체크까지 가능하다.

    for i in range(n):
        for k in range(m):
            
            cur = edges[k][START]
            next_node = edges[k][END]
            cost = edges[k][COST]

            if( distance[cur] !=INF and distance[cur] + cost < distance[next_node]):
                distance[next_node] = distance[cur]+cost
                if(i == n-1): ##여기서 갱신이 일어난다면 음의 간선이 존재한다. n-1번째 라운드에서 이미 결정이 난다. 시작노드로부터 구해지고
                    return True
    return False

