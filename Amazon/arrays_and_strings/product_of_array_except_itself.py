

"""
Product of Array Except Self
time: O(n)
space: O(n)
Input:  [1,2,3,4]
Output: [24,12,8,6]

product = [24,12,8,6]

left_product = 2, 6
right_product = 4, 12, 24




"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums) #create an array of 1s
        left_product = 1 #initialize left product with 1
        right_product = 1 #initialize right product with 1
        for i in range(len(products) -1, -1, -1): #move through with products right of the num
            products[i] *= right_product
            right_product *= nums[i]
        for i in range(len(products)):#move through with products left of the num
            products[i] *= left_product
            left_product *= nums[i]
        return products #return array