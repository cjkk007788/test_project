import sys
input = sys.stdin.readline

N = int(input())
M = int(input())


parent = [ i for i in range(101)]

def find(x):

    if(parent[x] != x):
        parent[x] = find(parent[x]) ## 경로압축 기법
        return parent[x]
    else: 
        return x

def union(x,y):    
    
    x_parent = find(x)
    y_parent = find(y)

    if(x_parent == y_parent):
        return
    if(x_parent < y_parent):
        parent[y_parent] = parent[x_parent]
    else:
        parent[y_parent] = parent[x_parent]    
    return


for k in range(M):
    a,b = map(int,input().split())
    union(a,b)

count = 0
check = find(1)

for i in range(2,N+1):
    if(find(i)==check):
        count = count +1

print(count)