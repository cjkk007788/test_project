n = 5 ## 데이터의 개수
m = 5 ## 찾고자하는 부분합

Array = []

for i in range(n):
    num = int(input())
    Array.append(num)

end = 0
partsum = 0 
count = 0

for start in range(n):    


    while(end < n and partsum <m):
        partsum = partsum+Array[end]
        end = end +1

    if(partsum == m):
        count = count+1

    partsum = partsum-Array[start]

    
    