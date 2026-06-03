class Solution:
    def solve(self, board: List[List[str]]) -> None:
        notSurrounded = set()
        def dfs(r, c):
            if (r, c) in notSurrounded: return
            notSurrounded.add((r, c))
            if r - 1 >= 0 and board[r - 1][c] == "O":
                board[r - 1][c]
                dfs(r - 1, c)
            if c - 1 >= 0 and board[r][c - 1] == "O":
                board[r][c - 1]
                dfs(r, c - 1)
            if r + 1 < len(board) and board[r + 1][c] == "O":
                board[r + 1][c]
                dfs(r + 1, c)
            if c + 1 < len(board[0]) and board[r][c + 1] == "O":
                board[r][c + 1]
                dfs(r, c + 1)

        for c in range(len(board[0])):
            if board[0][c] == "O": dfs(0, c)
            if board[len(board) - 1][c] == "O": dfs(len(board) - 1, c)
        for r in range(len(board)):
            if board[r][0] == "O": dfs(r, 0)
            if board[r][len(board[0]) - 1] == "O": dfs(r, len(board[0]) - 1)

        for r in range(1, len(board) - 1):
            for c in range(1, len(board[0]) - 1):
                if board[r][c] == "O" and (r, c) not in notSurrounded:
                    board[r][c] = "X"



