"""
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

|
|
|    *              *
|    *              *     *
|    *  *           *     *
|    *  *     *     *     *
|    *  *     *  *  *     *
|    *  *     *  *  *  *  *
|    *  *  *  *  *  *  *  *  
| *  *  *  *  *  *  *  *  *
|_______________________________________________________
  1  8  6  2  5  4  8  3  7

start = 0, 1 
end = 2
max_water = 0, 49


1 * (8 - 0) = 8
7 * (8 - 1) = 49
3 * (7 - 1) = 18
8 * (6 - 1) = 40
4 * (5 - 1) = 16
5 * (4 - 1) = 15
2 * (3 - 1) = 4
6 * (2 - 1) = 6
"""


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
            
        