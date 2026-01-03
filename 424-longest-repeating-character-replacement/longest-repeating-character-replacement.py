class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        max_f = 0
        count = {}
        for r in range(1, len(s) + 1):
            substr = s[l : r]
            if substr[len(substr) - 1] in count:
                count[substr[len(substr) - 1]] = count[substr[len(substr) - 1]] + 1
                max_f = max(count.values())
            else:
                count[substr[len(substr) - 1]] = 1
                max_f = max(count.values())
            
            if len(substr) - max_f <= k and len(substr) > longest:
                longest = len(substr)
            elif len(substr) - max_f > k:
                count[substr[0]] = count[substr[0]] - 1
                l += 1
        return longest