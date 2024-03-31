from collections import deque

n,m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):

    queue = deque()
    queue.append((x,y))

    while(queue):
        
        x, y = queue.popleft()##여기 위치 for문안에 넣으면 안된다. for문은 인접행렬에 접근하기 위함이니 기준위치가 계속 바뀌면 안됨
        
        
        for i in range(4):


            nx = x + dx[i]
            ny = y + dy[i]

            if(nx < 0 or nx >=n or ny < 0 or ny >= m ):
                continue
            
            if(graph[nx][ny] == 0):
                continue

            if(graph[nx][ny] == 1):
                graph[nx][ny]  = graph[x][y] +1 
                queue.append((nx,ny))



    return graph[n-1][m-1]


answer = bfs(0,0)

print(answer)