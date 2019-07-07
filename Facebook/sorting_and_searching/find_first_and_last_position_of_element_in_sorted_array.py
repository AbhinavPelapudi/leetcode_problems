# Find First and Last Position of Element in Sorted Array
"""
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]



[5,7,7,8,8,10] 
       *

[5, 7, 7, 8]
          *
[8, 10]
 *
"""


class Solution:
    def binary_search_first(self, nums, start, end, target):
        found_pos = end
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                found_pos = mid
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return found_pos

    def binary_search_last(self, nums, start, end, target):
        found_pos = start
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                found_pos = mid
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return found_pos  
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums) - 1
        first_and_last = [-1, -1]
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                first_and_last[0] = self.binary_search_first(nums, start, mid, target)
                first_and_last[1] = self.binary_search_last(nums, mid, end, target)
                return first_and_last
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return first_and_last