from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        longest = max_longest = 0
        chars = defaultdict(int)
        start = 0 
        for i in range(len(s)):
            chars[s[i]] += 1
            longest += 1
            while len(chars) > 2:
                chars[s[start]] -= 1
                if not chars[s[start]]:
                    chars.pop(s[start])
                start += 1
                longest -= 1
            max_longest = max(max_longest, longest)
        return max_longest