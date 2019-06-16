# Flatten Binary Tree to Linked List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        current = root
        stack = []
        while current:
            if current.right:
                stack.append(current.right)
                current.right = None
            if current.left:
                current.right = current.left
                current.left = None
            if not current.left and not current.right and stack:
                new_right = stack.pop()
                current.right = new_right
                
            current = current.right
 