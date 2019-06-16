# Binary Tree Paths
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        def get_paths(node, paths):
            if not node:
                return
            if not node.left and not node.right:
                paths += [str(node.val)]
                result.append('->'.join(paths))
                return
            get_paths(node.left, paths + [str(node.val)])
            get_paths(node.right, paths + [str(node.val)])
        get_paths(root, [])
        return result
            