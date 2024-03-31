class Heap():
    
    def __init__(self):
        self.heap = []
        
    def heapify_bottomup(self):
        n = len(self.heap)-1 ## 맨마지막 노드의 위치
        
        while(True):

            if(n==0):
                break
            data = self.heap[n]
            parent = self.heap[(n-1)//2]            
            if(data<parent):
                self.heap[n],self.heap[(n-1)//2] = self.heap[(n-1)//2],self.heap[n]
                n = (n-1)//2
            else:
                break
    def heapify_top_down(self):

        start = 0
        data = self.heap[start]
        
        
        while(True):
            
            if(start>len(self.heap())-1):
                break
            
            left_child = 2*start+1
            right_child = 2*start+2
            
            if(self.heap[left_child] <= right_child):
                self.heap[start], self.heap[left_child] = self.heap[left_child], self.heap[start]
                start = left_child
            elif(self.heap[left_child] > right_child):
                self.heap[start],self.heap[right_child] = self.heap[right_child],self.heap[start]
                start = right_child

        return
                            

    def heapPush(self,data):
        self.heap.append(data)
        self.heapify()
        
    def heapPop(self):
        value = self.heap[0]
        self.heap[0] = self.heap[len(self.heap())-1] ## 맨 마지막위치의 값을 0에 저장
        del(self.heap[self.heap()-1])

        return value
