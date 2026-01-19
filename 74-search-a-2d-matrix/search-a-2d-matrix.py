class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        while matrix:
            mid = matrix[round(len(matrix) / 2)]
            if target < mid[0]:
                matrix = matrix[: round(len(matrix) / 2)]
            elif target > mid[-1]:
                matrix = matrix[round(len(matrix) / 2) + 1 :]
            else:
                matrix = mid
                break

        while matrix:
            if target < matrix[round(len(matrix) / 2)]:
                matrix = matrix[:round(len(matrix) / 2)]
            elif target > matrix[round(len(matrix) / 2)]:
                matrix = matrix[(round(len(matrix) / 2)) + 1:]
            elif target == matrix[round(len(matrix) /2)]:
                return True
        return False