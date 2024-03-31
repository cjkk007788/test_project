def maxheight(Ary,M):

    h_max = max(Ary)
    h_min = 0
    
    while(h_min >= h_max):

        dif = 0           
        h = (h_max + h_min)//2 ## 중간값 설정

        for data in Ary: ## 차이합 구하기(n)
            if(data>h):
                dif = dif + (data-h)

        if(dif == M):## 찾기 차이합 == M 
            return h
        if(dif > M):## 차이합이 M보다 크면 현재 중간값을 최솟값으로 지정해서 다시 반복
            h_min = h+1
        else:##차이합이 M보다 작으면 중간값을 최댓값으로 설정해서 시작
            h_max = h-1

    