class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1={}
        dict2={}
        for num in nums1:
            dict1[num] = dict1.get(num, 0) + 1
        for num in nums2:
            dict2[num] = dict2.get(num, 0) + 1
            
        result = []
        
        for key, value in dict2.items():
            if dict1.get(key):
                frequency = min(dict2[key], dict1[key])
                mini_result = [key] * frequency
                result.extend(mini_result)
        return result