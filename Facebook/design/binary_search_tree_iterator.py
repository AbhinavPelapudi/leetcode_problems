# time: O(n)
# O(n)

# Binary Search Tree Iterator
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""

        7
      /   \
     3     15
          /  \
        9     20
iteration 1:
stack = [7,3] 
next -> 3

iteration 2:
stack = [15, 9]
next -> 7

iteration 3:
stack = [20]
next -> 9
next -> 15
next -> 20


"""

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = self.re_pop(root) #initialization
    
    def re_pop(self, root) -> None:
        if not root: # if no value just return empty array
            return []
        stack = [root] #start with a stack
        current = root #use current as a means to move through tree
        while current:
            if current.left: #add all values to the left of of the root
                stack.append(current.left)
            current = current.left
        return stack #return stack
    
    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.stack:
            top = self.stack.pop() #pop off top
            if top.right: #if right is found
                self.stack = self.stack + self.re_pop(top.right) #add everying to the left of right
            return top.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()