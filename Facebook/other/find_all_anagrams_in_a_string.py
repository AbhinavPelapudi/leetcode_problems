# Find All Anagrams in a String
"""
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

p_chars 
a - 1
b - 1
c - 1

start = 6
a_chars 
b - 1
a - 1
c - 1



   *
"cbaebabacd"

result = [0, 6]
"""
from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_chars = defaultdict(int)
        a_chars = defaultdict(int)
        for char in p:
            p_chars[char] += 1
        result = []
        start = 0 
        for i in range(len(s)):
            if s[i] not in p_chars:
                start = i + 1
                a_chars = defaultdict(int)
                continue
            a_chars[s[i]] += 1
            if a_chars[s[i]] > p_chars[s[i]]:
                while a_chars[s[i]] > p_chars[s[i]]:
                    a_chars[s[start]] -= 1
                    start += 1
            elif a_chars == p_chars:
                result.append(start)
                a_chars[s[start]] -= 1
                start += 1
        return result
            