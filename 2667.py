import sys
from collections import deque
input = sys.stdin.readline


N = int(input())

houses = []
visited = [[False for _ in range(N)] for _ in range(N)]


graph =[[] for _ in range(N)]
for i in range(N):
    line = str(input().strip())
    graph[i] = list(map(int,line))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
##동 서 남 북


def Bfs(x,y):
    count = 0
    q = deque()

    q.append((x,y))
    
    while(q):
        x,y = q.popleft()
        if(visited[x][y] == True):
            continue
        else:
            visited[x][y] = True
            count = count +1

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if(nx<0 or nx>N-1 or ny<0 or ny >N-1):
                continue
            elif(visited[nx][ny] == True):
                continue
            elif(graph[nx][ny] == 0):
                continue
            else:
                q.append((nx,ny))
    return count

counting = 0

for i in range(N):
    for j in range(N):
        if(graph[i][j] == 0):
            continue
        elif(visited[i][j] == True):
            continue
        else:
            counting = Bfs(i,j)
            houses.append(counting)

houses = sorted(houses)


print(len(houses))

for i in range(len(houses)):
    print(houses[i])

