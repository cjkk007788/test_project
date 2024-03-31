import math


def isprimenumber(n):

    for i in range(2,int(math.sqrt(n))+1):
        if(n % i ==0):
            return False
        else:
            True


        
def eratos(n):

    array = [True]*(n+1)
    for i in range(2,int(math.sqrt(n)+1)):
        if(isprimenumber(i)):
            index = i
            j = 2
            while(index<=n):    
                array[index*j] = False
                j = j+1