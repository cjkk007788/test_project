n,k = map(int,input().split())

result = 0 

while True:
    ##여기서 바로 그냥 만든다.--> n//k를 만들어버리고 n을 구한다.
    target = (n//k)*k ## ==> n-1을 하는 횟수를 줄이기 위한 방법
    result = result + (n-target)
    n = target

    if n<k:
        break
    ##이미 나누어떨어지는 수가 되어버렸으므로 나눈다.

    result = result +1
    n = n//k


##나머지 수에대해서 뺀다.

result = result + n-1

print(result)

