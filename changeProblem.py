def change(A,B,K):

    A = sorted(A) ##기본값이 내림차순 
    B = sorted(B,reversed = True) ## 역전시키면 오름차순


    for i in range(K):
        if(A[i] < B[i]): ## B의 원소가 더 크면 교체 그렇지 않으면 그냥 나가면 된다. 이후에는 이미 모든 A의 값이 B보다 크니까
            A[i], B[i] = B[i],A[i]
        else:
            break


##핵심 먼저 정렬은 nlogn으로 수행해라!! 그게 빠르다. 매번 최대최소를 찾는거 보다 싹 빠르게 정렬하는게 빠르드라. 최대최소를 매번 찾는 것은 좋지 않다.

