# Binary Tree Right Side View
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def right_nodes(self, root, stack, max_level, result, all_nodes, prev):
        current = root
        while current:
            if not prev:
                level = 1
            else: 
                level = all_nodes[prev] + 1
            if level > max_level:
                max_level = level
                result.append(current.val)
            stack.append(current)
            all_nodes[current] = level
            prev = current
            current = current.right
            
        return max_level
            
              
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        all_nodes = {}
        stack = []
        level = max_level = 0 
        result = []
        max_level = self.right_nodes(root, stack, max_level, result, all_nodes, None)
        while stack:
            current = stack.pop()
            if current.left:
                max_level = self.right_nodes(current.left, stack, max_level, result, all_nodes, current)
    
        return result
                
                