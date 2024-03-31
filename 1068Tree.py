import sys
input = sys.stdin.readline

N = int(input())
nodelist = list(map(int,input().split()))
delnode = int(input())

visitedAry = [False] * 51
graph = [[] for _ in range(51)]

for k in range(N):
    parent = nodelist[k]
    if(parent == -1):
        root = k
        continue
    else:
        graph[parent].append(k)

graph[delnode] = []

for g in graph:
    if delnode in g:
        g.remove(delnode)

def dfs(root,count):

    if(visitedAry[root]):
        return count
    else:
        visitedAry[root] = True

    if(len(graph[root]) == 0):
        count = count + 1
    else:
        for data in graph[root]:
            count = dfs(data,count)

    return count
if(delnode == root):
    print(0)
else:
    answer = dfs(root,0)
    print(answer)
