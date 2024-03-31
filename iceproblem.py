from collections import deque 
n,m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input() )))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

count = 0
q = deque()


for i in range(n):
    for k in range(m):
        if graph[i][k] ==0 :
            q.append((i,k))
            while(q):
                x,y = q.popleft()
                graph[x][y] = 1
                for j in range(4):
                    nx = x+dx[j]
                    ny = y+dy[j]
                    if(nx <0 or nx>n-1 or ny< 0 or ny > m-1):
                        continue
                    elif(graph[nx][ny] == 1):
                        continue
                    else:
                        q.append((nx,ny))
            count = count +1

print(count)