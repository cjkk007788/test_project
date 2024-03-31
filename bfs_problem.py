N,M = map(int,input().split())

graph = []

def dfs(x,y):

    if(x<0 or x>=N or y<0 or y>=M):
        return False

    if(graph[x][y] == 0):
        graph[x][y] = 1

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x-1,y+1)
        
        return True
    else:
        return False
    

result = 0

for j in range(N):
    for k in range(M):
        if(dfs(j,k)== True):
            result = result+1
