#Subsets
"""
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
                                  (-1, [])
                          /                    \
                        (0, [])                        (0, [1])
                    /           \                 /             \
            (1, [])         (1, [2])            (1, [1])           (1, [1, 2])
          /      \         /     \            /        \           /         \
     (2, [])  (2, [3]) (2, [2])  (2, [2,3]) (2, [1])  (2, [1,3]) (2, [1,2])  (1, [1,2,3])
"""
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
