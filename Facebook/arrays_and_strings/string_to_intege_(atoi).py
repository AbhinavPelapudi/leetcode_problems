# time: O(n)
# space: O(1)

class Solution:
    def returner(self, result, sign):
        if result < pow(2, 31):
            return result * sign
        if sign > 0:
            return pow(2, 31) - 1
        else: 
            return - pow(2, 31)

    def myAtoi(self, s: str) -> int:
        result = 0
        digit_found = False
        sign = 1
        sign_found = False
        symbols = set([".", '/','!'])
        for char in s:
            if char.isalpha():
                return self.returner(result, sign)
            elif char in symbols:
                return self.returner(result, sign)
            elif char == '+' or char == '-':
                if digit_found:
                    return self.returner(result, sign)
                if sign_found:
                    return self.returner(result, sign)
                if char == "-":
                    sign = -1
                sign_found = True
            elif char == " " and digit_found:
                return self.returner(result, sign)
            elif char == " " and sign_found:
                return self.returner(result, sign)
            elif char.isdigit():
                digit_found = True
                result = (result * 10) + int(char)
        return self.returner(result, sign)