from typing import Optional, List

class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        q = [(root, str(root.val))]
        paths = []

        while q:
            node, path = q.pop(0)
            
            if not node.left and not node.right:
                paths.append(path)
            
            if node.left:
                q.append((node.left, path + "->" + str(node.left.val)))
            
            if node.right:
                q.append((node.right, path + "->" + str(node.right.val)))
        
        return paths

# Example usage:
# Constructing a binary tree: 
#     1
#    / \
#   2   3
#  / \ / \
# 4  5 6  7

def insertLevelOrder(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i])
        root = temp
        
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    
    return root

arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
root = insertLevelOrder(arr, None, 0, n)

solution = Solution()
paths = solution.binaryTreePaths(root)
print(paths)  # Output: ["1->2->4", "1->2->5", "1->3->6", "1->3->7"]
