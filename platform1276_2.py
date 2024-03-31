import sys
input = sys.stdin.readline
N = int(input())

HEIGHT = 0
LEFT = 1
RIGHT =2

legs = []
sum = 0
platform = []

for i in range(N):
    Height,Left,Right = map(int,input().split())    
    legs.append((Height,Left,Right))

legs = sorted(legs)

platform.append(legs[0])
sum = legs[0][HEIGHT] * 2

for k in range(1,N):
    sum = sum + (legs[k][HEIGHT]*2)
    for j in range(len(platform)-1,-1,-1):
        if(platform[j][LEFT]<=legs[k][LEFT] and platform[j][RIGHT]>legs[k][LEFT]):
            sum = sum-platform[j][HEIGHT]
            break
    for j in range(len(platform)-1,-1,-1):
        if(platform[j][LEFT]<legs[k][RIGHT] and platform[j][RIGHT]>=legs[k][RIGHT]):
            sum = sum-platform[j][HEIGHT]
            break
    
    platform.append(legs[k])


print(sum)
    