L,M = map(list,input().split())

L = list(L)
M = list(M)

l_num = len(L)
m_num = len(M)

min = 0

if(l_num!=m_num):
    print(0)

else:
    for i in range(l_num):
        if(L[i] == M[i]):
            if(L[i]=='8'):
                min = min+1
        else:
            break
    print(min)


