# Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        seen_parens = []
        validator = {
            ')':'(',
            '}': '{',
            ']': '['
        }
        for char in s:
            if char in validator:
                if not len(seen_parens):
                    return False
                previous = seen_parens.pop()
                if validator[char] != previous:
                    return False
            else:
                seen_parens.append(char)
        if len(seen_parens): 
            return False
        return True