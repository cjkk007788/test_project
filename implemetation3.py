def quickSort(Ary,start,end):

    pivot = start
    low = start+1
    high = end

    if(start>=end):
        return

    while(low<=high):
        while( Ary[low] < Ary[pivot] and low < end):
            low = low + 1
        while (Ary[high] > Ary[pivot] and high > start):
            high = high-1
        
        if(low <= high):
            Ary[low],Ary[high] = Ary[high],Ary[low]
            low = low+1
            high = high-1
        Ary[high],Ary[pivot] = Ary[pivot],Ary[high]

    quickSort(Ary,start,high-1)
    quickSort(Ary,high+1,end)



st = input("숫자와 대문자가 포함된 문자열을 입력하세요").split()

st = list(st)
st = list(st[0])

newlist = []
result = 0
for data in st:
    if(data.isalpha()):
        newlist.append(data)
    else:
        result = result + int(data)


quickSort(newlist,0,len(newlist)-1)

for data in newlist:
    print(data,end='')

print(result)

