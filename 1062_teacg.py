import sys
from itertools import combinations

input = sys.stdin.readline


def check(word,char_list):
    
    for c in word:
        if not c in char_list:
            return False
    return True



N,K = map(int,input().split())

words = []
for i in range(N):
    word = input().rstrip()
    words.append(word)


if(K<5):
    print(0)
elif (K==26):
    print(N)

else:
    answer = 0

    alpha = ['b','d','e','f','g','h','j','k','l','m','o','p','q','r','s','u' ,'v','w','x','y','z']
    
    number = K-5
    base = ['a','c','i','n','t','c']

    combination_list = list(combinations(alpha,number))
    
    for com in combination_list:
        real_list = base + list(com)
        num = 0
        for word in words:
            if(check(word,real_list)):
                num = num + 1
        answer = max(answer,num)

    print(answer)

        

    