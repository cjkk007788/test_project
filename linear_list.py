katok = []

katok.append(None)
katok[len(katok)-1] = '다현'

print(katok)

katok.append(None)
katok[len(katok)-1]= '준규'

print(katok)

def add_data(value):

    katok.append(None)
    katok[len(katok)-1] = value

add_data("고구")
add_data("고구려")

print(katok)

def insert(position,value): ## 위치 꼭 확인하기
    list_size = len(katok)
    
    if position < 0 or position > list_size:
        print("데이터를 삽입할 범위를 벗어났습니다")
        return
    
    katok.append(None)
    
    for k in range(list_size,position,-1):
        katok[k] = katok[k-1]

    katok[position]=value

insert(3,"준규리")

print(katok)

def del_data(position):

    if position < 0 or position > len(katok)-1:
        print("삭제 범위를 벗어났다")
        return
    
    klen = len(katok)
    katok[position]= None

    for k in range(position,klen-2):
        katok[k] = katok[k+1]
    
    del(katok[klen-1])

del_data(2)

print(katok)


