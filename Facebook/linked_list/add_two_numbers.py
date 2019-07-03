# Add Two Numbers
# time: O(n)
# space: O(n)
"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

carry = 0
new_ll = 7 -> 0 -> 8
           *
(2 -> 4 -> 3)

           *
(5 -> 6 -> 4)


"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        previous = head = None
        while l1 or l2:
            current = None
            l1_val = l1.val if l1 else 0 #get value of l1_val
            l2_val = l2.val if l2 else 0 #get value of l2_val
            summed = l1_val + l2_val #do a sum of both values
            if summed + carry > 9:
                digit = (summed + carry) - 10 #subtract by 10 to get it in ones position
                current = ListNode(digit)
                carry = 1
            else:
                current = ListNode(summed + carry)
                carry = 0
            if l1: #checks if still l1
                l1 = l1.next
            if l2: #checks if still l2
                l2 = l2.next
            if previous: #assign current onto the linked list
                previous.next = current
            if not head: #assgn head
                head = current
            previous = current
        if carry: #get the straggler
            current = ListNode(carry)
            previous.next = current
        return head
            