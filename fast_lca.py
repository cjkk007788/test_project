import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

LOG = 21 ##2의 20승까지  왜 2로할까? ==> 2의 지수배합은 모든 경우의 숫자를 표현할 수 있기 때문이지

n = int(input())
parent = [[0] * LOG for _ in range(n+1)]

d =[0 for _ in range(n+1)] ##depth table
c =[0 for _ in range(n+1)] ## visited Ary

graph = [[] for _ in range(n+1)]


for i in range(n):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x,depth):
    
    d[x] = depth 

    for data in graph[x]:
        if(c[x]==True):
            return
        c[x]=True
        parent[data] = x
        dfs(data,depth+1)

def set_parent(a,b):
    dfs(1,0)

    for i in range(1,LOG): ## 2^0 번 부모들은 이미 dfs에서 초기화
        for j in range(1,n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1] ## 부모테이블 여러개 초기화

def LCA(a,b):

    ##b가 더 깊도록 설정 

    if(d[a]>d[b]):
        a,b = b,a

    for i in range(LOG-1,-1,-1):## 높이 맞추는 과정
        if(d[b]-d[a]>=1<<i):
            b = parent[b][i]##깊은애가 올라가야지 -->이렇게 하면 맞춰지진다.
    if(a==b):
        return b
    
    for i in range(LOG-1,-1,-1):
        if(parent[a][i]!= parent[b][i]): ## 루트노드 이상의 부모는 다 같겠구나. 큰거부터 확인. 이렇게하면 딱 부모전까지 확인한다.
            ##2의 20 승에서 2승까지 확인 -->부모가 다르면 넘어감 부모가 같으면 그만.
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]