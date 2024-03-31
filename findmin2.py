def selectionsort(ary):
    n = len(ary)

    for i in range(0,n-1):
        minidx =i
        for k in range(i+1,n):
            if(ary[minidx]>ary[k]):
                minidx=k
        tmp = ary[i]
        ary[i]=ary[minidx]
        ary[minidx] = tmp

    return ary



