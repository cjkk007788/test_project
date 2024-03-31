class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start

    if current.link == None:
        return
    
    print(current.data, end='')
    while current.link!= start:
        current = current.link
        print(current.data,end= '')

    print()
    
def insertNode(findNode,data):

    global pre,head,current, memory

    if head.data == findNode:
        newNode = Node()
        newNode.data = data
        newNode.link = head

        last = head
        while (last.link != head):
            last = last.link
        
        last.link = newNode()
        head = newNode
        return
    
    current = head

    while(current.link != head):
        pre = current
        current = current.link

        if(current.data == findNode):
            
            newNode = Node()
            newNode.data = data
            newNode.link = current
            pre.link = newNode
            return
        
    newNode =Node()
    newNode.data = data
    current.link = newNode
    newNode.link = head

def deleteNode(findNode):

    global pre, current,head,memory

    current = head

    if current.data == findNode:

        last = head

        while(last.link != head):
            last = last.link
        
        last.link = head.link
        head = head.link
        del(current)
        return
    
    while(current.link!= head):

        pre= current
        current = current.link

        if(current.data == findNode):
            pre.link = current.link
            del(current)

        return
    
def searchNode(findNode):
    
    global head,pre,current,memory

    current = head
    if current.data == findNode:
        return current
    while(current.link != head):
        current = current.link
        if(current.data == findNode):
            return current
    return Node()





memory = []
head,current,pre = None,None,None
dataArray = ["다현","정연","쯔위","사나","지효"]

if __name__ == "__main__":

    node = Node()
    node.data = dataArray[0]
    head = node
    node.link =head
    memory.append(node)

    
    for data1 in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data1
        pre.link = node
        node.link = head
        memory.append(node)

    printNodes(head)

    insertNode("정연","준규")

    
    printNodes(head)
