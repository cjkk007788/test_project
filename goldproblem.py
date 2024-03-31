N = int(input("행의 게수"))
M = int(input("열의 개수"))

dx = [-1]
dy = [-1,0,1]

memo = []
goldAry=[] ##원래 금괴의 값을 저장
def maxgold(goldAry):

    for row in range(1, M):##열
        for col in range(N):##행
            for i in range(3):
                if( col + dy[i] < N and col +dy[i] >-1 ):
                    goldAry[row][col] = max (goldAry[row][col] + goldAry[row+dx[i]][col+dy[0]])
                else:
                    continue
    
    max = goldAry[0][M-1]
    for i in range(1,N):
        max = max(goldAry[i][M-1],max)

    print(max)


