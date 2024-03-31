Goldmaze = [
    
    [1,4,4,2,2],
    [1,3,3,0,5],
    [1,2,4,3,0],
    [3,3,0,4,2],
    [1,3,4,5,3]]

memoization = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    if(i==0):
        memoization[0][i] = Goldmaze[0][i]
        memoization[i][0] = Goldmaze[i][0]
    else:
        memoization[0][i] = memoization[0][i-1] + Goldmaze [0][i] ## 1행 가로 누적
        memoization[i][0] = memoization[i-1][0] + Goldmaze [i][0] ## 1열 누적

    for i in range(4):
        for k in range(4):
            memoization[i+1][k+1] = Goldmaze[i+1][k+1]+max(memoization[i+1][k],memoization[i][k+1])


print(memoization[4][4])

def print_memoization(Ary):
    for row in range(5):
        for col in range(5):
            print(memoization[row][col],end = '  ')
        print()


print_memoization(memoization)


row = 4
col = 4

print()

memoization[row][col] = 0
    
while (True):
    
    if(row == 0 and col ==0):
        memoization[row][col] = 0
        break

    if(row == 0):
        memoization[row][col] = 0
        col = col-1
        continue
    if(col == 0):
        memoization[row][col] = 0
        row = row-1
        continue
    if(memoization[row-1][col] > memoization[row][col-1]):
        ##위에게 더 큰 경우 위로 이동
        row = row-1
    else:
        col = col-1
        
    memoization[row][col] = 0
    
    
print_memoization(memoization)