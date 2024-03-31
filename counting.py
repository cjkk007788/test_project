def counting(Ary,findata,N):

    start = 0
    end = N
    lastposition = 0
    lastposition2 = 0
    while(start <= end ):
        mid = start + end
        if(findata == Ary[mid]):
            lastposition = mid
            end = mid-1
        elif(findata>Ary[mid]):
            start = mid + 1
        else:
            end = mid -1
    
    start = 0
    end = N
    
    while(start <= end ):
        mid = start + end
        if(findata == Ary[mid]):
            lastposition2 = mid
            start = mid + 1
        elif(findata>Ary[mid]):
            start = mid + 1
        else:
            end = mid -1

    return (lastposition2 - lastposition + 1)



dataAry= [1,2,3,4,4,4,4,4,4,4,5,6,7,8]


print(counting(dataAry,4,13))
