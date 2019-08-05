"""
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
[-2,1,-3,4,-1,2,1,-5,4], 6
                     *
max_nums = 4
max_sum = 6
c_sum = 5
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = max(nums)
        if max_num < 0:
            return max_num
        max_sum, c_sum = 0, 0
        for n in nums:
            c_sum += n
            if c_sum < 0:
                c_sum = 0 
            if c_sum > max_sum:
                max_sum = c_sum
        return max_sum