def dfs(graph,v,visited):
    visited[v] = True ##방문어레이에 넣는다.

    print(v,end = '')

    for i in graph[v]:## 2차원 인접행렬이기때문에 행마다 배열을 갖고 그 배열은 인접한 벌택스임
        if not visited[i]:
            dfs(graph,i,visited)


graph = [
    [], ##0번행은 비워둔다.
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [7],
    [2,6,8],
    [1,7]

]
##2차원 배열

visited = [False] * 9

