import random

class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


bookAry =[['어린왕자','생택쥐베리'],['이방인','알베르카뮈'],['부활','톨스토이'],
          ['신곡','단테'],['돈키호테','세르반테스'],['동물농장','조지오웰'],['데미안','헤르만헤세'],
          ['파우스트','괴테'],['대지','펄벅']
          ]
def preorder(node):
    
    if(node ==None):
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)
    
def searchTree(root,findData):

    current = root

    while(True):
        if (current.data == findData):
            return current
        if(current.data < findData):
            if(current.right == None):
                return None
            else:
                current = current.right
        else:
            if(current.left == None):
                return None
            else:
                current = current.left

random.shuffle(bookAry)

memory = []
rootbook = None
rootAuth = None

##책이름으로 먼저 만드는 트리

node = TreeNode()
node.data =bookAry[0][0]
rootbook = node
memory.append(rootbook)

for book in bookAry[1:]:

    current = rootbook
    node = TreeNode()
    node.data = book[0]

    while(True):

        if(current.data < node.data):
            if(current.right == None):
                current.right = node
                break
            current = current.right
            continue
        else:
            if(current.left == None):
                current.left =node
                break
            current = current.left
            continue
    memory.append(node)

    ##작가이름 트리

node = TreeNode()
node.data = bookAry[0][1]
rootAuth = node
memory.append(rootAuth)

for book in bookAry[1:]:

    current = rootAuth
    node = TreeNode()
    node.data = book[1]

    while(True):

        if(current.data < node.data):
            if(current.right == None):
                current.right = node
                break
            current = current.right
            continue
        else:
            if(current.left == None):
                current.left =node
                break
            current = current.left
            continue
    memory.append(node)
        

##작가이름 책이름 검색

while(True):
    bookOrAuth = input("책검색 --> 1 or 작가검색-->2 " )
    if(bookOrAuth == '1' or bookOrAuth == '2' ):
        break
    else:
        print("1 or 2만 입력하세요!")
        continue

if ( bookOrAuth == '1' ):
    print("책 이름으로 검색 합니다")
    FindData = input("책이름 입력하세요--> ")

    result = searchTree(rootbook,FindData)
    if(result == None):
        print("없음")
    else:
        print("책이름{}".format(result.data))

if ( bookOrAuth =='2' ):
    print("작가 이름으로 검색 합니다")
    FindData = input("작가 이름을 입력하세요--> ")

    result = searchTree(rootAuth,FindData)
    if(result == None):
        print("없음")
    else:
        print("작가이름 {}".format(result.data))
