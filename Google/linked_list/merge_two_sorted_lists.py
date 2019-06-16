# Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        head = None
        current = None
        while l1 and l2:
            if l1.val < l2.val:
                new_node = ListNode(l1.val)
                if not current:
                    head = new_node
                    current = new_node
                    l1 = l1.next
                    continue
                current.next = new_node
                current = new_node
                l1 = l1.next
            else:
                new_node = ListNode(l2.val)
                if not current:
                    head = new_node
                    current = new_node
                    l2 = l2.next
                    continue
                current.next = new_node
                current = new_node
                l2 = l2.next
        if l1:
            current.next = l1
        if l2:
            current.next = l2
            
        return head