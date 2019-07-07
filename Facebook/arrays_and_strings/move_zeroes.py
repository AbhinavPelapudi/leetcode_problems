# Move Zeroes
# time: O(n)
# space: O(1)

"""
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

idx = 0 
   *
[0,1,0,3,12]
 * 

idx = 1
       *
[1,0,0,3,12]
   * 

idx = 2
       *
[1,3,0,0,12]
     * 


idx = 2
          *
[1,3,12,0,0]
     * 
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0 #start at 0th index
        for i in range(len(nums)):
            if nums[i] != 0: #check for non zero values
                nums[i], nums[idx] = nums[idx], nums[i] #swap them respectively
                idx += 1 #increase idx

        