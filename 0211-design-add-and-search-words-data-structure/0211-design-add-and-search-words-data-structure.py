class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        res = False
        def dfs(curr, idx):
            if idx == len(word): return curr.end
            if word[idx] == ".":
                for opt in curr.children:
                    if dfs(curr.children[opt], idx + 1):
                        return True
                return False                    
            elif word[idx] not in curr.children:
                return False
            return dfs(curr.children[word[idx]], idx + 1)

        return dfs(self.root, 0)
        
