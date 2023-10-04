class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        
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

def levelorder(root):
    q=[root]
    l=[]
    while q:
        node=q.pop(0)
        l.append([node.info])
        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)
    print(l)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelorder(tree.root)
"""======================================================================================================================================================================================================================="""
#another code BFS level order traversal
import collections
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        
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

def levelorder(root):
    if root==None:
            return []
        
    res=[]
    q=collections.deque()
    q.append(root)
    while q:
        ql=len(q)
        l=[]
        for i in range(ql):
            node=q.popleft()
            if node:
                l.append(node.info)
                q.append(node.left)
                q.append(node.right)
            if l:
                res.append(l)
    print(res)

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelorder(tree.root)
