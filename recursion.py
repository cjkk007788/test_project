def printStar(n):
    if (n > 0 ):
        print("*" * n)
        printStar(n-1)
        

printStar(5)

def gugu(dan,num):
    print("%d x %d = %d" %(dan,num, dan*num))

    if (num <9):
        gugu(dan,num+1)

for dan in range(2,10):
    gugu(dan,1)


def exp(num,ex):

    if(ex == 1):
        return num
    
    return num * exp(num,ex-1)

a = exp(2,5)

print(a)


def palindrom(pstr):
    if len(pstr)<=1:
        return True
    else:
        if(pstr[0] !=pstr[-1]):
            return False
        
    return palindrom(pstr[1:len(pstr)-1])