#time: O(n)
#space: O(1)

class Solution:
    def reverse_nums(self, i, j, nums): #reverses nums
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: #general basecase
            return
        right = len(nums) - 1 #start at far end of the array
        for i in range(len(nums) - 1, 0, -1): #continue until you are at 1st index
            if nums[i - 1] < nums[i]: 
                right = i
                break
            if i - 1 == 0:
                return self.reverse_nums(i - 1, len(nums) -1, nums) #just reverse and return
        pivot = right - 1 #this is where array will be pivoted
        succesor = 0 
        for i in range(len(nums) -1, pivot, -1): #go up until pivot
            if nums[i] > nums[pivot]:
                succesor = i 
                break
        nums[pivot], nums[succesor] = nums[succesor], nums[pivot] #swap pivot and successor
        self.reverse_nums(right, len(nums) - 1, nums) # from right put the rest of the array in ascending order