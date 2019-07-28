# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isSymmetric(self, root):
        if not root:
            return True
        queue = []
        queue.append(root)
        while queue:
            children_queue = []
            start = 0 
            end = len(queue) - 1
            while start <= end:
                if queue[start].left and queue[end].right:
                    if queue[start].left.val != queue[end].right.val:
                        return False
                elif queue[start].left and not queue[end].right:
                    return False
                elif not queue[start].left and queue[end].right:
                    return False

                if queue[start].right and queue[end].left:
                    if queue[start].right.val != queue[end].left.val:
                        return False
                elif queue[start].right and not queue[end].left:
                    return False
                elif not queue[start].right and queue[end].left:
                    return False  
 
                start += 1
                end -= 1
            for node in queue:
                if node.left:
                    children_queue.append(node.left)
                if node.right:
                    children_queue.append(node.right)
            
            queue = children_queue    

        return True