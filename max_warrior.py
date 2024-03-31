def max_warrior(Ary,n):


    sum1 = Ary[0]
    sum2 = Ary[1]
    sum_max = max(sum1,sum2)
    sum_min = min(sum1,sum2)
    temp = 0

    k = n

    for i in range(2,n):

        if( k == i ):
            continue
        if(sum_min + Ary[i] > sum_max ):

            temp = sum_max
            sum_max = sum_min + Ary[i]
            sum_min = temp
        
        else:
            sum_min = sum_max
            k = i + 1
            if(i == n):
                return sum_max
            else:
                sum_max = sum_max + Ary[k]

    return sum_max

Ary = [1,3,1,5]


print(max_warrior(Ary,len(Ary)))