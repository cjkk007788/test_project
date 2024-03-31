from collections import deque


v,e = map(int,input().split())

##노드의 개수, 간선의 개수 입력 받는다

indegree = [0] *(v+1)
graph = [[] for _ in range(v+1)]

for i in range(e):
    a,b = map(int,input())
    graph[a].append(b) ## 간선 a에는 b가연결
    indegree[b] = indegree + 1 #진입차수를 증가시킨다 ==> 알고리즘마다 사용되는 자료구조가 있다. union find --> parent 자료구조


def topology():
    
    result = []
    q = deque()

    for i in range(1, v+1):
        if(indegree[i] == 0 ):
            q.append(graph[i])
            
    while(q): ## q가 빌때까지

        now = q.popleft() ##q에서 꺼낸 순서가 result에 담겨야 한다. --> q에 넣는 순서랑 일치하므러
        result.append(data)

        for data in now: ##now는 노드가 꺼내짐 data는 노드에 연결된 목적 간선의 번호
            indegree[data] = indegree[data]-1
            if(indegree[data] == 0):
                q.append(graph[data])

    for i in result:
        print(i,end='-->')

        
