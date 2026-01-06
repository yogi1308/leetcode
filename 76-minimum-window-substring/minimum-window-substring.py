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


# original brute force Solution
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if s == t: return s
#         shortest = len(s)
#         shortestStr = ""
#         tmap = {}
#         for char in t:
#             tmap[char] = tmap.get(char, 0) + 1

#         for l in range(len(s) - len(t) + 1):
#             for r in range(len(t) + l, len(s) + 1):
#                 substr = s[l : r]
#                 valid = True
#                 print(substr)

#                 for char in tmap.keys():
#                     if tmap[char] > substr.count(char):
#                         valid = False
#                         break
#                 if valid and len(substr) <= shortest:
#                     shortest = len(substr)
#                     shortestStr = substr
#         return shortestStr


sliding window Solution
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if s == t: return s
#         shortest = len(s)
#         shortestStr = ""
#         tmap = {}
#         smap = {}
#         for i in range(26):
#             tmap[chr(65 + i)] = 0
#             smap[chr(65 + i)] = 0
#             tmap[chr(97 + i)] = 0
#             smap[chr(97 + i)] = 0

#         for char in t:
#             tmap[char] = tmap.get(char) + 1

#         for l in range(len(s) - len(t) + 1):
#             matches = 0
#             smap = {key: 0 for key in smap}
#             for char in s[l : len(t) + l]:
#                 smap[char] = smap.get(char) + 1
#             for char in tmap.keys():
#                 if tmap[char] <= smap[char]:
#                     matches += 1

#             for r in range(len(t) + l, len(s) + 1):
#                 substr = s[l : r]
#                 print(substr, matches)

#                 if r != len(t) + l:
#                     smap[substr[-1]] = smap[substr[-1]] + 1
#                     if smap[substr[-1]] == tmap[substr[-1]]: 
#                         matches += 1
                
#                 if matches == 52 and len(substr) <= shortest:
#                     shortest = len(substr)
#                     shortestStr = substr
#                     print("shortestStr:", shortestStr, "shortest:", shortest)
#                     if shortest == len(t):
#                         return shortestStr

#         return shortestStr
