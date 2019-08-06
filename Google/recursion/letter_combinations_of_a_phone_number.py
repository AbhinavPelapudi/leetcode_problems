# Letter Combinations of a Phone Number

"""
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'2': ['a','b','c']
'3': ['d','e','f']
depth = 0, 1, 2
build = cf
result = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        nums = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        all_combos = []
        def get_combos(digits, depth, build):
            if depth == len(digits):
                all_combos.append(build)
                return 
            for i in range(len(nums[digits[depth]])):
                get_combos(digits, depth + 1, build + nums[digits[depth]][i])
        get_combos(digits, 0, '')
        return all_combos