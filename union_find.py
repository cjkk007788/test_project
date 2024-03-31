def find_parent(parent,x):

    if(parent[x] != x ):
        parent[x] = find_parent(parent,parent[x]) ## 부모노드를 거슬러 올라가야하니 x의 부모를 다시 찾아야함.

    return parent[x]

def union_parent(parent,a,b):
    
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if(a<b):
        parent[a] = b
    else:
        parent[b] = a
    
    


v,e = map(int,input().split()) ## v-->노드의 갯수 , e union연산을 수행할 방법 --> 그래프 빠르게 연결하기 함수
##많은 그래프를 빠르게 연결할 수 있겠구만. union find 드는 노드와 간선을 연결하는게 아님. 같은 집합인지 확인하는 것임. 연결은 직접해줘야함.
##크루스칼 --> 간선을 빼서보기때문에 노드를 순회한다. 간선정보는 직접 입력한다.

cycle = False

parent = [0] * (v+1)

for i in range(v+1):
    parent[i] = i ##일단 부모를 모두 자기자신으로 초기화

for k in range(e): ## 사이클이 발생하는 경우 종료

    a,b = map(int,input()) 
    
    if(find_parent(parent,a) == find_parent(parent,b)):
        cycle = True
        break
    else:
        union_parent(parent,a,b)
   

for j in range(1,v+1):
    find_parent(parent,j)



