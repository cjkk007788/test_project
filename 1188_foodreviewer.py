import sys
input = sys.stdin.readline

N,M = map(int,input().split())

def gcd(a,b):

    min_num = min(a,b)
    max_num = max(a,b)

    while(min_num != 0):
        temp = max_num%min_num
        max_num = min_num
        min_num = temp
    
    return max_num
 
def lcm(a,b):
    return int(a*b/gcd(a,b))


if(N%M == 0):
    print(0)
elif(N<M):
    d_length = int(lcm(N,M) / M)
    s_length = int(lcm(N,M) / N)
    full_size = lcm(N,M)
    sosage_count = 0
    answer = 0
    rest = s_length
    while(sosage_count!=N):
        if(rest == d_length):
            sosage_count = sosage_count +1
            rest = s_length
        elif(rest > d_length):
            answer = answer + 1
            rest = rest - d_length
        else:##(rest < d_length)
            diff = d_length-rest
            answer = answer + 1
            sosage_count = sosage_count +1
            rest = s_length - diff

    print(answer)

else:##N > M
    s_length = int(lcm(N,M) / N)
    d_length = int(lcm(N,M) / M) ## 소시지 길이 보다 기준 길이가 더 크다
    full_size = lcm(N,M)
    sosage_count = 0
    answer = 0
    rest = d_length
    while(sosage_count<N):
        if(rest >= s_length):
            rest = rest - s_length
            sosage_count = sosage_count + 1
        else:
            rest = d_length -(s_length-rest)
            answer = answer + 1
            sosage_count = sosage_count +1
    print(answer)
