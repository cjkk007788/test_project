n,m = map(int,input().split())

INF = 10001

moneys=[]

table = [INF]*(m+1)

table[0] = 0

for i in range(n):
    money = int(input())
    moneys.append(money)


for k in range(1,m+1):
    for data in moneys:
        if(k-data<0):
            continue
        else:
            table[k] = min(table[k],table[k-data]+1)

if(table[m] == INF):
    print(-1)
else:
    print(table[m])

