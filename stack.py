def stackIsFull():
    global SIZE,top,stack
    
    if(top >= SIZE-1):
        return True
    
    return False

def stackIsEmpty():
    global SIZE,top,stack
    
    if(top ==-1):
        return True
    else:
        return False


def stackPush(data):

    global SIZE,top,stack
    
    if (stackIsFull()):
        print("Stack is already fulled")
        return 
    else:
        top = top+1
        stack[top] = data

def stackPop():
    global SIZE,top,stack
    if(stackIsEmpty()):
        print("Stack is empty!")
        return
    else: 
        pdata = stack[top]
        stack[top]= None
        top = top -1
        return pdata
    
def peek():

    global SIZE,top,stack

    if(stackIsEmpty()):
        print("stack is empty!")
        return None
    else:
        return stack[top]
    
SIZE = 5
stack =[]
top = -1

for i in range(SIZE):
    stack.append(None)

stackPush("A")
stackPush("B")
stackPush("C")
stackPush("D")

while(stackIsEmpty()!=True):
    print(stackPop())