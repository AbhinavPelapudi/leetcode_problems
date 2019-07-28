# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        previous = head = None
        while l1 or l2:
            current = None
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            summed = l1_val + l2_val
            if summed + carry > 9:
                digit = (summed + carry) - 10
                current = ListNode(digit)
                carry = 1
            else:
                current = ListNode(summed + carry)
                carry = 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if previous:
                previous.next = current
            if not head:
                head = current
            previous = current
        if carry:
            current = ListNode(carry)
            previous.next = current
        return head