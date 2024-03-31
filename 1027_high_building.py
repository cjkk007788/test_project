import sys
input = sys.stdin.readline

N = int(input())

buildings = list(map(int,input().split()))


N_count = 0
max_building = 0
def slope(i,k):

    return (buildings[k] - buildings[i])/(k-i)

def see_building(now,check,slope):
    
    if slope*(check-now)+buildings[now] < buildings[check]:
        return True
    
    
for i in range(N):
    count = 0
    if(i!=N-1):
        sl = slope(i,i+1)
        count = count +1
        for k in range(i+2,N):
            if see_building(i,k,sl):
                count = count+1
                sl = slope(i,k)
        
    if(i!=0):
        sl = slope(i,i-1)
        count = count + 1
        for k in range(i,-1,-1):
            if see_building(i,k,sl):
                count = count+1
                sl = slope(i,k)

    if N_count < count:
        max_building = i+1
        N_count = count

print(N_count)