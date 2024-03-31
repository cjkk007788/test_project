import sys
import heapq
import bisect
from operator import itemgetter
input = sys.stdin.readline

N = int(input())
platform = []
Right_legs = []
Left_legs = []

for i in range(N):
    Height,Left,Right = map(int,input().split())
    heapq.heappush(platform,(Left,Right,Height)) ## LEFT 로 먼저 정렬 

##1번 다리 설치

l,r,h = heapq.heappop(platform)

Left_legs.append([l,0,h,h]) ## 왼쪽 좌표, 땅의 높이, 그리고 길이, 그리고 높이
Right_legs.append([r,0,h,h])##왼쪽 좌표 땅의 높이, 그리고 길이,그리고 높이
##1번 다리는 그냥 설치

##1번 다리는 그냥 설치 ## 

while(platform):
    l,r,h = heapq.heappop(platform) ## 왼쪽 다리 위치 오른쪽 다리 위치 그리고 높이
    if(Right_legs[len(Right_legs)-1][0] <= l):## left 보다 큰 R이 없으면 그냥 설치한다.
        Left_legs.append([l,0,h,h])
        Right_legs.append([r,0,h,h])
        continue
        
    else: ##겹치는 경우 왼쪽 처리
        fri = bisect.bisect_right(Right_legs,[l,0,h,h]) ##first right index (left보다 큰 right의 최소 위치 인덱스)
        fhi = bisect.bisect_left(Right_legs[fri:],[l,0,h,h],key = lambda x:x[3]) ## 플랫폼의 높이 다음위치
        if(Right[fri][0] == l):#같은 위치라면 땅부터 설치
            bisect.insort(Left_legs,[l,0,h,h],key = lambda x:x[0])
        else:
            bisect.insort(Left_legs,[l,Right_legs[fhi][3],h-Right_legs[fhi][3],h],key = lambda x:x[0]) ##왼쪽다리 겹치는 경우 추가

        ##오른쪽 처리
        fli = bisect.bisect_left(Right_legs,[r,0,h,h]) ## 자기보다 작은 오른쪽 다리의 최대값까지
        if(fli == len(Right_legs)-1):
            Right_legs.append([r,0,h,h])## 자기보다 작은 오른쪽 다리가 없는 경우 그냥 설치
        for k in range(fri,fli+1):
            if(Right_legs[k][3] > h and Right_legs[k][1] <h):##바닥이 높이 보다 낮으면서 플랫폼의 높이는 높은 경우
                Right_legs[k][2] = Right_legs[k][2] - (h-Right_legs[k][1])
                Right_legs[k][1] = h
        
        if(Right_legs[fli][0]<= r): ##밑에 뭐가 없는 경우
            bisect.insort(Right_legs,[r,0,h,h],key = lambda x:x[0])    
        else:##밑에 뭐가 있는 경우
            fhhi = bisect.bisect_left(Right_legs[fli+1:],[r,0,h,h],key = lambda x:x[3]) ## 플랫폼의 높이 다음위치 오른쪽 다리
            bisect.insort(Right_legs[fli+1:],[r,Right_legs[fhhi][1],])

sum = 0

for i in range(len(Left_legs)):
    sum = sum+Left_legs[i][2]
for k in range(len(Right_legs)):
    sum = sum+Right[i][2]

print(sum)



