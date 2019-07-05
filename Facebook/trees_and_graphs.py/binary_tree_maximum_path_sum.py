# Binary Tree Maximum Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Input: [-10,9,20,null,null,15,7]

        -10(34)
        / \
    (9)9  20(42)
         /  \
        15   7

Output: 42



self.ans = -float('inf')


"""
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans = - float('inf')
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            temp_path = root.val + left + right
            max_path = root.val + max(left, right, 0)
            self.ans = max(temp_path, max_path, self.ans)
            return max_path
        helper(root)
        return self.ans