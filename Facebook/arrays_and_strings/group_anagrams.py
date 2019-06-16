# Group Anagrams
# time: O(n)
# space: O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for char in strs:
            char_sorted = "".join(sorted(char))
            grouped[char_sorted] = grouped.get(char_sorted, []) + [char]
        return list(grouped.values())
        