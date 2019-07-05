# Convert Binary Search Tree to Sorted Doubly Linked List

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

        4
       /  \
      2    5
    /  \
   1    3

stack = []
node = 4

stack = [4,2]
node = 1
head = 1
prev = 1

stack = [4, 3]
node = 3
head = 1
prev = 2

1 -> 2
  <-

stack = [4]
node = 3
head = 1
prev = 3

1 -> 2 -> 3
  <-   <-

stack = []
node = 4
head = 1
prev = 4

1 -> 2 -> 3 -> 4
  <-   <-   <-

stack = [5]
node = 5
head = 1
prev = 4

1 -> 2 -> 3 -> 4 -> 5
  <-   <-   <-   <-

"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return
        head = None
        stack, node = [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if head:
                node.left, prev.right, prev = prev, node, node
            else:
                head = prev = node
            node = node.right
        head.left, prev.right = prev, head
        return head