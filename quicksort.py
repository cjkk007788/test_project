def quicksort(Ary):

    n = len(Ary)

    if n <= 1:
        return Ary
    
    leftAry = []
    rightAry = []
    midAry= []
    pivot = n//2

    for num in range(n):
        if Ary[num] < Ary[pivot]:
            leftAry.append(Ary[num])
        elif Ary[num] > Ary[pivot]:
            rightAry.append(Ary[num])
        else:
            midAry.append(Ary[num])
    return quicksort(leftAry) + midAry + quicksort(rightAry)

dataAry = [188,150,168,162,105,120,177,50]


print("정렬 전",dataAry)
dataAry = quicksort(dataAry)
print("정렬 후",dataAry)