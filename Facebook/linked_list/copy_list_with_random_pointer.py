#  Copy List with Random Pointer
# time: O(n)
# space: O(n)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


1(next = 2
random = 2) -> 2(next = None
random = 2) -> None


current = 1, 2
copy_node = 1, 2
seen = {
    1: Node(1),
    2: Node(2)
    }


"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        new_node = Node(head.val, None, None) #initial copy of head
        new_head = new_node
        current = head
        seen = {}
        seen[new_node.val] = new_node #using values to check for visited
        while current:
            if current.next:
                seen[current.next.val] = seen.get(current.next.val, Node(current.next.val, None, None)) #get or creates new node
                new_node.next = seen[current.next.val] # continues copy
            if current.random:
                seen[current.random.val] = seen.get(current.random.val, Node(current.random.val, None, None)) #get or creates new node
                new_node.random = seen[current.random.val] 
            new_node = new_node.next #move through list copy
            current = current.next #move through original list
        return new_head
        