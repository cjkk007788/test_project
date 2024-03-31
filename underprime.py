import math
A,B = map(int,input().split())


underprime = 0

def is_prime(N):

    if(N<=1):
        return False
    if(N==2):
        return True
    if(N==3): 
        return True
    
    for i in range(2,root_num(N)):
        if(N%i==0):
            return False
    
    return True
    
def root_num(N):
    return (int(math.sqrt(N)))+1
  
def prim_find(N):##소수의 개수찾기
    
    count = 0
    for i in range(2,root_num(N)):
            while(N%i == 0):
                if(N%i == 0):
                    count = count +1
                    N = N//i
    if(N>1):
        count = count+1
                
    return count

for i in range(A,B+1):
    if(is_prime(prim_find(i))):
        underprime= underprime+1

print(underprime)
        