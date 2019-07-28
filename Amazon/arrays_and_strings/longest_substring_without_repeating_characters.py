class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        s = 0 
        seen = {}
        max_length = 0 
        for i in range(len(string)):
            if string[i] in seen:
                end = seen[string[i]]
                while s <= end:
                    seen.pop(string[s])
                    s += 1
            seen[string[i]] = i
            if len(seen) > max_length:
                max_length = len(seen)
        return max_length
            
        