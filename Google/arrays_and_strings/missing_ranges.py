class Solution:
    def append_ranges(self, min_num, max_num, missing):
        if  min_num == max_num:
            missing.append(str(min_num))
        else:
            missing.append(str(min_num) + '->' + str(max_num))

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        missing = []
        if not nums:
            self.append_ranges(lower, upper, missing)
            return missing
        for i in range(len(nums)):
            if i == 0:
                if nums[i] > lower:
                    self.append_ranges(lower, nums[i] - 1, missing)
            if i < len(nums) - 1 and nums[i] != nums[i + 1] and nums[i] + 1 != nums[i + 1]:
                self.append_ranges(nums[i] + 1, nums[i + 1] - 1, missing)
            elif i == len(nums) - 1:
                if nums[i] < upper:
                    self.append_ranges(nums[i] + 1, upper, missing)
        return missing