s1 = input()
s1 = list(str(s1))

s2 = input()
s2 = list(str(s2))

Array = [ [0 for _ in range(4001)] for _ in range(4001)] ## 0행 0열에는 모두 0이 들어감

n = len(s1)
m = len(s2)


for i in range(1,m+1):
    for k in range(1,n+1):
        if(s2[i-1] ==s1[k-1]):
            Array[i][k] = Array[i-1][k-1] + 1
            max_result= max(max_result, Array[i][k])

print(max_result)