import sys
input = sys.stdin.readline


R,C,K = map(int,input().split())
dx = [0,0,1,-1]
dy = [1,-1,0,0]

graph=[]
visited = [[0 for _ in range(C)] for _ in range(R)] ## R X C 행렬 0으로 초기화
answer =0
for i in range(R):
    line = list(str(input().rstrip('\n')))
    graph.append(line)


def dfs(x,y,count):
    global answer

    if(visited[x][y] != 0):
        return ## 방문했던 곳이면 리턴
    else:
        visited[x][y] = 1##방문처리
        if(x == 0 and y == C-1):##도착위치 
            if(count == K):
                answer = answer + 1
                visited[x][y] = 0
                return True
            else:
                visited[x][y] = 0
                return False
        else:##도착위치가 아닌데 이미 K인경우는 탐색 종료
            if(count == K):
                visited[x][y] = 0 ##돌아설때는 방문 안한처리 해주기
                return False
            
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if(nx<0 or nx >R-1 or ny<0 or ny >C-1):##배열 밖으로 나가는 경우는 제거
                continue
            if(visited[nx][ny] == 1):##이미 방문했던 곳은 처리
                continue
            if(graph[nx][ny] =='T'):##T인 경우 Bfs수행하지 않음
                continue
            else:
                dfs(nx,ny,count+1)
        visited[x][y] = 0##for 문이 끝나는 건 백트래킹을 하는 것 -->이때 방문 안한처리를 해주기

dfs(R-1,0,1)


print(answer)