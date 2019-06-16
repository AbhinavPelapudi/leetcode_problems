#Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = []
        def get_subsets(depth, builder):
            if depth == len(nums) - 1:
                subs.append(builder)
                return 
            get_subsets(depth + 1, builder)
            get_subsets(depth + 1, builder + [nums[depth + 1]])
        get_subsets(-1, [])
        return subs
