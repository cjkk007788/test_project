import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

graph = [[] for _ in range(1001)]

N,M = map(int,input().split())


for i in range(N-1):
    start,end,cost = map(int,input().split())
    graph[start].append((end,cost))
    graph[end].append((start,cost))
    

def DFS(now,end,cost):

    ##찾으면 종료하는 법
    
    if(now == end):
        answer.append(cost)
        return True
    if(visitedAry[now]):
        return False
    else:
        visitedAry[now] = True
    for data in graph[now]:
        if(visitedAry[data[0]]):
            continue
        else:
            if(DFS(data[0],end,cost+data[1])):
                break
            
answer = []

for k in range(M):
    start, end = map(int,input().split())
    visitedAry = [False]*1001
    DFS(start,end,0)
   

for j in range(M):
    print(answer[j])
