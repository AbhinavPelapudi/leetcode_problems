# time: O(s * k)
# space: O(k)
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        chars = defaultdict(int) #set defaultdict
        start = 0
        current_string = max_string = 0
        for i in range(len(s)): #iterate over string
            current_string += 1 #tracks length of the current string
            chars[s[i]] += 1 #increases frequency of char
            if len(chars) > k: #if length of chars is greater than k that means that the string needs to be cut
                while len(chars) > k: #proceed to shorten the front of the window
                    char = s[start]
                    chars[char] -= 1
                    if chars[char] == 0:
                        chars.pop(char)
                    start += 1 #increase the front
                    current_string -= 1 #shorten the string
            if current_string > max_string: #simple comparison
                max_string = current_string
        return max_string #return max_string
