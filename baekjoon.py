T = int(input())

test_list = []

for k in range(T):

    number = int(input())
    test_list.append(number)

    N_list = [0 for _ in range(12)]


for i in range(T):
    
    n = test_list[i]

    N_list[0] = 0
    N_list[1] = 1
    N_list[2] = 2
    N_list[3] = 4

    for j in range(4,n+1):

        N_list[j] = N_list[j-1] + N_list[j-2] + N_list[j-3]


    print(N_list[n])