# time: O(n)
# space: O(n)
"""
Input: ")()())"
Output: 4

max_val = 0 
stack = [-1, 0,]
val = 4

")()())"

"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1] #utilize stack, -1 is used because they are zero based
        max_val = 0 
        for i in range(len(s)): #iterate through strings
            if s[i] == ')': #if ending paren found
                if stack[-1] != -1 and s[stack[-1]] == ')' or stack[-1] == -1: #if previous is not opening bracket
                    stack.append(i)
                    continue
                val = stack.pop()
                max_val = max(i - stack[-1], max_val) #get the distance of matching parens
            else:
                stack.append(i) #add opening parens to stack
        return max_val
                