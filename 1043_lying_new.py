import sys
input = sys.stdin.readline

Black_list= list(map(int,input().split()))[1:] ##

def find(parent,a):

    if (parent[a] !=a):
        parent[a] = find(parent,parent[a])
    else:
        return parent[a]
    
def union(parent,a,b,Black_list):
    a = find(parent,a)
    b = find(parent,b)

    if a in Black_list and b in Black_list:
        return
    elif a in Black_list:
        parent[b] = a
    elif b in Black_list:
        parent[a] = b
    else:
        if(a<b):
            parent[b] = a
        else:
            parent[a] = b


n,m = map(int,input().split())
parent = [i for i in range(51)] ## 자기 자신으로 일단 초기화
parties = []

for _ in range(m):
    party_info = list(map(int,input().split())) ## 입력 받기
    party_len = party_info[0]
    party = party_info[1:]

    for i in range(party_len-1):
        union(parent,party[i],party[i+1],Black_list)

    parties.append(party)

ans = 0

for party in parties:
    for i in range(len(party)):
        if find(parent,party[i]) in Black_list:
            break
    else:
        ans = ans+1

print(ans)


