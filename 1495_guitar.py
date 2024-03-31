import sys
input = sys.stdin.readline

N,S,M = map(int,input().split())

v = list(input().split())
v = [ int(i) for i in v]

memo = [[] for _ in range(N+1)]
dp = [[-1 for _ in range(M+1)] for _ in range(N)]


def func(s,i,N):

    if(s in memo[i]):
        return
    else:
        memo[i].append(s)
    
    if(i>N-1):
        return

    if(s+v[i] <= M):
        dp[i][s+v[i]] = s+v[i]
        func(s+v[i], i+1,N)
    if(s-v[i]>=0):
        dp[i][s-v[i]] = s-v[i]
        func(s-v[i],i+1,N)\

    return

func(S,0,N)

print(max(dp[N-1]))
