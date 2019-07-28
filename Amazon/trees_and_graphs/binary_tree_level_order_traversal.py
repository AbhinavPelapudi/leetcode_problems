# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        results = [[root.val]]
        def traversal(queue):
            child_queue = []
            child_queue_values = []
            if not queue:
                return
            for node in queue:
                if node.left:
                    child_queue.append(node.left)
                    child_queue_values.append(node.left.val)
                if node.right:
                    child_queue.append(node.right)
                    child_queue_values.append(node.right.val)
            if child_queue_values:
                results.append(child_queue_values)
            traversal(child_queue)
        traversal([root])
        return results