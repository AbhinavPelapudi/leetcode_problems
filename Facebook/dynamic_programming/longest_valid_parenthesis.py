class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_val = 0 
        for i in range(len(s)):
            if s[i] == ')':
                if stack[-1] != -1 and s[stack[-1]] == ')' or stack[-1] == -1:
                    stack.append(i)
                    continue
                val = stack.pop()
                max_val = max(i - stack[-1], max_val)
            else:
                stack.append(i)
        return max_val
                