class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        start = 0
        end = len(s) - 1
        s = s.lower() #lower all chars
        while start < end:
            if not s[start].isalpha() and not s[start].isdigit(): #keep going until you find a digit or a alpha
                start += 1
                continue
            if not s[end].isalpha() and not s[end].isdigit(): #keep going until you find a digit or a alpha
                end -= 1
                continue
            if s[start] != s[end]: #if not equal return false
                return False
            start += 1
            end -= 1
        return True