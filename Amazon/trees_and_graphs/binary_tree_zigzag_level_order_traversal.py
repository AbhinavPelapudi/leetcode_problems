# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
    3
   / \
  9  20
    /  \
   15   7

[
  [3],
  [20,9],
  [15,7]
]

s1 = [7, 15]
s2 = [9]
results = [[3], [20, 9], [15, 7]]
level = [20, 9]
current = 3


"""
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return
        s1 = [root]
        s2 = []
        results = []
        while s1 or s2:
            level = []
            while s1:
                current = s1.pop()
                if current.left:
                    s2.append(current.left)
                if current.right:
                    s2.append(current.right)
                level.append(current.val)
            if level:
                results.append(level)
            level = []
            while s2:
                current = s2.pop()
                if current.right:
                    s1.append(current.right) 
                if current.left:
                    s1.append(current.left)
                level.append(current.val)
            if level:
                results.append(level)
        return results
                