N = int(input("화폐의 종류 입력"))
M = int(input("돈 입력"))


ms = list(map(int,input("화폐의 종류 입력하세요").split(' ')))


print(ms)

num  = 0
ms = sorted(ms,reverse= True)
rest  = M

for i in range(N):

    num = num + rest // ms[i]
    rest = rest % ms[i]

    if(rest ==0):
        print(num)
        break

if(rest !=0 ):
    print(-1)
