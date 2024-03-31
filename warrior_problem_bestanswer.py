n = int(input("배열의 크기"))

array = list(map(int,input().split()))

d = [0]* 100

d = array[0]
d[1] = max(d[0],array[1])

for i in range(2,n):

    d[i] = max(d[i-1],d[i-1]+array[i])