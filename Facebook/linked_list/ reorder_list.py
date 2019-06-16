# Reorder List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        double_ll = []
        current = head
        prev = None
        while current:
            double_ll.append([current, prev])
            prev = current
            current = current.next
        double_ll = double_ll[(len(double_ll) // 2) + 1:]
        current = head
        while current:
            if double_ll:
                new_next, parent = double_ll.pop()
                next_node = current.next
                parent.next = None
                current.next = new_next
                new_next.next = next_node
                current = new_next.next
                continue
            current = current.next