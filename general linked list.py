class Node():
    def __init__(self):
        self.data =None
        self.link = None

def insert_Data(findData,insertData):

    global memory,head,pre,current

    if head.data == findData :

        newnode = Node()
        newnode.data = insertData
        newnode.link = head
        head = newnode
        return
    
    current = head

    while (current.link != None):
        pre = current
        current = current.link

        if current.data == findData :
            newnode = Node()
            newnode.data = insertData
            pre.link = newnode
            newnode.link = current
            return
        
    newnode = Node()
    newnode.data = insertData
    current.link = newnode
        
    return



    return
def delete_Data(findData):
    global memory,head,pre,current

    current = head

    if head.data == findData:
        head = head.link
        del(current)

    while(current.link!=None):
        pre = current
        current = current.link
        
        if current.data == findData:
            
            pre.link = current.link
            del(current)
            return
            
        

def print_Node(start):

    current = start
    if (start == None): 
        return
    while(current != None):
        print(current.data)
        current = current.link


memory = []

head,current,pre = None,None,None

dataArray = ["A","B","C","D","E"]


if __name__=="__main__":

##1번 노드 삽입
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)
def searchNode(findData):

    global current,memory,head,pre

    current = head
    if(head.data == findData):
        return head
    while current.link != None:
        pre = current
        current = current.link
        if(current.data == findData):
            return current
        
    return Node() ## 빈 노드 반환

print_Node(head)

insert_Data("L","F")
insert_Data("A","G")
delete_Data("D")
delete_Data("A")

print_Node(head)
