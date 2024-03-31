def selectionSort(ary):

    minidx = 0
    n = len(ary)

    for i in range(n-1):
        minidx = i
        for k in range(i+1,n):
            if(ary[minidx] > ary[k]):
                minidx = k
        
        temp = ary[minidx]
        ary[minidx] = ary[i]
        ary[i]= temp

    return ary


ary2 = [[55,33,250,44],
        [88,1,67,23],
        [199,222,38,47],
        [155,145,20,99]
        ]

ary1 = []

for i in range(4):
    for r in range(4):
        ary1.append(ary2[i][r])

ary1 = selectionSort(ary1)

print(ary1)
