"""
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

s = "anagram"

t = "nagaram"

s_freq = {
    a:3,
    n:1,
    g:1,
    r:1, 
    m:1
}
t_freq = {
    a:3,
    n:1,
    g:1,
    r:1, 
    m:1
}

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_freq = {}
        t_freq = {}
        
        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1
            
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1
        return s_freq == t_freq
            