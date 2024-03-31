def insertionSort(ary):

    n = len(ary)

    for end in range(1,n):
        for a in range(end,0,-1):
            if(ary[a-1]>ary[a]):
                ary[a-1],ary[a] = ary[a],ary[a-1]

    return ary

