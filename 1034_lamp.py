import sys
input = sys.stdin.readline

N,M = map(int,input().split())

graph = []
count = []
answer = [0] * 51

for i in range(N):
    number = input().strip()
    num_list = list(map(int,str(number)))
    graph.append(num_list)

K = int(input())



for n in range(N):
    count_n = 0
    for m in range(M):
        if(graph[n][m] == 0):
            count_n = count_n+1 ## 0의 개수 저장 1번 행에 대해서
    
    if(count_n<= K and count_n % 2 == K%2): ## 0의 개수 저장후 각 행에 대해서 같은 행이 있는 지확인
        for j in range(N):
            if(graph[j] == graph[n]):
                answer[n] = answer[n] +1

print(max(answer))


