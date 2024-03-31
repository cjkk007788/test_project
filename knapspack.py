def knapspack():

    array = [[0 for _ in range(maxWeight+1) for _ in range(rowCount + 1 )]]

    for row in range(1,rowCount+1):
        print(row,'개-->',end = ' ')
        for col in range(1,maxWeight+1):
            if( weight[row] > col ):
                array[row][col] = array[row-1][col]
            else:
                value1 = array[row-1][col]
                value2 = money[row] + array[row-1][col-weight[row]]
                array[row][col] = max(value1,value2)
            print("%2d" %array[row][col], end = ' ')
        print()

    return array[maxWeight][rowCount]

maxWeight = 7
rowCount = 4
weight = [0,6,4,3,5]
money = [0,13,8,6,12]

