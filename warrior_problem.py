def warrior(Ary,n):##n은 배열의 크기


    if(n<1):
        return
    
    max_t = [Ary[0],0]

    for i in range(n):
        if(Ary[i]> max):
            max_t[0]= Ary[i]
            max_t[1] = i
    
    sum = sum + max_t[0]

    del(Ary[max_t[1]])
    del(Ary[max_t[1]]-1)
    del(Ary[max_t[1]]+1)

    warrior(Ary,n-3)## 배열의 크기가 3씩 줄어들겠다.


sum = 0

Ary = [1,4,7,2,5,6,8,11,15,14]

print(warrior(Ary))