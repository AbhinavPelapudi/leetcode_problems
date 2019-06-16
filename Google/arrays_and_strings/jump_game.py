# Jump Game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_max = nums[0]
        for n in nums[1:]:
            if not current_max:
                return False
            current_max = max(current_max - 1, n)
        return True