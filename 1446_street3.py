import sys
input = sys.stdin.readline

N,D = map(int,input().split())

d = [0]*(D+1)

for i in range(D+1):
    d[i] = i


for i in range(N):
    start,end,length = map(int,input().split())
    
    if(end <= D and end-start>length):
        d[end] = min(d[end],d[start]+length)

for k in range(D):
    d[k+1] = min(d[k+1],d[k]+1)

print(d[D])