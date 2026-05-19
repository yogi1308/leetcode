class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        
        def isValid(row, col, occupied):
            for cell in occupied:
                if cell[1] == col:
                    return False
                if cell[0] - cell[1] == row - col:
                    return False
                if cell[0] + cell[1] == row + col:
                    return False
            return True
             
        def backtrack(row, occupied):
            if row == n:
                board = [['.' for _ in range(n)] for _ in range(n)]
                for r,c in occupied:
                    board[r][c] = "Q"
                b = []
                for r in board:
                    s = "".join(r)
                    b.append(s)
                res.append(b[:])

            
            for i in range(n):
                if isValid(row, i, occupied):
                    occupied.append((row, i))
                    backtrack(row + 1, occupied)
                    occupied.pop()
        
        backtrack(0, [])
        return res