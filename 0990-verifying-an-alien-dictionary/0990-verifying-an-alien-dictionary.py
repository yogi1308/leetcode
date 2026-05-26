class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderTable = {order[c]: c for c in range(len(order))}
        def appearsBefore(c1, c2):
            if orderTable[c1] <= orderTable[c2]: return True
            return False

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            same = True
            for j in range(min(len(words[i]), len(words[i + 1]))):
                c1 = word1[j]
                c2 = word2[j]
                if c1 == c2: continue
                same = False
                if appearsBefore(c1, c2): break
                else: 
                    return False
            if same:
                if len(word1) > len(word2): return False
        return True
        