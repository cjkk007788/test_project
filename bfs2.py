from collections import deque
def bfs(graph,start,visited):

    queue = deque()

    visited[start] = True
    queue.append(start)

    while(queue):

        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                print(i, end = '')
                queue.append(i)
                visited[i] =True
    
