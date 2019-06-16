class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x *= -1
            new_num = self.reverse_vals(x)
            return -new_num
        return self.reverse_vals(x)

    def reverse_vals(self, x: int) -> int: 
        new_num = 0
        while x:
            remainder = x % 10
            x -= remainder
            x = x // 10
            new_num = (new_num * 10) + remainder
        return 0 if new_num > pow(2, 31) -1 else new_num
        