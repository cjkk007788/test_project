import sys
input = sys.stdin.readline

V,E = map(int,input().split())

edges = []
sum = 0

def find(a):

    if(parent[a]!=a):
        parent[a] = find(parent[a])
    
    return parent[a]

def union(a,b):
    
    a_parent = find(a)
    b_parent = find(b)

    if(a_parent == b_parent): ## 같은 집합이라면 연결 x 
        return False
    else:
        if(a_parent < b_parent):
            parent[b_parent] = a_parent
        else:
            parent[a_parent] = b_parent
        return True



parent = [i for i in range(10001)] ## 일단 자기 자신으로 초기화


for i in range(E):
    start,end,cost = map(int,input().split())
    edges.append((cost,start,end))
    
new_edges = sorted(edges,reverse=True)

cost = 0

while(new_edges):
    cost,start,end = new_edges.pop()
    if(union(start,end)):
        sum = sum+cost
    else:
        continue

print(sum)