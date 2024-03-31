def find_parent(parent,x):
    if parent[x] !=x:
        parent[x] = find_parent(parent,parent[x])
    
    return parent[x]


def uniond_parent(parent,a,b):

    a= find_parent(parent,a)
    b= find_parent(parent,b)

    if(a<b):
        parent[a] = b
    else:
        parent[b] = a
    
v,e = map(int,input().split())
## 노드의 개수, 간선의 개수
parent = [0] *(v+1)
edges = []
result = 0

for i in range(v+1): ##자기 자신을 부모로 설정
    parent[i] = i

for k in range(e):##간선정보 입력
    cost,a,b = map(int,input().split()) ##어떻게 연결되어있는지 여기서 정보를 준다. 그래프를 순회하면서 빼면된다다. 간선정보를 뺴면 되겠다. 
    edges.append((cost,a,b))

edges = sorted(edges)

for edge in edges:
    cost,a,b = edge

    if(find_parent(parent,a) == find_parent(parent,b)):
        continue
    else:
        uniond_parent(a,b)
        result = result + cost
    



