class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(substrings, idx):
            print(substrings)
            if len("".join(substrings)) == len(s):
                shouldBeAdded = True
                for string in substrings:
                    if string != string[::-1]:
                        shouldBeAdded = False
                        break
                if shouldBeAdded:
                    res.append(substrings[:])
            for end in range(idx, len(s)):
                substrings.append(s[idx:end + 1])
                dfs(substrings, end + 1)
                substrings.pop()
        dfs([], 0)
        return res