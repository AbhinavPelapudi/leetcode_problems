class Solution:
    def decodeString(self, s: str) -> str:
        stack = [['', 1]]
        num = ''
        for char in s:
            if char.isdigit():
                num += char
            elif char == '[':
                stack.append(['', int(num)])
                num = ''
            elif char == ']':
                c, n = stack.pop()
                stack[-1][0] += c * n
            else:
                stack[-1][0] += char
        return stack[0][0]