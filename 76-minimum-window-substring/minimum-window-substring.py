class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t: return s
        elif len(s) < len(t): return ""
        if len(s) == len(t): 
            if sorted(s) == sorted(t): return s
            else: return ""

        shortest = len(s)
        shortestStr = ""

        tmap = {}
        smap = {}
        matches = 0
        for char in t:
            tmap[char] = tmap.get(char, 0) + 1
            smap[char] = 0

        l = 0
        keys = tmap.keys()
        for r in range(0, len(s)):
            if s[r] in keys:
                smap[s[r]] = smap[s[r]] + 1
                if smap[s[r]] == tmap[s[r]]: 
                    matches += 1
            
            while matches == len(keys):

                if matches == len(keys) and shortest >= r - l:
                    shortest = r - l
                    shortestStr = s[l : r + 1]
                if s[l] in keys:
                    smap[s[l]] = smap[s[l]] - 1
                    if smap[s[l]] + 1 == tmap[s[l]]:
                        matches -= 1
                l += 1

        return shortestStr