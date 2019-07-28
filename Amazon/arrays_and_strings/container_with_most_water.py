class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        max_water = 0 
        while start < end:
            max_water = max(min(height[start], height[end]) * (end - start), max_water)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_water
            
        