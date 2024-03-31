A,B,C = map(int,input().split())


def power(A,B,C):

    if(B == 0):
        return 1
    if(B == 1):
        return A%C
    
    k = power(A,B//2,C)%C

    if(B%2==0):
        return (k * k) % C
    else:
        return ((k * k) % C * (A%C))%C 
    

print(power(A,B,C))

