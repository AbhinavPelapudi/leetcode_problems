from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        start = 0
        current_string = max_string = 0
        for i in range(len(s)):
            current_string += 1
            chars[s[i]] += 1
            if len(chars) > k:
                while len(chars) > k:
                    char = s[start]
                    chars[char] -= 1
                    if chars[char] == 0:
                        chars.pop(char)
                    start += 1
                    current_string -= 1
            if current_string > max_string:
                max_string = current_string
        return max_string