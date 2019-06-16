class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not len(nums): return 0
        prev_min = prev_max = max_product = current_max = current_min = nums[0]
        for i in range(1,len(nums)):
            current_max = max(nums[i], prev_max * nums[i], prev_min * nums[i])
            current_min = min(nums[i], prev_max * nums[i], prev_min * nums[i])
            prev_max = current_max
            prev_min = current_min
            current = max(current_max, current_min)
            if current > max_product:
                max_product = current
        return max_product