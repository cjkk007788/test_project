N = int(input("정수 N을 입력하세요")) ##  0< N <=23


Acase  = 3600 * (N+1)

Ecase = 0
if(N < 3):
    Ecase = (N+1) * 45* 45
elif(N<13):
    Ecase = (N)* 45* 45
elif (N<23):
    Ecase = (N-1)* 45*45
else:
    Ecase = (N-2)*45*45

print(Acase - Ecase)
