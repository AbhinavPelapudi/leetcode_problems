# Intersection of Two Arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = set(nums1)
        result = [] 
        for num in set(nums2):
            if num in nums:
                result.append(num)
        return result