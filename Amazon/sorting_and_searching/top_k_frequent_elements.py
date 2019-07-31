"""
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

frequency = {1: 3, 2: 2, 3: 1}
partners = [[1, 3], [2: 2], [3: 1]]
result = [1, 2]


"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        partners = []
        result = []
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        for key, value in frequency.items():
            partners.append([value, key])
        partners.sort()
        partners.reverse()
        for i in range(k):
            result.append(partners[i][1]) 
        return result
        
        