# Permutation in String
"""
Input: s1 = "ab" s2 = "eidbaooo"
Output: True

builder_dict
b - 1
a - 1

s1_dict
a - 1
b - 1

start = 3

"eidbaooo"

"""


from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        builder_dict = defaultdict(int)
        s1_dict = defaultdict(int)
        for char in s1:
            s1_dict[char] += 1
        start = 0 
        for i in range(len(s2)):
            if s2[i] not in s1_dict:
                builder_dict = defaultdict(int)
                start = i + 1
                continue 
            builder_dict[s2[i]] += 1
            if builder_dict[s2[i]] > s1_dict[s2[i]]:
                while builder_dict[s2[i]] > s1_dict[s2[i]]:
                    builder_dict[s2[start]] -= 1
                    start += 1
            elif builder_dict == s1_dict:
                return True
        return False