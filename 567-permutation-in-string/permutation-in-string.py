class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count, s2Count = {}, {}
        for i in range(26):
            s1Count[chr(97 + i)] = 0
            s2Count[chr(97 + i)] = 0
        for i in range(len(s1)):
            s1Count[s1[i]] += 1
            s2Count[s2[i]] += 1
        
        matches = 0
        for i in s1Count:
            if s1Count[i] == s2Count[i]: matches += 1

        l = 0
        for r in range(len(s1), len(s2) + 1):
            if l != 0:
                matched_earlier = s2Count[s2[r-1]] == s1Count[s2[r-1]]
                s2Count[s2[r-1]] = s2Count[s2[r-1]] + 1
                if s2Count[s2[r-1]] == s1Count[s2[r-1]]: matches += 1
                elif matched_earlier: matches -= 1

            if matches == 26: return True
            
            matched_earlier = s2Count[s2[l]] == s1Count[s2[l]]
            s2Count[s2[l]] = s2Count[s2[l]] - 1
            if s2Count[s2[l]] == s1Count[s2[l]]: matches += 1
            elif matched_earlier: matches -= 1

            l += 1
        return False