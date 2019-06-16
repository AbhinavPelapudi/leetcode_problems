# Merge k Sorted Lists

# Definition for singly-linked list.
from queue import PriorityQueue
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = PriorityQueue()
        prev = head = None
        for ll in lists:
            if ll:
                q.put((ll.val, id(ll), ll))
        while not q.empty():
            _, _, current = q.get()
            if not head:
                head = current
            if current.next:
                q.put((current.next.val, id(current.next), current.next ))
            if prev:
                prev.next = current
            prev = current
        return head
                
            
            