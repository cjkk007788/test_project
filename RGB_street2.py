import sys
input = sys.stdin.readline



N = int(input())

list = []
dp = [[0,0,0] for _ in range(N)]

for i in range(N):
    a,b,c = map(int,input().split())
    list.append([a,b,c])



dp[0][0] = list[0][0]
dp[0][1] = list[0][1]
dp[0][2] = list[0][2]

for i in range(1,N):
    dp[i][0] = list[i][0] + min(dp[i-1][1],dp[i-1][2])
    dp[i][1] = list[i][1] + min(dp[i-1][0],dp[i-1][2])
    dp[i][2] = list[i][2] + min(dp[i-1][0],dp[i-1][1])

print(min(dp[N-1][0],dp[N-1][1],dp[N-1][2]))



