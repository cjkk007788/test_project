import sys
input = sys.stdin.readline


n,m = map(int,input().split())
visited = [0] * (n+1)

graph = [[] for _ in range(n+1)]

for i in range(n):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))##a에서 b로가며 비용 c

def Dfs_check_cycle(here):

    if (visited[here]):##이미 방문
        if(visited[here] == -1):
            return True
        else:
            return False ## 이런 경우는 사이클을 생성하지 않은 다른 경우에서 온것이다.
        
    visited[here] = -1 # 아직 방문한적이 없다면 아직 끝나지 않음 표시

    for data in graph[here]:
        end= data[0]
        if Dfs_check_cycle(end):
            return True
    
    visited[here] = 1 ## 끝났음 표시
    return False ## 사이클 없음 표시 check cycle에서 true --> 사이클이 있다. false 는 사이클이 없다.
