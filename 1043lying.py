import sys

def check(party,Black_list):
    len_p  = party[0] ## 사람 수 

    for j in range(1,len_p+1):
        if(party[j] in Black_list): 
            return True
    
    return False


def append_list(party,Black_list):
    for k in range(1,party[0]+1):
        Black_list.append(party[k]) ## 진실리스트에 추가 하기
        
N,M = map(int,input().split())
Black_list = [] ## 0번 인덱스에는 사람수가 들어오고 1번부터 리스트
temp = []
party = [] ## 0번 인덱스에는 인원수 1번 ~ 끝까지 오는 인원의 번호

arr = list(map(int,input().split()))
for i in range(len(arr)):
    Black_list.append(arr[i])

Black_list = Black_list[1:] ## 블랙리스트 1번에는 인원수가 들어가니까 버려도 괜찮다.

for k in range(M):
    party.append(list(map(int,input().split())))

while(True):
    B_len = len(Black_list)
    for k in range(M):
        if(check(party[k],Black_list)):
            append_list(party[k],Black_list)
            Black_list = list(set(Black_list))
        else:
            continue
    if(B_len == len(Black_list)): ## 숫자에 변화 없으면 끝
        break

count = 0

for k in range(M):
    if(check(party[k],Black_list)):
        count = count + 1

print(M-count)

