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
            substr = s2[l : r]

            if l != 0:
                s2Count[substr[-1]] = s2Count[substr[-1]] + 1
                if s2Count[substr[-1]] == s1Count[substr[-1]]: matches += 1
                elif s2Count[substr[-1]] - 1== s1Count[substr[-1]]: matches -= 1

            if matches == 26: return True
            
            s2Count[substr[0]] = s2Count[substr[0]] - 1
            if s2Count[substr[0]] == s1Count[substr[0]]: matches += 1
            elif s2Count[substr[0]] + 1 == s1Count[substr[0]]: matches -= 1

            l += 1
        return False



# Original brute force solution
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         longest = 1
#         count = {}
#         for l in range(len(s)):
#             for r in range(l + 1, len(s) + 1):
#                 substr = s[l : r]
#                 for char in substr:
#                     if char in count:
#                         count[char] = count[char] + 1
#                     else:
#                         count[char] = 1
                
#                 max_f = max(count.values())
#                 if len(substr) - max_f <= k and len(substr) > longest:
#                     longest = len(substr)
#                 count.clear()
#         return longest
                

# sliding window solution
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         s1map = {}
#         for char in s1:
#             s1map[char] = s1map.get(char, 0) + 1
        
#         l = 0
#         for r in range(len(s1), len(s2) + 1):
#             substr = s2[l : r]
#             print(substr)
#             valid = True    
#             for char in s1map:
#                 if s1map[char] != substr.count(char):
#                     valid = False
#             if valid:
#                 return True
#             l += 1
#         return False


# Faster solution that uses hashmap and matches variable to track matches
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         if len(s1) > len(s2):
#             return False

#         s1Count, s2Count = [0] * 26, [0] * 26
#         for i in range(len(s1)):
#             s1Count[ord(s1[i]) - ord('a')] += 1
#             s2Count[ord(s2[i]) - ord('a')] += 1

#         matches = 0
#         for i in range(26):
#             if s1Count[i] == s2Count[i]: matches += 1

#         l = 0
#         for r in range(len(s1), len(s2)):
#             if matches == 26:
#                 return True

#             index = ord(s2[r]) - ord('a')
#             s2Count[index] += 1
#             if s1Count[index] == s2Count[index]:
#                 matches += 1
#             elif s1Count[index] + 1 == s2Count[index]:
#                 matches -= 1

#             index = ord(s2[l]) - ord('a')
#             s2Count[index] -= 1
#             if s1Count[index] == s2Count[index]:
#                 matches += 1
#             elif s1Count[index] - 1 == s2Count[index]:
#                 matches -= 1
#             l += 1
#         return matches == 26


# Neetcode's best solution. the earlier solution was the same as this but adapted to use hashmap instead of arrays. this one is faster 
# than hashmap solution used earlier
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         if len(s1) > len(s2):
#             return False

#         s1Count, s2Count = [0] * 26, [0] * 26
#         for i in range(len(s1)):
#             s1Count[ord(s1[i]) - ord('a')] += 1
#             s2Count[ord(s2[i]) - ord('a')] += 1

#         matches = 0
#         for i in range(26):
#             matches += (1 if s1Count[i] == s2Count[i] else 0)

#         l = 0
#         for r in range(len(s1), len(s2)):
#             if matches == 26:
#                 return True

#             index = ord(s2[r]) - ord('a')
#             s2Count[index] += 1
#             if s1Count[index] == s2Count[index]:
#                 matches += 1
#             elif s1Count[index] + 1 == s2Count[index]:
#                 matches -= 1

#             index = ord(s2[l]) - ord('a')
#             s2Count[index] -= 1
#             if s1Count[index] == s2Count[index]:
#                 matches += 1
#             elif s1Count[index] - 1 == s2Count[index]:
#                 matches -= 1
#             l += 1
#         return matches == 26