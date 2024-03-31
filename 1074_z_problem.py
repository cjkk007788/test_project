import sys
input = sys.stdin.readline

N,r,c = map(int,input().split())


def z_fun(N,r,c,count,x,y):

    if(N==1):
        if(x==r and y ==c):
            return x,y,count
        y = y+1
        count = count+1
        if(x==r and y==c):
            return x,y,count
        y = y-1
        x = x+1
        count = count +1
        if(x==r and y ==c):
            return x,y, count
        y = y+1
        count = count+1
        if(x == r and y== c):
            return x,y,count

        return x,y,count
    elif(N>=2):
        
        for i in range(1,5):
            x,y,count = z_fun(N-1,r,c,count,x,y)

            if(i==1):##1번째 우상향
                x = x- (1<<(N-1)) + 1
                y = y+1
                count = count+1
                continue
            elif(i==2):##1좌하향
                x = x + 1
                y = y - (1<<N) + 1
                count = count+1
                continue
            elif(i==3):##2번째 우상향
                x = x- (1<<(N-1)) + 1
                y = y+1
                count = count+1
                continue
            else:## 마지막 우상향
                x = x-(1<<(N)) + 1
                y= y+1
                count = count+1
                continue

        return x,y,count


count = 0


a,b,answer = z_fun(N,r+1,c+1,count,1,1)
print(answer)