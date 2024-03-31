def bublesort(Ary):

    n = len(Ary)
    ChangeYN = 0
    for end in range(n-1,0,-1):
        for k in range(0,end):
            if(Ary[k]>Ary[k+1]):
                Ary[k],Ary[k+1] = Ary[k+1],Ary[k]
                ChangeYN = ChangeYN+1
        if ChangeYN ==0:
            break

    return Ary

def qsort(Ary,start,end):

    if(start>=end):
        return
    
    low = start+1
    high = end
    pivot = start


    while(low<=high):
        while(Ary[low]<Ary[pivot] and low < end):
            low = low+1
        while(Ary[high]>Ary[pivot] and high > start):
            high =high-1
        if(low<high):
            Ary[low],Ary[high] = Ary[high], Ary[high]
            high = high-1
            low = low +1
        else:
            Ary[pivot],Ary[high] = Ary[high],Ary[pivot]

    qsort(Ary,start,high-1)
    qsort(Ary,high+1,end)
    

