import random

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

memory = []
root = None



dataAry = ['바나나 우유','레쓰빈 커피','츄파츕스','도시락','삼다수','코카콜라','삼각김밥']

sellAry = [ random.choice(dataAry) for _ in range (20) ]

node = TreeNode()
node.data = sellAry[0]
root = node
memory.append(node)

for sellproduct in sellAry[1:]:

    current = root
    node = TreeNode()
    node.data = sellproduct

    while True:
        if(current.data == sellproduct):
            break
        if(current.data <sellproduct):
            if(current.right == None):
                current.right = node
                memory.append(node)
                break
            else:
                current = current.right
                continue
        
        if(current.data > sellproduct):
            if(current.left == None):
                current.left = node
                memory.append(node)
                break
            else:
                current = current.left
                continue


preorder(root)