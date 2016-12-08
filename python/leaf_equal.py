from collections import deque
class node():
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

class Solution():
    

sol = Solution()
tree = node(1)
tree.left = node(3)
tree.right = node(4)

sol.traverse(tree, [])






