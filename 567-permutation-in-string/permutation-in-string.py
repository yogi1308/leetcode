class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = {}
        for char in s1:
            if char in s1map:
                s1map[char] = s1map[char] + 1
            else:
                s1map[char] = 1
        
        l = 0
        for r in range(len(s1), len(s2) + 1):
            substr = s2[l : r]
            valid = True    
            for char in s1map:
                if s1map[char] != substr.count(char):
                    valid = False
            if valid:
                return True
            l += 1
        return False