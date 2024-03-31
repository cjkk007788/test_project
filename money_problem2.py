N = int(input("화폐의 종류 입력"))
M = int(input("돈 입력"))


ms = list(map(int,input("화폐의 종류 입력하세요").split(' ')))
moneys_min = [10001 for _ in range(M)]

for i in ms:
    for k in range(M+1):
        if(moneys_min[k-i]!=10001):
            moneys_min[k] = min(moneys_min[k], moneys_min[k-i]+1)

if(moneys_min[M] == 10001):
    print(-1)
else:
    print(moneys_min[M])


