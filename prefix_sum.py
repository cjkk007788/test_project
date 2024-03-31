import sys
input = sys.stdin.readline


n,m = map(int,input().split()) ## n 은 리스트 숫자 m은 쿼리의 개수

numberArray =[0]*(n+1)
q = []

for k in range(m):
    left,right = map(int,input().split())
    q.append((left,right))

print("한줄에 한글자씩 입력")
for i in range(1,n+1):
    a = int(input())
    numberArray[i] = a

print(numberArray)

for i in range(1,n+1):
    numberArray[i] = numberArray[i-1]+numberArray[i]

while(q):
    left, right = q.pop()
    sum = numberArray[right] - numberArray[left-1]
    print(sum)