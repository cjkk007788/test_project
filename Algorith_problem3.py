from operator import itemgetter

def diveGroup(tAry):

    tAry = sorted(tAry,key = itemgetter(1) ) ##내림차순 -->점점 내려간다 오름차순 -->점점 올라간다

    Gcount = 0

    n = 0
    
    while (n < len(tAry)):
        n = n + tAry[n][1]
        Gcount = Gcount+1


    return Gcount


tAry = [['A',1],['B',4],['C',4],['D',2],['E',2]]


count = diveGroup(tAry)

print(count)

