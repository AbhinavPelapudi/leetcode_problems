# Move Zeroes
# time: O(n)
# space: O(1)
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

        