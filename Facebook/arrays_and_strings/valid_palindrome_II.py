# Valid Palindrome II
class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end, counter= 0, len(s) - 1, 0
        while start < end:
            if s[start] != s[end]:
                if counter > 0:
                    return False
                if end - start >= 3:
                    if s[start + 1] == s[end] and s[start + 2] == s[end -1]:
                        start += 1
                        counter += 1
                    elif s[start] == s[end - 1] and s[start + 1] == s[end - 2]:
                        end -= 1
                        counter += 1
                    else:
                        return False
                else:
                    if s[start + 1] == s[end]:
                        start += 1
                        counter += 1
                    elif s[start] == s[end - 1]:
                        end -= 1
                        counter += 1
                    else:
                        return False
            start += 1
            end -= 1
        return True