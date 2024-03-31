import sys
input = sys.stdin.readline

N,S,M = map(int,input().split())

v = list(input().split())
v = [ int(i) for i in v]


dp = [[-1 for _ in range(M+1)] for _ in range(N+1)]
dp[0][S] = 1

for i in range(0,N):
    for k in range(0,M+1):
        if(dp[i][k]!=-1):
            if(k+v[i]<=M):
                dp[i+1][k+v[i]] = 1
            if(k-v[i]>=0):
                dp[i+1][k-v[i]] = 1

for j in range(M,-1,-1):
    if(dp[N][j] == 1):
        dp[N][j] = j
print(max(dp[N]))