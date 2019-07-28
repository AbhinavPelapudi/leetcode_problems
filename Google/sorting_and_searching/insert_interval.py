class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        result = []
        intervals.append(newInterval) 
        intervals.sort()
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
                continue
            result.append(intervals[i])
        return result