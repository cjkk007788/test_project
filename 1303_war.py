import sys
from collections import deque
input = sys.stdin.readline


N,M = map(int,input().split())
visited_W = [[0 for _ in range(100)] for _ in range(100)]
visited_B = [[0 for _ in range(100)] for _ in range(100)]

graph =[[] for _ in range(100)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
##동서남북

for i in range(M):
    line = list(str(input().rstrip('\n')))
    graph.insert(i,line)


def bfs(x,y):
    
    if(visited_B[x][y] == 1 or visited_W[x][y]==1):
        return 0,'B'
    
    else:
        count = 0
        q= deque()
        q.append((x,y))
        
        if(graph[x][y] == 'W'):##흰색인 경우
            color = 'W'
            while(q):
                x,y = q.popleft()
                if(visited_W[x][y]==1):
                    continue
                visited_W[x][y] = 1
                count = count +1
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if(nx < 0 or nx > M-1 or ny<0 or ny> N-1):
                        continue
                    if(graph[nx][ny] == 'B'):
                        continue
                    if(visited_W[nx][ny] ==1):
                        continue
                    else:
                        q.append((nx,ny))
                        
        if(graph[x][y] == 'B'):##흰색인 경우
            color = 'B'
            while(q):
                x,y = q.popleft()
                if(visited_B[x][y]==1):
                    continue
                visited_B[x][y] = 1
                count = count+1
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if(nx < 0 or nx > M-1 or ny<0 or ny> N-1):
                        continue
                    if(graph[nx][ny] == 'W'):
                        continue
                    if(visited_B[nx][ny] ==1):
                        continue
                    else:
                        q.append((nx,ny))
                        
    return count,color
                        
blue = 0
white = 0          

for n in range(M):
    for m in range(N):
        count,color = bfs(n,m)
        if(color == 'B'):
            blue = blue+(count**2)
        else:
            white = white + (count**2)

print(white,blue)

