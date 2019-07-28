# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0 
            left = dfs(root.left)
            right = dfs(root.right)
            temp_sum = (root.val + left + right)
            
            
        dfs.res = 0  
        