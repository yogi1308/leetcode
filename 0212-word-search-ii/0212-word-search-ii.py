class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        res = set()

        def addWord(word):
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.end = True
            curr.word = word

        for word in words:
            addWord(word)

        def dfs(x, y, curr):
            ch = board[y][x]
            if ch not in curr.children: return
            curr = curr.children[ch]

            if curr.end:
                res.add(curr.word)
                curr.end = False

            board[y][x] = "#"
            if x - 1 >= 0 and board[y][x-1] != "#":
                dfs(x-1, y, curr)
            if x + 1 < len(board[0]) and board[y][x+1] != "#":
                dfs(x+1, y, curr)
            if y - 1 >= 0 and board[y-1][x] != "#":
                dfs(x, y-1, curr)
            if y + 1 < len(board) and board[y+1][x] != "#":
                dfs(x, y+1, curr)
            board[y][x] = ch

        for y in range(len(board)):
            for x in range(len(board[0])):
                dfs(x, y, root)

        return list(res)


