import sys
input = sys.stdin.readline
FULL = 0
EMPTY = 1
N = int(input())

graph = [[[-1,-1] for _ in range(2)] for _ in range(2*N+1)]

def fun(Depth,State,Parent,grandparent,N):
  
    if(graph[Depth][State][Parent]!=-1):
        return graph[Depth][State][Parent]
    else:
        if(Depth == 2*N):
            return 1
        
        if(Depth % 2 !=0):## 현재가 홀 수 인경우
            if(grandparent == FULL):
                graph[Depth][State][Parent] = fun(Depth+1,EMPTY,State,Parent,N)
                return graph[Depth][State][Parent] 
            else:
                if(State == FULL):##현재가 찬경우
                    graph[Depth][State][Parent] = fun(Depth+1,EMPTY,State,Parent,N)
                    return graph[Depth][State][Parent]
                else: ## 조부모랑 부모가 둘다 안 찬 경우 두가지 경우를 더한다.
                    graph[Depth][State][Parent] = fun(Depth+1,EMPTY,State,Parent,N) + fun(Depth+1,FULL,State,Parent,N)
                    return graph[Depth][State][Parent]
        else: ## 현재가 짝수인 경우
            if(Parent == FULL):## 부모가 찬경우
                graph[Depth][State][Parent] = fun(Depth +1 ,EMPTY,State,Parent,N)
                return graph[Depth][State][Parent]
            else:
                graph[Depth][State][Parent] = fun(Depth+1,EMPTY,State,Parent,N) + fun(Depth+1,FULL,State,Parent,N)
                return graph[Depth][State][Parent]
        

sum = fun(0,1,1,1,N)

print(sum)