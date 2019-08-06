# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return
        to_last = {}
        counter = 0
        current = head
        while current:
            counter += 1
            to_last[counter] = current
            current = current.next
        current_node = to_last.get(counter - n)
        if not current_node:
            new_head = head.next
            head.next = None
            return new_head
        current_node.next = current_node.next.next
        return head
        