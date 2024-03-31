def isQueueFull():

    global SIZE,front,rear,queue

    if( (rear +1) % SIZE == front):
        return True
    else : False

def isQueueEmpty():
    
    global SIZE,front,rear,queue
    if ( rear == front ):
        return True
    else :
        return False
    
def enQueue(data):
    global SIZE,front,rear,queue

    if(isQueueFull()):
        print("is fulled")
        return None
    else:
        rear = (rear + 1) % SIZE
        queue[rear] = data

def deQueue():

    global SIZE,front,rear,queue


    if(isQueueEmpty()):
        print("is empty")
        return None
    else:
        front = (front +1) % SIZE
        data = queue[front]
        queue[front] = None
        return data

def peek():

    global SIZE,front,rear,queue
    if(isQueueEmpty()):
        print("isEmpty")
        return None
    else:
        return queue[front +1 ]
    

