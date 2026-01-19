class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new_matrix = []
        for arr in matrix:
            for num in arr:
                new_matrix.append(num)
        
        found = False
        while new_matrix:
            if target < new_matrix[round(len(new_matrix) / 2)]:
                new_matrix = new_matrix[:round(len(new_matrix) / 2)]
            elif target > new_matrix[round(len(new_matrix) / 2)]:
                new_matrix = new_matrix[(round(len(new_matrix) / 2)) + 1:]
            elif target == new_matrix[round(len(new_matrix) /2)]:
                return True
        return False