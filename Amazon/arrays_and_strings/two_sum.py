"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


seen = {7, }

[2,7,11,15] target = 9
   *



"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                return [seen[nums[i]], i]
            poss = target - nums[i]
            seen[poss] = i