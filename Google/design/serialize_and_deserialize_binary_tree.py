# time: O(n)
# space: O(n)

"""
    1
   / \
  2   3
     / \
    4   5
serialize(root):
vals = ['1', '2', '#', '#', '3', '4', '#', '#', '5]
returns '1 2 # # 3 4 # # 5'
deserialize(data):
Iteration 1:
data = ['2', '#', '#', '3', '4', '#', '#', '5]
    1
Iteration 2:
data = ['3', '4', '#', '#', '5]
    1
   /  
  2    
Iteration 3:
data = ['4', '#', '#', '5]
    1
   /  \
  2    3
Iteration 4:
data = ['#', '#', '5]
    1
   / \
  2   3
     / 
    4 
Iteration 5:
data = []
    1
   / \
  2   3
     /  \
    4     5
"""

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
        def pre_order(node): #do a preorder search
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
        data = deque(data.split(' ')) # split the data being passed through
        def pre_order():
            if data:
                current = data.popleft() #pop data
            if current == '#': #use this to move up the tree
                return None
            root = TreeNode(int(current)) #set root
            root.left = pre_order() #go as far left as possible
            root.right = pre_order() #then go as far right as possible
            return root #this will be assign to previous stacks to build tree
        return pre_order()
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))