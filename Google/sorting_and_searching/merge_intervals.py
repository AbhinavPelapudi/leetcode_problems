# Merge Intervals

""""
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
[[1,3],[2,6],[8,10],[15,18]]
           *
result = [[1, 6], [8, 10], [15, 18]]
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        result = []
        intervals.sort()

        for i in range(1, len(intervals)):
            if intervals[i-1][1] >= intervals[i][0]:
                intervals[i][0] = intervals[i-1][0]
                intervals[i][1] = max(intervals[i-1][1],intervals[i][1])
            else:
                result.append(intervals[i - 1])
        result.append(intervals[-1])
        return result
                
