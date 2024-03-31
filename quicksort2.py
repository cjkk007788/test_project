def quicksort(ary,start,end):

    low = start+1
    high = end

    if(start>=end):
        return

    pivot = ary[start]

    while low<=high:
        while(ary[low] < pivot and low < end):
            low = low+1

        while(ary[high]>pivot and high> start ):
            high = high-1

        if(low<=high):
            ary[low], ary[high] = ary[high],ary[low]
            low = low +1
            high = high-1

    ary[high],ary[start] = ary[start],ary[high]

    quicksort(ary,start,low-1)
    quicksort(ary,high+1,end)


Ary = [188,150,168,162,105,120,177,50]

quicksort(Ary,0,len(Ary)-1)

print(Ary)



