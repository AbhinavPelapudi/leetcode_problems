# Valid Palindrome II
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def checkPalindrome(l,r):
            return s[l:r+1] == s[l:r+1][::-1]
        
        l,r = 0,len(s)-1
        while l <= r:
            if s[l] != s[r]:
                return checkPalindrome(l+1,r) or checkPalindrome(l,r-1)
            l,r = l+1,r-1
        return True