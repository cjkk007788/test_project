test = input("숫자를 입력하세요")
test = list(test)
test = list(map(int,test))

n= len(test)

result = 0

result = test[0]
"""
for i in range(1,n):
    
    if(test[i]==0 or test[i == 1]):##틀린 부분 1을 생각하지 못했다. 조금더 테스트 케이스를 만들기 
        #테스트 케이스 최소 4개 이상 생각해보기 #result도 마찬가지로 0 이나 1이면 더 해야한다.
        result = result+test[i]
    else:
        if(result ==0  or result == 1):
            result = result + test[i]
        else:
            result = result * test[i]

print(result)
"""

for i in range(1,n):

    if result <=1 or test[i]<=1:
        result = result+test[i]
    else:
        result = result * test[i]

print(result)

