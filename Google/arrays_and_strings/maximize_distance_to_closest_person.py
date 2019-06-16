# Maximize Distance to Closest Person
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_zeros = 0
        start = 0 
        for i in range(len(seats)):
            if seats[i] == 1:
                if seats[start] == 1:
                    if (i - start) // 2 > max_zeros:
                        max_zeros = (i - start) // 2
                else:
                    if (i - start) > max_zeros:
                        max_zeros = i - start
                start = i
            elif seats[i] == 0 and i == len(seats) - 1:
                if (i - start) > max_zeros:
                    max_zeros = i - start
        return max_zeros