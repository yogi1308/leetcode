class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False

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

        for word in words:
            addWord(word)

        def dfs(x, y, occupied, curr, word):
            word += board[y][x]
            if (x, y) in occupied: return
            if curr.end: 
                res.add(word[:])
                
            occupied.add((x, y))
            if x - 1 >= 0:
                if board[y][x-1] in curr.children: 
                    dfs(x-1, y, occupied, curr.children[board[y][x-1]], word)
            if x + 1 < len(board[0]):
                if board[y][x + 1] in curr.children: 
                    dfs(x + 1, y, occupied, curr.children[board[y][x + 1]], word)
            if y - 1 >= 0:
                if board[y-1][x] in curr.children: 
                    dfs(x, y-1, occupied, curr.children[board[y-1][x]], word)
            if y + 1 < len(board):
                if board[y+1][x] in curr.children: 
                    dfs(x, y+1, occupied, curr.children[board[y+1][x]], word)
            occupied.remove((x,y))
            return
        
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] in root.children:
                    dfs(x, y, set(), root.children[board[y][x]], "")

        return list(res)


