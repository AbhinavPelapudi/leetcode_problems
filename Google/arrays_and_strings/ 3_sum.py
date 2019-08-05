 #time: O(n^2)
# space: O(1)

"""
input = [-1, 0, 1, 2, -1, -4],
output = [
  [-1, 0, 1],
  [-1, -1, 2]
]
result = [[-1,-1,2], [-1, 0, 2]]
step 1: sort -> [-4, -1, -1, 0, 1, 2]
step 2: iterate 
        [-4, -1, -1, 0, 1, 2]
                  i
                     j
                        k 
        
step 3: return result
"""
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