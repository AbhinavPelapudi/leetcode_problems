class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        left_product = 1
        right_product = 1
        for i in range(len(products) -1, -1, -1):
            products[i] *= right_product
            right_product *= nums[i]
        for i in range(len(products)):
            products[i] *= left_product
            left_product *= nums[i]
        return products