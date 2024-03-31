import random
import time
import sys
sys.setrecursionlimit(10**7)

def bublesort(Ary):
    n = len(Ary)

    ChangeYN = 0
    for end in range(n-1,0,-1):
        for k in range(0,end):
            if(Ary[k]>Ary[k+1]):
                Ary[k],Ary[k+1] = Ary[k+1],Ary[k]
                ChangeYN = ChangeYN+1
        if(ChangeYN == 0):
            break
    return Ary

def selectionsort(ary):

    n = len(ary)

    for i in range(n-1):
        
        minidx = i

        for k in range(i+1,n):
            if ary[k] < ary[minidx]:
                minidx = k
        
        ary[i],ary[minidx] = ary[minidx],ary[i]

    return ary


def qsort(ary,start,end):


    if (start>=end):
        return 
    
    low = start + 1
    high = end
    pivot = start

    while(low <= high):

        while(ary[low]<=ary[pivot] and low < end ):
            low = low +1
        while(ary[high]>=ary[pivot] and high > start ):
            high = high-1

        if(low>high):
            ary[high],ary[pivot] = ary[pivot],ary[high]
 
        else:
            ary[high],ary[low] = ary[low], ary[high]
            high = high-1
            low = low+1
    
    qsort(ary,start,high-1)
    qsort(ary,high+1,end)

def quickSort(ary):

    qsort(ary,0,len(ary)-1)



countAry = [1000,10000,12000,15000]

for count in countAry:

    tempAry = [random.randint(10000,99999) for _ in range(count)]
    selectAry = tempAry[:]
    quickAry = tempAry[:]
    bubleAry = tempAry[:]

    print("데이터의 개수",count,"개")
    start = time.time()
    selectionsort(selectAry)
    end = time.time()
    print("선택정렬 --> %10.3f초" %(end -start))

    print("데이터의 개수",count,"개")
    start = time.time()
    bublesort(bubleAry)
    end = time.time()
    print("버블정렬 --> %10.3f초" %(end -start))

    
    
    print("데이터의 개수",count,"개")
    start = time.time()
    quickSort(quickAry)
    end = time.time()
    print("퀵 정렬 --> %10.3f초" %(end -start))
    
    print()

