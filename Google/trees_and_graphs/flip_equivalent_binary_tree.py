# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
                    1
                   / \
                 3     2
                  \   / \
                   6  4  5  
                        / \     
                       7   8


                1
               / \ 
             3     2
              \   / \
               6 4   5
                    / \
                   8   7


q = [[7, 7], [8, 8]]
node1 = 5
node2 = 5
"""
from collections import deque
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 and not root2 or root2 and not root1:return False
        if not root1 and not root2: return True
        if root1.val != root2.val: return False
        q = deque()
        q.append([root1, root2])
        while q:
            node1, node2 = q.popleft()
            if not node1.left and not node1.right and not node2.left and not node2.right:
                continue
            if node1.left and node2.left and node1.right and node2.right:
                if node1.left.val == node2.left.val and node1.right.val == node2.right.val:
                    q.append([node1.left, node2.left])
                    q.append([node1.right, node2.right])
                elif node1.left.val == node2.right.val and node2.left.val == node1.right.val:
                    node1.left, node1.right = node1.right, node1.left
                    q.append([node1.left, node2.left])
                    q.append([node1.right, node2.right])
                else:
                    return False
            elif not node1.right and not node2.left and node1.left and node2.right:
                if  node1.left.val == node2.right.val:
                    node1.left, node1.right = node1.right, node1.left
                    q.append([node1.right, node2.right])
                else:
                    return False
            elif not node1.left and not node2.right and node1.right and node2.left:
                if  node1.right.val == node2.left.val:
                    node1.left, node1.right = node1.right, node1.left
                    q.append([node1.left, node2.left])
                else:
                    return False
            elif not node1.left and not node2.left and node1.right and node2.right:
                if node1.right.val == node2.right.val:
                    q.append([node1.right, node2.right])
                else:
                    return False
            elif not node1.right and not node2.right and node1.left and node2.left:
                if node1.left.val == node2.left.val:
                    q.append([node1.left, node2.left])
                else:
                    return False
            else:
                return False
        return True
                    
                