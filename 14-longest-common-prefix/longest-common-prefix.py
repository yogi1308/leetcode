class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        if "" in strs: return ""
        for word in strs:
            length = len(prefix)
            if len(prefix) > len(word): prefix = prefix[: len(word)]
            for i in range(min(len(word), len(prefix))):
                if word[i] != prefix[i]: 
                    prefix = prefix[: i]
                    break
            print(prefix)
        return prefix