class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rowSum = []
        for row in matrix:
            rowarr = []
            sum = 0
            for cell in row:
                sum += cell
                rowarr.append(sum)
            self.rowSum.append(rowarr)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for row in range(row1, row2 + 1):
            add = self.rowSum[row][col2]
            if col1 != 0:
                add -= self.rowSum[row][col1 - 1]
            sum += add
        return sum




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)