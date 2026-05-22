class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = word

        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, curr):
            ch = board[r][c]
            if ch not in curr.children:
                return
            node = curr.children[ch]

            if node.word:
                res.append(node.word)
                node.word = None

            board[r][c] = "#"
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != "#":
                    dfs(nr, nc, node)
            board[r][c] = ch

            # correct pruning: remove from parent's children dict
            if not node.children and not node.word:
                del curr.children[ch]
                
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return res