from operator import itemgetter

def makeIndex(ary,pos):
    beforeAry = []
    index = 0

    for data in ary:
        beforeAry.append([data,index])
        index = index+1

    sortedAry = sorted(beforeAry,key=itemgetter(0))##이름 순으로 정렬
    return sortedAry

def bookSearch(ary,fData):
    pos = -1

    start = 0
    end = len(ary)-1
    while(start<=end):
        mid = (start+end)//2
        if fData == ary[mid]:
            return mid
        elif fData <ary[mid]:
            end = mid-1
        else:
            start = mid +1

    return pos

bookAry = [['어린왕자','썡떽쥐베리'],['이방인','까뮈'],['부활','톨스토이'],['신곡','단테'],['돈키호테','세르반테스'],['동물농장','조지오웰'],
           ['데미안','헤르만헤세'],['파우스트','괴테'],['대지','펄벅']]

nameIndex = []
authIndex = []


nameIndex = makeIndex(bookAry,0)

authIndex = makeIndex(bookAry,1)


print("이름 인덱싱")


print(nameIndex)

print("작가 인덱싱")

print(authIndex)


