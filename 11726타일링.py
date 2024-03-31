import sys
input = sys.stdin.readline

n = int(input())

d  = [[0,0] for _ in range(1001)]
d[1][1] = 0
d[1][0] = 1
d[2][0] = 1
d[2][1] = 1

for k in range(3,n+1):
    d[k][0] = d[k-1][0]+d[k-1][1]%10007
    d[k][1] = d[k-2][0]+d[k-2][1]%10007


answer = (d[n][0]+d[n][1])%10007
print(answer)



