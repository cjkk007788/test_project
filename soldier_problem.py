N  = int(input("병사수를 입력하세요"))
soldier_list = list(map(int,input("병사 정보를 입력하세요").split(' ')))

n = len(soldier_list)
d = []

for i in range(n):

    d.append(1)
    for k in range(i):
        if(soldier_list[i]<soldier_list[k]):
            d[i] = d[i] +1

max_result = max(d)

print(n-max_result)



