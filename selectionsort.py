def findinsert(ary,data):

    position =-1
    for i in range(len(ary)):
        if(ary[i]>data):
            position = i
            break
    if position == -1:
        return len(ary)##없으면 맨 끝으로
    else:
        return position
    
before = [188,162,168,120,50,150,177,105]
after = []

print('정렬 전 -->', before)


for i in range(len(before)):
    data = before[i]
    inspos = findinsert(after,data)
    after.insert(inspos,data)

print("정렬 후 -->",after)