from collections import deque

M,N = map(int,input().split())

graph = []
graph2 = []
visited = [[False for _ in range(101)] for _ in range(101)]

for i in range(N):
    line = list(map(int,input()))
    graph.append(line)
    graph2.append(line)

dx = [0,1,-1,0] ## 0 ~ 1 인덱스는 오른쪽 그리고 아래 2~3 위쪽 그리고 왼쪽
dy = [1,0,0,-1]

def BFS(x,y):
    q = deque()
    q.append((x,y))

    while(q):

        x,y = q.popleft()
        
        for i in range(2): 
            nx = x + dx[i]
            ny = y + dy[i]
            if(nx < 0 or nx >N-1 or ny <0 or ny >M-1): ## 범위 넘어간 곳이라면 x
                continue
            if(visited[nx][ny]): ## 이미 처리된 곳이라면 넘기기
                continue
            else:
                visited[nx][ny] = True
                value = 100000
                for k in range(0,4):
                    nx_nx = nx+dx[k]
                    ny_ny = ny+dy[k]
                    if(nx_nx <0 or nx_nx>N-1 or ny_ny<0 or ny_ny>M-1):
                        continue
                    value = min(value,graph[nx_nx][ny_ny])
                graph[nx][ny] = graph[nx][ny] + value

                q.append((nx,ny))


BFS(0,0)

x = 0
y = 0
for i in range(N):
    for k in range(M):
        value = 100000
        for j in range(0,2):
            nx = i + dx[j]
            ny = k + dy[j]
            if(nx < 0 or nx >N-1 or ny<0 or ny>M-1):
                continue
            else:
                value = min(value,graph[nx][ny]) + graph2[i][k]
        graph[i][k] = min(value,graph[i][k])

print(graph[N-1][M-1])