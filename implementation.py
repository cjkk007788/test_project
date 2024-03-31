dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(input("공간의 크기를 입력하세요"))
planner = input("계획서를 입력하세요 L(Left) R(Right) U(UP) D(Down)").split()

planner = str(planner)
planner = list(planner)


x=1
y=1

for ch in planner:
    if(ch == 'L'):
        if(y==1):
            continue
        y = y+ dy[2]
    elif(ch =='R'):
        if(y==N):
            continue
        y = y+ dy[3]
    elif(ch == "U"):
        if(x==1):
            continue
        x = x +dx[0]
    elif(ch == "D"):
        if(x==N):
            continue
        x = x+dx[1]
    else:
        continue

print("(",x,",",y,")")
