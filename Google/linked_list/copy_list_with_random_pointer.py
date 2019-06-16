# Copy List with Random Pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        new_node = Node(head.val, None, None)
        new_head = new_node
        current = head
        seen = {}
        seen[new_node.val] = new_node
        while current:
            if current.next:
                seen[current.next.val] = seen.get(current.next.val, Node(current.next.val, None, None)) 
                new_node.next = seen[current.next.val]
            if current.random:
                seen[current.random.val] = seen.get(current.random.val, Node(current.random.val, None, None)) 
                new_node.random = seen[current.random.val] 
            new_node = new_node.next
            current = current.next
        return new_head