"""
Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

                                   *
    [[0,2],[5,10],[13,23],[24,25]]
       
                             *
    [[1,5],[8,12],[15,24],[25,26]]

result = [[1, 2], [5, 5], [8, 10],[15, 23], [24, 24], [25, 25]]
"""


class Solution:
    def intervalIntersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        i,j, res = 0, 0, []
        while i < len(a) and j < len(b):
            if a[i][1] < b[j][0]:
                i += 1
            elif b[j][1] < a[i][0]:
                j += 1
            else:
                res.append([max(a[i][0], b[j][0]), min(a[i][1], b[j][1])]) 
                if a[i][1]> b[j][1]:
                    j += 1
                else:
                    i += 1
        return res
        