class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def topView(root):
    dataL = []
    dataR = [root.info]
    left_node = root.left
    right_node = root.right
    while left_node or right_node:
        if left_node:
            dataL.append(left_node.info)
            left_node = left_node.left
        if right_node:
            dataR.append(right_node.info)
            right_node = right_node.right

    for x in range(len(dataL), 0, -1):
        print(dataL[x-1], end=" ")
    for x in range(len(dataR)):
        print(dataR[x], end=" ")


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)