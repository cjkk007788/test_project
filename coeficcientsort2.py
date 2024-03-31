data = [0,1,4,5,7,2,4,6,20,15,17,12,12,3,4,5,6]

def coeficent(A):
    
    n = len(A)

    min = A[0]
    max = A[0]

    for i in range(n):
        if(min > A[i]):
            min = A[i]
        if(max < A[i]):
            max = A[i]

    depth = max - min  ## 최소 3 최대 5 --> 인덱스 배열의 크기는 3이어야 하므로 depth +1

    indexAry = [ 0 for _ in range( depth +1 )]

    for k in A:
        indexAry[k-min] = indexAry[k-min] + 1

    for k in range(len(indexAry)):
        for j in range(indexAry[k]):
            print(k + min ,end = ' ')
    
coeficent(data)
