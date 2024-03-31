import math
import sys
input = sys.stdin.readline

N,r,c = map(int,input().split())


def z_problem(N,r,c,count):      

    if(N==0):
        return count
    else:
        if(1<<N-1 <r and 1<<N-1 <c):##4사분면
            r = r-(1<<N-1)
            c = c-(1<<N-1)
            count = count + 4**(N-1) * 3
            count = z_problem(N-1,r,c,count)
            return count
        elif(1<<N-1 >= r and 1<<N-1 <c):##2사분면
            c= c-(1<<N-1)
            count = count + 4**(N-1) * 1
            count = z_problem(N-1,r,c,count)
            return count
        elif(1<<N-1 >=r and 1<<N-1 >= c):##1사분면
            count = count
            count = z_problem(N-1,r,c,count)
            return count
        else:##3사분면
            r= r-(1<<N-1)
            count = count + 4**(N-1) * 2
            count = z_problem(N-1,r,c,count)
            return count
        
count = 0
answer = z_problem(N,r+1,c+1,count)

print(answer)