class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, idx, used):
            used.append((x, y))
            br1, br2, br3, br4 = False, False, False, False

            if idx == len(word): 
                return True

            if y + 1 < len(board):
                if board[y + 1][x] == word[idx] and (x, y + 1) not in used:
                    br1 = dfs(x, y + 1, idx + 1, used)

            if x + 1 < len(board[y]):
                if board[y][x + 1] == word[idx] and (x + 1, y) not in used:
                    br2 = dfs(x + 1, y, idx + 1, used)

            if x - 1 >= 0:
                if board[y][x - 1] == word[idx] and (x - 1, y) not in used:
                    br3 = dfs(x - 1, y, idx + 1, used)

            if y - 1 >= 0:
                if board[y - 1][x] == word[idx] and (x, y - 1) not in used:
                    br4 = dfs(x, y - 1, idx + 1, used)

            used.remove((x, y))
            if br1 or br2 or br3 or br4: return True
            return False
        
        for i in range(len(board)):
            start = 0
            for occurences in range(board[i].count(word[0])):
                if dfs(start + board[i][start:].index(word[0]), i, 1, []): return True
                start = start + board[i][start:].index(word[0]) + 1
        return False