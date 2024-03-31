def findMinidx(ary):
    minidx = ary[0]
    for i in range(1,len(ary)):

        if(minidx > ary[i]):
            minidx = i
    return minidx



before = [188,162,168,120,50,177,105]

after = []

print("정렬 전 --> before")

for _ in range(len(before)):

    minpos = findMinidx(before)
    after.append(before[minpos])
    del(before[minpos])

