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
    
SIZE = 7
front, rear = 0,0

queue = [None for _ in range(7)]

def cal_time(queue):
    global front,rear,SIZE
    sum_time = 0
    for k in range(front+1, rear+1):
        sum_time = sum_time + queue[k][1]
    
    print(list(queue))
    print("당신의 총 대기 시간은 {}분 입니다".format(sum_time))


user1 = ("사용",9)
user2 = ("고장",3)
user3 = ("환불",4)
user4 = ("고장",3)
user5 = ("사용",9)


enQueue(user1)
enQueue(user2)
enQueue(user3)
enQueue(user4)
enQueue(user5)

cal_time(queue)