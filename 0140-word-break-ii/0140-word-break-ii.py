class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordDict = set(wordDict)
        def backtrack(idx, sentence):
            if idx == len(s):
                sentence = " ".join(sentence)
                res.append(sentence)
                return
            for i in range(idx, len(s) + 1):
                w = s[idx: i]
                if w in wordDict:
                    sentence.append(w)
                    backtrack(i, sentence)
                    sentence.pop()
        backtrack(0, [])
        return res
                    
