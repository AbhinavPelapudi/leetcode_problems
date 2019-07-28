class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            sb = start
            for i in range(start, end):
                if nums[i] <= nums[end]:
                    nums[sb], nums[i] = nums[i], nums[sb]
                    sb += 1
            nums[sb], nums[end] = nums[end], nums[sb] 
            if len(nums) - sb == k:
                return nums[sb]
            else:
                if k >  len(nums) - 1 - sb:
                    end = sb - 1
                else:
                    start = sb + 1
