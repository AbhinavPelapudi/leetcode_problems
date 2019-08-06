# Definition for singly-linked list.
from queue import PriorityQueue
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
q = []
prev =Node(4)
head = Node(1)
current = Node(6)
"""
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
            
            