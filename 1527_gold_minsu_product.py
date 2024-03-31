from itertools import product

a,b = map(int,input().split())

a_len = len(str(a))
b_len = len(str(b))

count = 0

for i in range(a_len,b_len+1):
    for n in product([4,7], repeat = i) :
        join  = ''.join(list(map(str,n))) ##숫자 문자열을 하나의 문자열로 바꾸는 방법
        if a<=int(join)<=b:
            count = count+1

print(count)
