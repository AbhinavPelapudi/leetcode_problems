# Permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        all_chars_except_last = nums[:-1]
        last_char = nums[-1]
        
        permuation_of_all_chars_except_last = self.permute(all_chars_except_last)
        result = []
        for permuation_of_all in permuation_of_all_chars_except_last:
            for i in range(len(permuation_of_all) + 1):
                perm = permuation_of_all[:i] + [last_char] + permuation_of_all[i:]
                result.append(perm)
        return result
        