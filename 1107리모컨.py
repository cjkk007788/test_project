import sys
input = sys.stdin.readline
from itertools import product

def make_Abs(tuple):
    n = len(tuple)
    number = 0
    for i in range(n):
        number = number + tuple[i] * (10**i)
    return number
    

N = int(input())
M = int(input())

nonbroken = []
N_digiit = len(str(N))
count = abs(N-100) ## 오로지 +랑 -만 눌렀을때 

if(M!=0):
    broken = list(map(int,input().split()))
    for i in range(10):
        if i in broken:
            continue
        else:
            nonbroken.append(i)

min_count = count

if(M !=0):
    for i in range(N_digiit-1,N_digiit+2):
        if(i==0):
            continue
        for k in product(nonbroken,repeat = i):
            number = make_Abs(k)
            if(min_count>abs(number-N)):
                min_count = abs(number-N)
                if(number-N>0):
                    index =0
                else:
                    index =1

    if(min_count == count):
        print(count)    
    else:
        if(index ==0):
            answer = min_count + len(str(abs(N+min_count)))
        else:
            answer = min_count + len(str(abs(N-min_count)))
        print(answer)
else:
    answer = min(count,len(str(N)))
    print(answer)