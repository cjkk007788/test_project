def seletionsort(ary):

    n = len(ary)
    minidx = 0

    for i in range(0,n-1):
        for k in range(i+1,n):
            if(ary[minidx]>ary[k]):
                minidx = k
        temp = ary[i]
        ary[i]=ary[minidx]
        ary[minidx] = temp

    return ary


moneyAry = [7,5,4,11,6,7,11000,5,15,12]

sortedary = seletionsort(moneyAry)

middle = sortedary[len(sortedary)//2]
print(middle)
            