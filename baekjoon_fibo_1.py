def fibonach(N,count):

    
    if(N == 0 ):
        count[0] = count[0] + 1

        return 1
    if(N == 1):
        count[1] = count[1] + 1
        return 1
    
    if(N in memo):
        return memo[N]

    else:
        memo[N] = fibonach(N-1,count) + fibonach(N-2,count)

        return memo[N]
    
        
        

T = int(input())

test_list = []
count_list = [[0,0] for _ in range(T)] ##0의 개수 1의 개수 모두 생각해야하므로

for k in range(T):
    number = int (input())
    test_list.append(number)

for i in range(T):
    
    memo = [0 for _ in range(test_list[i])]
    memo.append(1)
    memo.append(1)
    
    fibonach(test_list[i],count_list[i])
    
    print(count_list[i][0],count_list[i][1])



