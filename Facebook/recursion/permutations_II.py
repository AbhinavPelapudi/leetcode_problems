# Permutations II
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        all_chars_except_last = nums[:-1]
        last_char = nums[-1]
        all_perms_except_last = self.permuteUnique(all_chars_except_last)
        result = []
        for all_perms in all_perms_except_last:
            for i in range(len(all_perms) + 1):
                perms = all_perms[:i] + [last_char] + all_perms[i:]
                if perms not in result:
                    result.append(perms)
        return result
        