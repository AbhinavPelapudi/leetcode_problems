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
            
        