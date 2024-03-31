class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def preorder(node):
    
    if(node == None):
        return
    
    print(node.data)
    preorder(node.left)
    preorder(node.right)

def inorder(node):

    if(node ==None):
        return
    
    inorder(node.left)
    print(node.data)
    inorder(node.right)

def postorder(node):

    if(node == None):
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data)

memory = []
root = None

nameAry = ["블랙핑크","레드벨벳","에이핑크","걸스데이","트와이스","마마무"]

node = TreeNode()
node.data = nameAry[0]
root = node

memory.append(node)


for name in nameAry[1:]:

    node = TreeNode()
    node.data =name
    current = root

    while True:

        if(current.data < node.data):
            if(current.right == None):
                current.right = node
                break
            else:
                current = current.right
                continue
        else:
            if(current.left == None):
                current.left = node
                break
            else:
                current = current.left
                continue

preorder(root)

findName ="마마무"

current = root

while True:
    if(current.data == findName):
        print("찾았다. 마마무")
        break
    elif(current.data < findName):
        if(current.data == None):
            print("없음")
            break
        current = current.right
    else:
        if(current.data == None):
            print("없음")
            break
        current = current.left
        

deleteName ="마마무"
current = root
parent = None

while True:

    if(current.data == deleteName):

        if (current.left == None and current.right == None):
            if(current == parent.right):
                parent.right ==None
            else:
                parent.left == None
            print("{}가 삭제됨".format(current.data))
            del(current)
            

        elif(current.left != None and current.right == None):
            ##자식이 하나 있는데 왼쪽만 있는 경우
            if(current == parent.right):
                parent.right = current.left
            else:
                parent.left =current.left
            print("{}가 삭제됨".format(current.data))
            del(current)

            
        elif(current.left == None and current.right != None):
            ##자식이 하나 있는데 왼쪽만 있는 경우
            if(current == parent.right):
                parent.right = current.right
            else:
                parent.left =current.right
                
            print("{}가 삭제됨".format(current.data))
            del(current)

    elif(deleteName < current.data):
        if (current.left == None):
            print("없음")
            break
        parent = current
        current = current.left
        continue
    else:
        if current.right ==None:
            print("없음")
            parent = current
        current = current.right
        continue

