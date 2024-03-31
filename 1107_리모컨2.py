import sys
input = sys.stdin.readline


N = int(input())
M = int(input())

nonbroken = []
N_digiit = len(str(N))
count = abs(N-100) ## 오로지 +랑 -만 눌렀을때 


if(M!=0):
    broken = list(map(int,input().split()))
    for i in range(10):
        if i in broken:
            continue
        else:
            nonbroken.append(i)

    min_count = count

    for i in range(1000000):
        num = str(i)

        for k in range(len(num)):
            if int(num[k]) in broken:
                break
            elif k == len(num)-1:
                min_count = min(min_count,len(num) + abs(int(num)-N))
    answer = min_count

else:
    answer = min(count,len(str(N)))

print(answer)