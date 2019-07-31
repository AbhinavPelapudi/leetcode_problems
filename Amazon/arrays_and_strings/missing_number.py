"""

Input: [9,6,4,2,3,5,7,0,1]
Output: 8



"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0 
        nums_sum = sum(nums)
        max_num = max(nums)
        all_num = sum([i for i in range(max_num + 1)])
        return all_num - nums_sum or max_num + 1