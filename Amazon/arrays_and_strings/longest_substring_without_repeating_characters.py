# time complexity: O(n)
# space complexity: O(n)
"""
Input: "abcabcbb"
Output: 3 

s = 2
length = 3
max_length = 3

seen 
c
a
b


"""
class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        s = 0 
        seen = {}
        max_length = 0 
        for i in range(len(string)): #iterate through string
            if string[i] in seen: #checks for duplicate chars
                end = seen[string[i]] #end is set to the first ocurrence of duplicated char
                while s <= end: #iterate to remove duplicated char
                    seen.pop(string[s]) #pop until dupe is removed
                    s += 1
            seen[string[i]] = i #add char to seen
            if len(seen) > max_length: #check for length
                max_length = len(seen)
        return max_length #return max length 
            
        