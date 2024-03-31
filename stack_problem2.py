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
        return None
    else: 
        pdata = stack[top]
        stack[top]= None
        top = top -1
        return pdata
    
def peek():

    global SIZE,top,stack

    if(stackIsEmpty()):
        return None
    else:
        return stack[top]
    
SIZE = 100
stack =[]
top = -1

for i in range(SIZE):
    stack.append(None)


with open("진달래꽃.txt","r",encoding = 'UTF8') as rfp:
    lineAry = rfp.readlines()

    print("------원본-------")
    
    for line in lineAry:
        stackPush(line)
        print(line,end ='')

    
print()
while(True):

    line = stackPop()        
    if(line == None):
        break
        
    ministack = [None for _ in range(len(line))]
    minitop = -1

    for ch in line:
        minitop = minitop +1
        ministack[minitop] = ch
            
    while(True):
        if minitop == -1:
            break
        else:
            print(ministack[minitop],end ='')
            minitop = minitop -1

