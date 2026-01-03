class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        longest = 1
        l, r = 0, 1
        while r < len(s) + 1:
            substr = s[l : r]
            if substr.count(substr[len(substr) - 1]) == 2:
                l += substr.find(substr[len(substr) - 1]) + 1
            elif len(substr) > longest:
                longest = len(substr)
            r += 1
        return longest