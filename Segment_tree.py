Mx=100000
import math
tree=[0]*(2*Mx)
def create_tree(node,b,e):
    if b==e:
        tree[node]=arr[b]
        return
    Left=node*2
    Right=node*2+1
    Mid=math.floor((b+e) /2)
    create_tree(Left,b,Mid)
    create_tree(Right,Mid+1,e)
    tree[node]=tree[Left]+tree[Right]

def query(node,b,e,i,j):
    if i>e or j<b:
        return 0
    if b>=i and e<=j:
        return tree[node]
    Left = node * 2
    Right = node * 2 + 1
    mid = math.floor((b + e) / 2)
    p1 = query(Left, b, mid, i, j)
    p2 = query(Right, mid + 1, e, i, j)
    return p1+p2

def update(node,b,e,i,newvalue):
    if i>e or i<b:
        return
    if b>=i and e<=i:
        tree[node] = newvalue
        return
    Left=node*2
    Right=node * 2 + 1
    mid=math.floor((b+e)/2)
    update(Left,b,mid,i,newvalue)
    update(Right,mid+1,e,i,newvalue)
    tree[node]=tree[Left]+tree[Right]


if __name__ == "__main__":
    arr=[4,9,3,7,1,0,2]
    create_tree(1,0,6)
    i=query(1,0,6,0,6)
    print(i)
    update(1,0,6,1,40)
    o=query(1,0,6,0,6)
    print(o)
