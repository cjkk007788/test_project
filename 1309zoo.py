import sys
input =sys.stdin.readline


N = int(input())


dp = [ [0,0,0] for _ in range(N+1)]

dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1

for k in range(2,N+1):
    dp[k][0] = (dp[k-1][0]+ dp[k-1][1] + dp[k-1][2])%9901
    dp[k][1] = (dp[k-1][0] + dp[k-1][2])%9901
    dp[k][2] = (dp[k-1][0] + dp[k-1][1])%9901


print((dp[N][0] + dp[N][1] + dp[N][2])%9901)


