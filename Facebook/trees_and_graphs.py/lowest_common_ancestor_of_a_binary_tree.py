# Lowest Common Ancestor of a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def get_path(self, root):
        q = deque()
        path = {root: None}
        q.append(root)
        while q:
            current = q.pop()
            if current.left:
                q.append(current.left)
                path[current.left] = current
            if current.right:
                q.append(current.right)
                path[current.right] = current
        return path

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        paths = self.get_path(root)
        visited = set()
        current = p
        while current:
            visited.add(current)
            current = paths[current]
        current = q
        while current:
            if current in visited:
                return current
            current = paths[current]
            