import heapq

INF = 100000

M,N = map(int,input().split()) 

distance = [ [INF for _ in range(100)] for _ in range(100)] ## 무한으로 모두 초기화
graph = []
for i in range(N):
    line = list(map(int,input()))
    graph.append(line)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dijkstra(x,y):
    
    q = []
    distance[x][y] = 0
    heapq.heappush(q,(0,x,y))
    
    while(q):
        dist, x , y = heapq.heappop(q)
        if(dist > distance[x][y]): ## 이미 갱신
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(nx < 0 or nx > N-1 or ny < 0 or ny > M-1):
                continue
            else:
                if(distance[nx][ny] > dist + graph[nx][ny]):
                    distance[nx][ny] = dist + graph[nx][ny]
                    heapq.heappush(q,(distance[nx][ny],nx,ny))

dijkstra(0,0)
print(distance[N-1][M-1])