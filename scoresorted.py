def selectionsort(ary):
    minIdx = 0
    n = len(ary)
    for i in range(n-1):
        minIdx = i
        for k in range(i+1, n):
            if(ary[minIdx][1]> ary[k][1]):
                minIdx= k 
        
        temp = ary[minIdx]
        ary[minIdx] = ary[i]
        ary[i] = temp
    return ary




socoreAry = [['선미',88], ['초아',71], ['화사',71], ['영탁',78], ['영웅',67], ['민호',92]]


print("정렬 전 --> ", socoreAry)

socoreAry = selectionsort(socoreAry)

print("정렬 후 --> ", socoreAry)


for i in range(len(socoreAry)//2):
    print("{}:{}".format(socoreAry[i], socoreAry [len(socoreAry)-1-i]))