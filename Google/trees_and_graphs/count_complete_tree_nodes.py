# Count Complete Tree Nodes
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

             1(6)
            /   \
           2(3)  3(2)
          / \     /
       (1)4 (1)5 6(1)

"""
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return (left + right) + 1