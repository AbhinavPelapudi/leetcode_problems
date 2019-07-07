# Find Peak Element
"""
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5


[1,2,1,3,5,6,4]
   *
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        for i in range(len(nums)):
            if i == 0:
                if nums[i] > nums[i + 1]:
                    return i
            elif i == len(nums) - 1:
                if nums[i] > nums[i - 1]:
                    return i
            else:
                if nums[i] > nums[i + 1] and nums[i] > nums[i -1]:
                    return i