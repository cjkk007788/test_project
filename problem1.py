import random


def insertSellAry(Ary,fdata):
    
    start = 0
    end = len(Ary)-1

    while(start<=end):##2진 탐색

        mid = ( start + end ) // 2

        if fdata == Ary[mid][0]:
            Ary[mid][1]= Ary[mid][1]+1 ##개수 증가
            return Ary
        
        elif fdata < Ary[mid][0]:
            end = mid-1
        else:
            start = mid +1

    if(fdata < Ary[mid][0]): ## 판매어레이에 추가
        if(mid == 0):
            Ary.insert(0,[fdata,1])
        else:
            Ary.insert(mid-1,[fdata,1])
    else:
        Ary.insert(mid+1,[fdata,1])

    return Ary

dataAry = ['바나나맛 우유','레쓰빈커피','츄파춥스','도시락','삼다수','코카콜라','삼각김밥']
SellAry = [random.choice(dataAry) for _ in range(20)]



n = len(SellAry)

LastAry = []
LastAry.append([SellAry[0],1])

for i in range(1,n):
    LastAry = insertSellAry(LastAry,SellAry[i])

print(LastAry)
