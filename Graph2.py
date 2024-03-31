class Graph:
    def __init__(self,size):
        self.size = size
        self.graph = [ [0 for _ in range(size)] for _ in range(size) ]

nameAry = ['문별','솔라','휘인','쯔위','선미','화사']
문별, 솔라,휘인,쯔위,선미,화사 = 0,1,2,3,4,5
Gsize = 6
G1 = Graph(Gsize)


def printGraph(G):
    ##맨 위 이름 행 출력
    print("    ",end = ' ')
    for row in range(G.size):
        print(nameAry[row],end = ' ')
    print()
    
    for row in range(G.size):
        print(nameAry[row],end = ' ')
        for col in range(G.size):
            print(" ",end = '')
            print(G.graph[row][col],end = '   ')
        print()
    print()


G1.graph[문별][솔라] = 1
G1.graph[솔라][문별] = 1
G1.graph[문별][휘인] = 1
G1.graph[휘인][문별] = 1
G1.graph[솔라][쯔위] = 1
G1.graph[쯔위][솔라] = 1
G1.graph[휘인][쯔위] = 1
G1.graph[쯔위][휘인] = 1
G1.graph[쯔위][선미] = 1
G1.graph[선미][쯔위] = 1
G1.graph[쯔위][화사] = 1
G1.graph[화사][쯔위] = 1
G1.graph[선미][화사] = 1
G1.graph[화사][선미] = 1


printGraph(G1)


def bfs(G):
    
    ##출발 위치는 배열의 맨 처음 행의 번호 0

    current = 0
    visitedAry = []
    stack = []

    visitedAry.append(0)
    stack.append(0)

    
    while( len(stack) != 0 ): ##현재위치를 확인하는 지점

        next = None ## 다음위치 초기화 (없는 상태)

        for vertex in G.size:
            ##갈 수 있는 간선이 있는지 탐색

            if(G.graph[current][vertex]==1):## 간선이 있으면
                if(vertex in visitedAry ): ##근데 이미 방문한 곳이면
                    pass
                else:
                    ##방문한 곳이 아니면
                    next = vertex ##다음 방문위치 저장
                    break ## 간선 탐색 끝
                
        if( next != None) : ## 방문안한 곳이 존재
            current = next
            visitedAry.append(current)
            stack.append(current)
        else: ## 모두 방문했으면 
            current = stack.pop()

