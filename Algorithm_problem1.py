def acmin(N,K):

    count = 0

    while(N != 1):
        count = count +1
        if(N % K == 0):
            N = N/K
        else:
            N = N-1

    return count

N = 0

N = int(input("N을 입력하세요-->"))
K = int(input("K를 입력하세요-->"))

count = acmin(N,K)

print(count)

