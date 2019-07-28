class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        self.matrix = matrix
        self.T = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        self.update_t()

    def update_t(self):
        for i in range(1,len(self.T)):
            for j in range(1,len(self.T[0])):
                self.T[i][j] = self.T[i - 1][j] + self.T[i][j - 1] + self.matrix[i - 1][j - 1] - self.T[i - 1][j - 1]
        
    def update(self, row: int, col: int, val: int) -> None:
        self.matrix[row][col] = val
        self.update_t()
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        T_row1 = row1 + 1
        T_col1 = col1 + 1
        T_row2 = row2 + 1
        T_col2 = col2 + 1
        return self.T[T_row2][T_col2] - self.T[T_row1 - 1][T_col2] - self.T[T_row2][T_col1 - 1] + self.T[T_row1 - 1][T_col1 - 1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)