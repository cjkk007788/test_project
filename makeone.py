n = int(input())

memo = [] ## 메모에는 n과 f(n)이 들어간다 --> memo = [n,f(n)] n을 찾아야한다.
memo = [0 for _ in range(n)]

result = [n+1 for _ in range(4)]

## 변수를 재귀함수에서 사용할때 외부참조를 조심하자. 예를 들어서 재귀함수에서 변수가 계속 선언되도록 하지 말자.
## 배열을 이용해서 선언은 한번만 되도록 하기 ## 선언이 반복되면 문제가 생길 수 있다. 예를 들어서
## n-1번째 재귀함수에서 선언된 변수의 값이 n-2번째에서 변할 수 가 있다. 그러니 조심하자.


def makeone(N):

    if(memo[N-1] != 0):##이미 존재하면

        return memo[N-1]

    if(N == 1):
        return 0
    
    else:

        if(N % 5 ==0):
            result[0] = makeone(N//5) + 1
            memo[N-1]= result[0]
        
        if(N % 3 ==0 ):
            result[2] = makeone(N//3) + 1
            memo[N-1]= result[2]
        if(N % 2 ==0):
            result[1] = makeone(N//2) + 1
            memo[N-1]= result[1]
        
        result[3] = makeone(N-1) + 1
        memo[N-1]= result[3]

        return min(result[0],result[2],result[1],result[3])
    

print(makeone(n))
