def dp_fibo(n):

    global count
    memo = [0,1,1]
    if n<=2:
        return memo[n]
    else:
        for i in range(3,n+1):
            count = count+1
            memo.append( memo[i-1]+memo[i-2] )
            result = memo[i]

    return result

count = 0

print(dp_fibo(30))
