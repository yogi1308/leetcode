class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        def isValid(r, c, occupied):
            for cell in occupied:
                if cell[1] == c: return False
                if cell[0] - cell[1] == r - c: return False
                if cell[0] + cell[1] == r + c: return False
            return True

        def backtrack(row, occupied):
            nonlocal res
            if row == n:
                res += 1
            for col in range(n):
                if isValid(row, col, occupied):
                    occupied.append((row, col))
                    backtrack(row + 1, occupied)
                    occupied.pop()
        backtrack(0, [])
        return res