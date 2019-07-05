"""
Input: [23, 2, 6, 4, 7],  k=6
Output: True

[23, 2, 6, 4, 7]

mod_k = 0
mods = {0: -1, 5: 0, 1: 1}
mod_k = (23 + 0) % 6 => 5
mod_k = (2 + 5) % 6 => 1
mod_k = (6 + 1) % 6 => 1
mod_k = (4 + 1) % 6 => 1
"""
# Continuous Subarray Sum
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mods = {0: -1}
        mod_k = 0 
        if k == 0:
            return any(nums[i] == 0 and nums[i + 1] == 0 for i in range(len(nums) - 1))
        for i, n in enumerate(nums):
            mod_k = (n + mod_k) % k
            if mod_k in mods and i - mods[mod_k] > 1:
                return True
            if mod_k not in mods:
                mods[mod_k] = i
        return False