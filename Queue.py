def isQueueFull():

    global SIZE,front,rear,queue

    if(SIZE != rear-1):
        return False
    elif ( SIZE == rear-1 & front ==-1):
        return True
    else: ##(SIZE == rear -1 & front != -1)
        for k in range(front+1,SIZE):
            queue[k-1] = queue[k]
            queue[SIZE-1] = None
            front = front -1
            rear = rear -1
            return False


def isEmpty():
    
    global SIZE,front,rear,queue

    if(front == rear):
        return True
    else:
        False

def enqueue(data):
    global SIZE,front,rear,queue
    if(isQueueFull()):
        print("isFull")
        return None
    
    rear = rear +1
    queue[rear] = data
    
def dequeue():
    
    global SIZE,front,rear,queue

    if(isEmpty()):
        print("isEmpty!")
        return None
    else:
        front = front +1
        data= queue[front]
        queue[front] = None
        return data
def peek():
    
    global SIZE,front,rear,queue
    if(isEmpty()):
        print("isEmpty!")
        return None
    else:
        return queue[front+1]

    

SIZE = 5
queue = [None for _ in range(SIZE)]
rear, front = -1,-1

enqueue("AB")
enqueue("CD")
enqueue("ED")
enqueue("FG")

print(dequeue())

print(peek())