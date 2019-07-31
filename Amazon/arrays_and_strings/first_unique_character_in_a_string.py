"""
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.


alphabet = [0, 0, 1, e, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
            a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z

"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        alphabet = [0] * 26
        for char in s:
            idx = ord(char) - 97
            alphabet[idx] += 1
        for index, char in enumerate(s):
            idx = ord(char) - 97
            if alphabet[idx] == 1:
                return index
        return -1
            