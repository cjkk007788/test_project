from operator import itemgetter

class Graph():
    def __init__(self,size):
        self.size =size
        self.graph = [[0 for _ in range(size) for _ in range(size)]]

def findVertex(G,findata):

    current = 0
    visitedAry =[]
    stack  = []
    visitedAry.append(current)
    stack.append(current)

    while (len(stack) !=0 ):
            
        next = None
        for vertex in range(G.size):
            if(G.graph[current][vertex] != 0): ##연결 되어 있다.
                if(vertex in visitedAry):
                    pass
                else:
                    next = vertex
                    break
        
        if(next != None):
            current = next
            visitedAry.append(current)
            stack.append(current)
        else:
            current = stack.pop()

    if findata in visitedAry:
        return True
    else:
        return False



                

        


nameAry = ['춘천','서울','속초','대전','광주','부산']
춘천,서울,속초,대전,광주,부산 = 0,1,2,3,4,5
gsize =6

G1 = Graph(gsize)

G1.graph[서울][춘천] = 10
G1.graph[춘천][속초] = 15
G1.graph[서울][춘천] = 10
G1.graph[서울][속초] = 40
G1.graph[서울][대전] = 11
G1.graph[서울][광주] = 50
G1.graph[속초][춘천] = 15
G1.graph[속초][서울] = 40
G1.graph[속초][대전] = 12
G1.graph[대전][서울] = 11
G1.graph[대전][속초] = 12
G1.graph[대전][광주] = 20
G1.graph[대전][부산] = 30
G1.graph[광주][서울] = 50
G1.graph[광주][대전] = 20
G1.graph[광주][부산] = 25
G1.graph[부산][대전] = 30
G1.graph[부산][광주] = 25

edgeAry = []

for i in G1.size:
    for k in G1.size:
        if( G1.graph[i][k] != 0 ):
            edgeAry.append([G1.graph[i][k],i,k]) ## [가중치, 출발, 도착] --> 크기가 3인 리스트로 간선 저장 

edgeAry = sorted(edgeAry, key = itemgetter(0),reverse= True) ## sorted --> 리스트 정렬, key

newAry = []

for i in range(0,len(edgeAry),2):
    newAry.append(edgeAry[i]) ##두개씩 중복되므로 중복간선 제거


index = 0

while ( len(newAry) > G1.size -1 ):
    
    start = newAry[index][1]
    end = newAry[index][2]

    SaveCost = G1.graph[index][0]

    G1.graph[start][end] = 0
    G1.graph[end][start] = 0 ## 1차 삭제 -->그래프내부 값만 변경

    startYn = findVertex(G1,start) ## 삭제하고 나서 확인
    endYn = findVertex(G1,end) ## 삭제하고 나서 확인

    if startYn and endYn : ##삭제했을때 연결된 두 그래프 모두 그래프와 연결되어 있으면
        del(newAry[index])## 최종삭제 간선 집합에서 제거
        pass
    else:
        G1.graph[start][end] = SaveCost
        G1.graph[end][start] = SaveCost
        
        index = index+1
