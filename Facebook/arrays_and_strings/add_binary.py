# Add Binary
# time: O(n)
# space: O(n)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        end_a, end_b, carry = len(a) - 1, len(b) - 1, 0
        new_digit = ''
        while end_a >= 0 and end_b >= 0:
            if int(a[end_a]) + int(b[end_b]) > 1:
                new_digit += str(carry)
                carry = 1
            elif int(a[end_a]) + int(b[end_b]) + carry > 1:
                new_digit += '0'
                carry = 1
            else:
                new_digit += str(int(a[end_a]) + int(b[end_b]) + carry)
                carry = 0 
            end_a -= 1
            end_b -= 1
        while end_a >= 0:
            if int(a[end_a]) + carry > 1:
                carry = 1
                new_digit += '0'
            else:
                new_digit += str(int(a[end_a]) + carry)
                carry = 0 
            end_a -= 1
        while end_b >= 0:
            if int(b[end_b]) + carry > 1:
                carry = 1
                new_digit += '0'
            else:
                new_digit += str(int(b[end_b]) + carry)
                carry = 0 
            end_b -= 1
        if carry:
            new_digit += str(carry)
        digit = ''
        for i in range(len(new_digit) - 1, - 1, -1):
            digit += new_digit[i]
        return digit
