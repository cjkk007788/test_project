from operator import itemgetter

class Graph():
    def __init__(self,SIZE):
        self.size = SIZE
        self.graph = [[0 for _ in range(SIZE)] for _ in range (SIZE)] 
    

서울,뉴욕,북경,방콕,런던,파리 = 0,1,2,3,4,5

G1 = Graph(6)
G1.graph[서울][뉴욕] = 80
G1.graph[뉴욕][서울] = 80
G1.graph[서울][북경] = 10
G1.graph[북경][서울] = 10
G1.graph[북경][방콕] = 50
G1.graph[방콕][북경] = 50
G1.graph[뉴욕][북경] = 40
G1.graph[북경][뉴욕] = 40
G1.graph[뉴욕][방콕] = 70
G1.graph[방콕][뉴욕] = 70
G1.graph[방콕][런던] = 30
G1.graph[런던][방콕] = 30
G1.graph[방콕][파리] = 20
G1.graph[파리][방콕] = 20
G1.graph[런던][파리] = 60
G1.graph[파리][런던] = 60

graphAry = []
for col in range(G1.size):
    for row in range(G1.size):
        if(G1.graph[col][row] != 0):
            graphAry.append([col,row,G1.graph[col][row]])


graphAry = sorted(graphAry,key = itemgetter(2), reverse = True)

print()
print()


realAry = []

for i in range(0,len(graphAry),2):
    realAry.append(graphAry[i])


print(list(realAry))
    

index = 0


def bfSFindVertex(G1,sp,findvertx):
    stack = []
    visitedAry = []
    current = sp

    stack.append(current)
    visitedAry.append(current)

    while(len(stack) != 0):
        
        next = None

        for vertex in range(G1.size):
            if(G1.graph[current][vertex] != 0):
                if(vertex in visitedAry):
                    pass
                else:
                    next = vertex
                    break
        
        if(next != None):
            current = next
            stack.append(current)
            visitedAry.append(current)
        else:
            current = stack.pop()

    
    return (findvertx in visitedAry)

while( len(realAry) > G1.size-1):
    
    start = realAry[index][0] ##vertex와 간선정보 저장
    end = realAry[index][1]

    savecost = realAry[index][2]

    G1.graph[start][end] = 0 ## 일단 삭제
    G1.graph[end][start] = 0 ## 일단 삭제
    
    syn = bfSFindVertex(G1,start,end)
    eyn = bfSFindVertex(G1,end,start)

    if(syn and eyn):
        del(realAry[index])
    else:
        G1.graph[start][end] = savecost
        G1.graph[end][start] = savecost
        ##복구
        index = index +1


print(realAry)