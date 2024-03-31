import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())

graph=[[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1,N+1):
    line = list(str(input()).strip())
    graph[i] = list(map(int,line))
    graph[i].insert(0,0)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

##동 서 남 북

def BFS(x,y):

    q= deque()

    q.append((x,y))

    while(q):
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if(nx <1 or nx >N or ny <1 or ny>M):
                continue
            if(graph[nx][ny]!=1):
                continue
            elif(nx == 1 and ny ==1):
                continue ## 2에서 1로 돌아온 경우
            else:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
                if(nx == N and ny ==M):
                    return graph[nx][ny]
                
    return -1
               
print(BFS(1,1))

