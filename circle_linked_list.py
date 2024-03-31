class Node():
    def __init__(self):
        self.data = None
        self.link = None


node1 = Node()
node1.data ="A"
node1.link = node1

node2 = Node()
node2.data ="B"
node1.link = node2
node2.link = node1

node3 = Node()
node3.data ="C"
node2.link = node3
node3.link = node1

node4 = Node()
node4.data = "D"
node3.link = node4
node4.link = node1

current = node1
print(current.data)

while(current.link!= node1):
    current = current.link
    print(current.data)



newNode = Node()
newNode.data = "HJ"

node2.link = newNode
newNode.link = node3

node4.link = node2
del(node1)

current = node2
print(current.data)

while(current.link!= node2):
    current = current.link
    print(current.data)
