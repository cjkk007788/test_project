import sys
input = sys.stdin.readline
LOG = 24 ##2^24 ==>1048576 (10 7승부터 더하면 된다)

N,K = map(int,input().split())
min = [0]*2

if(N == K):
    print(0)
elif N < K :
    print(K-N)
else:
    rest = N
    count = 0
    d =[0] * (LOG) ## 인덱스 0 ~ 25까지 존재
    for i in range(LOG-1,-1,-1):
        if(rest >= 1<<i):
            count = count +1
            d[i] = 1
            rest = rest % (1<<i)
    if count == K:
        print(0)
    elif count < K:
        print(0)
    else: ##count > k 인경우 물병을 더 사서 줄여 나가기
        k = 0
        start = 0
        num = count-K
        d_sum =0
        for j in range(LOG):
            if(d[j]!=0):
                min[k] = 1<<j
                k = k+1
                if(k==2):
                    start = j+1
                    break
        d_pre = min[1]
        d_sum = min[1] - min[0]
        num = num-1
        for j in range(start, LOG):
            if(num == 0):
                break
            if(d[j]!=0):
                d_sum = d_sum + (1<<j) - (d_pre*2)
                d_pre = 1<<j
                num = num - 1
               
        print(d_sum)