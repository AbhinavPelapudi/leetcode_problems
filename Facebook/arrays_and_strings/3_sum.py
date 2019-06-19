# time: O(n^2)
# space: O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #sorted nums
        result = []
        for i in range(len(nums) - 2):
            if nums[i] > 0: #breaks here 
                break
            elif i>0 and nums[i]==nums[i-1]: #prevent duplicates
                continue
            j, k = i + 1, len(nums) - 1 #initialize j and k
            while i < j and j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    while j<k and nums[j]==nums[j+1]: #prevent duplicates
                        j+=1
                    while j<k and nums[k]==nums[k-1]: #prevent duplicates
                        k-=1
                    j+=1
                    k-=1
                elif nums[i] + nums[j] + nums[k] > 0: #move k based on sorting
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0: #move j based on sorting
                    j += 1
        return result
    