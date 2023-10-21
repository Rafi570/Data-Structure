class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def serialize(root, result):
    if root is None:
        result.append(None)
        return
    result.append(root.value)
    serialize(root.left, result)
    serialize(root.right, result)

def deserialize(data):
    if data[0] is None:
        data.pop(0)
        return None

    root = TreeNode(data[0])
    data.pop(0)
    root.left = deserialize(data)
    root.right = deserialize(data)
    return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

serialized_tree = []
serialize(root, serialized_tree)
print("serialized tree:", serialized_tree)
deserialized_tree = deserialize(serialized_tree)
