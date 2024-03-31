class graph():
    def __init__(self,size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

        
def findMaxchip(G,martAry):

    stack = []
    visitedAry = []
    current = 0
    maxchip = martAry[0][1]
    maxstore = 0

    stack.append(0)
    visitedAry.append(0)
    

    
    while(len(stack)!=0):

        next = None

        for vertex in range(G.size):
            if(G.graph[current][vertex]!=0):
                if(vertex in visitedAry):
                    pass
                else:
                    if(maxchip < martAry[vertex][1]):
                        maxchip = martAry[vertex][1] #새로운 vertex에 들렀을때 최댓값을 최신화 한다.
                        maxstore = vertex
                    next = vertex
                    break            
        if(next!=None):
            current = next
            stack.append(current)
            visitedAry.append(current)

        else:
            current = stack.pop()

    maxAry = [maxstore,maxchip]
    return maxAry
            


G1 = graph(5)

GS25, CU, Emart,seven,ministop = 0,1,2,3,4

G1.graph[GS25][CU] = 1

MartAry = [[0,30],[1,60],[2,40],[3,10],[4,90]]

G1.graph[GS25][CU]=1
G1.graph[CU][GS25]=1
G1.graph[GS25][seven] =1
G1.graph[seven][GS25] =1
G1.graph[CU][seven] =1 
G1.graph[seven][CU] =1
G1.graph[CU][ministop] =1 
G1.graph[ministop][CU] =1
G1.graph[seven][ministop] = 1
G1.graph[ministop][seven] = 1
G1.graph[ministop][Emart] = 1
G1.graph[Emart][ministop] = 1

maxAry2 = findMaxchip(G1,MartAry)

print(maxAry2[0],maxAry2[1])