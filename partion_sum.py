import sys
import heapq
input = sys.stdin.readline

print("리스트 문자들 입력하세요")
numberAry =list(map(int,input().split( )))

print("쿼리 개수를 입력하세요")

n = int(input())
q = []

hq_left = []
hq_right=[]

Arraysum = sum(numberAry)

for i in range(n):
    left,right = map(int,input().split())
    q.append([left,right])
    heapq.heappush(hq_left,left) ## left는 -붙이고 들어간다
    heapq.heappush(hq_right,-right)## right가 -붙이고 들어가면 -1 -3 -7 -7이런애들부터 나올테니까 가장 큰 right가 먼저 나오네

m = len(numberAry) # m -->배열의 길이

index = m-1
while(hq_right):
    
    sum_temp = 0
    now = heapq.heappop(hq_right)
    now = now * (-1) ##right부터 나올테니까
    if(now == m-1):
        sum_temp = 0
        continue
    else:
        for k in range(index,now,-1):
            sum_temp = sum_temp + numberAry[k]
    
        numberAry[now+1] = sum_temp## now 1번 위치에 right(now) 저장 right(now) S(n-1 ~ now+1)
        index = now+1

index = 0
while(hq_left):
    sum_temp = 0
    now = heapq.heappop(hq_left)
    if(now == 0):
        sum_temp = 0
        continue
    for k in range(index,now):
        sum_temp = sum_temp +numberAry[k] ##now -1 번 위치에 left(now) 저장 left now S (0 ~ now -1 )
    numberAry[now-1] = sum_temp
    index = now-1

sum= [0] * n##쿼리 개수

index = 0
while(q):
    
    left_sum= 0
    right_sum = 0
    temp = q.pop()
    
    if(temp[0]==0):
        left_sum = 0
    else:
        left_sum = numberAry[temp[0]-1]
    
    if(temp[1]==m-1):
        right_sum = 0
    else:
        right_sum = numberAry[temp[1]+1]
    
    sum[index] = Arraysum - left_sum - right_sum

    print(sum[index])
    index = index +1 