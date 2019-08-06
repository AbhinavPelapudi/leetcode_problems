
"""
Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.


[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 


dp = [
    [3, 2, 1], 
    [1, 3, 1], 
    [2, 0, 2]
]

val = 3
max_path = 3 
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[0] * len(matrix[0]) for i in range(len(matrix))]
        def dfs(i, j):
            val = matrix[i][j]
            if not dp[i][j]:
                dp[i][j] = 1 + max(
                    dfs(i + 1, j) if i < len(matrix) - 1 and matrix[i + 1][j] > matrix[i][j] else 0, 
                    dfs(i - 1, j) if i > 0 and matrix[i - 1][j] > matrix[i][j] else 0,
                    dfs(i, j - 1) if j > 0  and matrix[i][j - 1] > matrix[i][j] else 0,
                    dfs(i, j + 1) if j < len(matrix[0]) - 1  and matrix[i][j + 1] > matrix[i][j] else 0,
                )
            return dp[i][j]
        max_path = 0 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_path = max(dfs(i, j), max_path)
        return max_path