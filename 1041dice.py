import sys
input = sys.stdin.readline
INF = 300

A = 0
B = 1
C = 2
D = 3
E = 4
F = 5

##A와 F가 마주본다고 생각

dice = [0] * 6

N = int(input())



a,b,c,d,e,f = map(int,input().split())

dice[A] = a
dice[B] = b
dice[C] = c
dice[D] = d
dice[E] = e
dice[F] = f

min_vertext = 300

max_x = 0
sum = 0
if(N==1):
    for k in range(A,F+1):
        max_x = max(max_x,dice[k])
        sum = sum + dice[k]

    print(sum - max_x)

else:
    min_vertext = min(min_vertext,dice[A]+dice[D]+dice[B]) 
    min_vertext = min(min_vertext,dice[A]+dice[B]+dice[C])
    min_vertext = min(min_vertext,dice[A]+dice[C]+dice[E])
    min_vertext = min(min_vertext,dice[A]+dice[E]+dice[D])
    min_vertext = min(min_vertext,dice[F]+dice[D]+dice[B])
    min_vertext = min(min_vertext,dice[F]+dice[B]+dice[C])
    min_vertext = min(min_vertext,dice[F]+dice[C]+dice[E])
    min_vertext = min(min_vertext,dice[F]+dice[E]+dice[D])

    min_edge = 300

    min_edge = min(min_edge,dice[A] + dice[D])    
    min_edge = min(min_edge,dice[A] + dice[B])    
    min_edge = min(min_edge,dice[A] + dice[C])
    min_edge = min(min_edge,dice[A] + dice[E])
    min_edge = min(min_edge,dice[B] + dice[C])
    min_edge = min(min_edge,dice[C] + dice[E])
    min_edge = min(min_edge,dice[E] + dice[D])
    min_edge = min(min_edge,dice[D] + dice[B])
    min_edge = min(min_edge,dice[F] + dice[D])
    min_edge = min(min_edge,dice[F] + dice[B])
    min_edge = min(min_edge,dice[F] + dice[C])
    min_edge = min(min_edge,dice[F] + dice[E])

    min_dimension = 300
    for k in range(A,F+1):
        min_dimension = min(min_dimension,dice[k])

    answer = 4*min_vertext + (8*N-12)*min_edge + (N-2)*(5*N-6)*min_dimension

    print(answer)