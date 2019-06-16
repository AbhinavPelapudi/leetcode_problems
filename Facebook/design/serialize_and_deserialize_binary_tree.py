# Serialize and Deserialize Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    def serialize(self, root):
        vals = []
        def pre_order(node):
            if not node:
                vals.append('#')
                return 
            vals.append(str(node.val))
            pre_order(node.left)
            pre_order(node.right)
        pre_order(root)
        return " ".join(vals)

    def deserialize(self, data):
        if not data: 
            return
        data = deque(data.split(' '))
        def pre_order():
            if data:
                current = data.popleft()
            if current == '#':
                return None
            root = TreeNode(int(current))
            root.left = pre_order()
            root.right = pre_order()
            return root
        return pre_order()
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))