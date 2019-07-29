
# Lowest Common Ancestor of a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
                3
               /  \
              5    1
            /  \   / \
           6    2  0  8
               / \
              7   4
paths = {
    3: None, 
    5: 3, 
    1: 3,
    6: 5,
    2: 5, 
    0: 1, 
    7: 2, 
    4: 2, 
    8: 1
}
visited = {5,3}
p = 5
q = 1
"""
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