# Group Anagrams
# time: O(n klogk)
# space: O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for char in strs: #iterate over strings
            char_sorted = "".join(sorted(char)) #sort chars
            grouped[char_sorted] = grouped.get(char_sorted, []) + [char] #add chars to correct key
        return list(grouped.values()) #return the values as a list
        