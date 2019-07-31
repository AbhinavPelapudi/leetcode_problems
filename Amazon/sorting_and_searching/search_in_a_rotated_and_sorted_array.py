"""
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

             *
[4,5,6,7,0,1,2]
         *
s = 4 
e = 6
m = 3

"""


# Search in Rotated Sorted Array
 class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0 
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            elif nums[mid] < nums[end]:
                if nums[mid] < target and target < nums[end]:
                    start = mid + 1
                else: 
                    end = mid - 1
            elif nums[start] < nums[mid]:
                if nums[start] < target and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                end -= 1
                
        return -1