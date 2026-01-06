class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortest = len(s)
        shortest_start = 0
        shortest_end = 0

        tmap = {}
        smap = {}
        matches = 0
        for char in t:
            tmap[char] = tmap.get(char, 0) + 1
            smap[char] = 0

        l = 0
        keys = tmap.keys()
        len_keys = len(keys)
        for r in range(0, len(s)):
            if s[r] in keys:
                smap[s[r]] = smap[s[r]] + 1
                if smap[s[r]] == tmap[s[r]]: 
                    matches += 1
            
            while matches == len_keys:

                if matches == len_keys and shortest >= r - l:
                    shortest = r - l
                    shortest_start = l
                    shortest_end = r + 1
                if s[l] in keys:
                    smap[s[l]] = smap[s[l]] - 1
                    if smap[s[l]] + 1 == tmap[s[l]]:
                        matches -= 1
                l += 1

        return s[shortest_start : shortest_end]