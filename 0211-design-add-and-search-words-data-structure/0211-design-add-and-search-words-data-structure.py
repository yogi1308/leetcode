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
        def dfs(curr, word):
            if not word: return curr.end
            if word[0] == ".":
                for opt in curr.children:
                    if dfs(curr.children[opt], word[1:]):
                        return True
                return False                    
            elif word[0] not in curr.children:
                return False
            return dfs(curr.children[word[0]], word[1:])

        return dfs(self.root, word)
        
