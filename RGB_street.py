import sys
import heapq
from collections import deque
sys.stdin.readline

RED = 1
GREEN = 2
BLUE = 3
N = int(input())

cost_list = deque()
runner_list= []
q= []
temp_list = []
for i in range(N):

    r_cost,g_cost,b_cost = map(int,input().split())
    q=[]
    heapq.heappush(q,(r_cost,RED))
    heapq.heappush(q,(g_cost,GREEN))
    heapq.heappush(q,(b_cost,BLUE)) ##리스트마다 크기 3짜리 힙이 들어간다
    cost_list.append(q) ##순서대로 cost_list에 저장 (cost_list[i][0] ==> 가장 적은값 저장)
    
now = cost_list.popleft()

runner_list.append([now[0][0],now[0][1]])
runner_list.append([now[1][0],now[1][1]])
runner_list.append([now[2][0],now[2][1]])

## 첫시행에서 1등 2등 3등 정해짐 ##러너 리스트에는 3개밖에 없고 합계와 1등 2등 3등의 이전 칼라가 저장

for i in range(N-1):
    now = cost_list.popleft() ##now에는 비용별로 저장 내림차순으로 저장
    min = now[0]
    s_min = now[1]
    ss_min = now[2]
    color = 0
    for i in range(3):## 1등에게는 자신과 다른 색깔이면서 가장 작은 거 넣기
        if(runner_list[0][1]!=now[i][1]):
            color = now[i][1]
            runner_list[0][1] = now[i][1]
            runner_list[0][0] = runner_list[0][0] + now[i][0]
            break
    
    if(color == runner_list[1][1]):
        for k in range(3):
            if(now[k][1]==runner_list[2][1]):
                runner_list[1][0] = runner_list[1][0] + now[k][0]
                runner_list[1][1] = now[k][1]
                break
        for k in range(3):
            if(now[k][1] == runner_list[0][1]):
                runner_list[2][0] = runner_list[2][0] + now[k][0]
                runner_list[2][1] = now[k][1]
                break
    if(color == runner_list[2][1]):
        for k in range(3):
            if(now[k][1] == runner_list[0][1]):
                runner_list[1][0] = runner_list[1][0] + now[k][0]
                runner_list[1][1] = now[k][1]
                break

        for k in range(3):
            if(now[k][1] == runner_list[1][1]):
                runner_list[2][1] = now[k][1]
                runner_list[2][0] = runner_list[2][0] +now[k][0]
                break

    runner_list = sorted(runner_list)

print(runner_list[0][0])