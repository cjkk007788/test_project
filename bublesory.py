def BubbleSort(ary):
    n = len(ary)

    for end in range(n-1,0,-1):
        
        changeYN = False
        for k in range(end):
            if(ary[k]<ary[k+1]):
                changeYN = True
                ary[k],ary[k+1] = ary[k+1],ary[k]
        if(changeYN == False):
            break

    return ary


