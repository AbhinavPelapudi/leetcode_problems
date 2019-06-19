# time: O(n)
# space: O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = s = 0 
        prefix = {0:1} #initialize this, not sure why
        for i in range(len(nums)):
            n = nums[i]
            s += n 
            checker = s - k
            if checker in prefix:
                count +=  prefix.get(checker,0)
            prefix[s] = prefix.get(s,0) + 1
        return count
            
        