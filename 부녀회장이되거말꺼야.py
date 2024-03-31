T = int(input())

test_list = []

for i in range(T):
    
    N = int(input()) ## 호수
    K = int(input()) ## 층수

    test_list.append([N,K])


for i in range(T):

    N = test_list[i][0]##호수
    K = test_list[i][1]##층

    daily_apartment = [[0 for _ in range(15)] for _ in range(15)] ## 15 15 0-0은 k층 0호는 0명이 산다고 가정한다.

    for k in range(1,15):
        daily_apartment[0][k] = k ##초기화 0층 K호 -->K명이 산다고 가정

    for k in range(1,K+1): ## 1층에서부터 K층까지
        for n in range(1,N+1): ## 1호에서부터 N호까지
            daily_apartment[k][n] = daily_apartment[k][n-1] + daily_apartment[k-1][n]## 1층 1호는 0층 0호 + 0층 1호
    
    print(daily_apartment[N][K])

    
                
        
    
