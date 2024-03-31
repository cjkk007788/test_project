def quick_sort(array,start,end):

    if start>= end:
        return
    
    pivot = start
    low = start + 1
    high = end

    while(low<=high):

        while(low <= end and array[low] <= array[pivot]):
            low = low +1
        while(high > start and array[high] >= array[pivot]): ## 피벗이랑 값이 같아도 넘어가도록 만들어야한다. 그래야 반드시 엇갈림
            high = high-1
        
        if(low > high):
            array[high], array[pivot] = array[pivot], array[high]
        else:
            array[high],array[low] = array[low],array[high]

    quick_sort(array,start,high-1)
    quick_sort(array,high+1,end)            

 
        