h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) +str(j)+str(k):
                count = count +1


print(count)

##이런건 기하급수적으로 경우의 수가 많지 않다. 최대 24*60*60으로 제한되어있으므로 그냥 O(N)이 문제가 없다. N도 생각해보니 23까지다. N이 막 늘어나면 문제