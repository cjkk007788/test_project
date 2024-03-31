T = int(input())

test_list = []

for k in range(T):

    number  = int (input())
    test_list.append(number)


for i in range(T):
    size = test_list[i]

    fibo_Array = [[0,0] for _ in range(41)]
    
    fibo_Array[0] = [1,0]
    fibo_Array[1] = [0,1]
    fibo_Array[2] = [1,1]

        
    for k in range(3,size+1):
        fibo_Array[k][0] = fibo_Array[k-1][0] + fibo_Array[k-2][0]
        fibo_Array[k][1] = fibo_Array[k-1][1] + fibo_Array[k-2][1]


    print(fibo_Array[size][0],fibo_Array[size][1])

        


        
