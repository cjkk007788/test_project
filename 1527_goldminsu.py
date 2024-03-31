import sys
input = sys.stdin.readline

A,B = map(int,input().split())

A_NUM = len(str(A))
B_NUM = len(str(B))



def bin_change(N,number_count):

    array = [0 for _ in range(number_count)] ##자리수 만큼 0으로 채워진 배열 형성
 
    bin_a = bin(N)
    l = len(array)-1
    bin_al = len(bin_a)
    for j in range(bin_al-1,1,-1):
        array[l] = bin_a[j]
        l = l-1

    return array
    
def bin_to_gold(bin_string):

    number = len(bin_string)-1
    num = 0
    for k in range(number,-1,-1):
        if(bin_string[k]=='1'):
            num= num + int(7*((10**(number-k))))
        else:
            num = num + int(4*(10**(number-k)))
    return num

answer = 0

for k in range(2**A_NUM):
    str_num = bin_change(k,A_NUM)
    num = bin_to_gold(str_num)
    if(num >= A and num <=B):
        answer = answer+1
if(A_NUM !=B_NUM):
    for j in range(2**B_NUM):
        str_num = bin_change(j,B_NUM)
        num = bin_to_gold(str_num)
        if num <= B:
            answer =answer+1
        else:
            break

    for k in range(A_NUM+1,B_NUM):
        answer = answer + 2**k

print(answer)
