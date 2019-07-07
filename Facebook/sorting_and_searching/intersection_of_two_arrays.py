# Intersection of Two Arrays
"""
nums1 = [4,9,5] 
nums2 = [9,4,9,8,4]
     *
set([4,9,5])

set([9,4,9,8,4])

return [4, 9]
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = set(nums1)
        result = [] 
        for num in set(nums2):
            if num in nums:
                result.append(num)
        return result