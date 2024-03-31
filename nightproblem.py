x = 0
y = 0

x = int(input ("나이트의 행 1,2,3,4,5,6,7,8"))
y = input("나이트의 열 a,b,c,d,e,f,g,h") ## 아스키 코드 a = 97

y = ord(y)-96 ## x와 y는 현재 위치의 -1의값이 들어가있다 --> 연산은 0과 7이 끝값이고 출력시에는 1씩 더해서 출력한다

count = 0

dx = [1,-1,2,-2]
dy = [1,-1,2,-2]
print(x,y)


for row in dx:
    for col in dy:
        if abs(row) == abs(col):
            continue
        elif(x+row < 1 or x+row > 8 or y+col < 1 or y+col>8):
            continue
        else:
            count = count+1

print(count)
    