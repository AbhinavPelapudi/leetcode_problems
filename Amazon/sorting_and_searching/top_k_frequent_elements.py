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
        
        