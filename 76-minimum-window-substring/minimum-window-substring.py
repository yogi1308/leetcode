class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""

        # 1. Count characters in t
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        
        # 2. Filter s to keep only characters present in t
        # This is the biggest speed boost for many test cases
        filtered_s = []
        for i, char in enumerate(s):
            if char in t_count:
                filtered_s.append((i, char))

        required = len(t_count)
        l, r = 0, 0
        formed = 0
        window_counts = {}
        
        # (length, start_index, end_index)
        ans = float("inf"), None, None

        # 3. Iterate only over the filtered characters
        while r < len(filtered_s):
            char = filtered_s[r][1]
            window_counts[char] = window_counts.get(char, 0) + 1

            if window_counts[char] == t_count[char]:
                formed += 1

            # Try to contract
            while l <= r and formed == required:
                start_idx = filtered_s[l][0]
                end_idx = filtered_s[r][0]
                
                if end_idx - start_idx + 1 < ans[0]:
                    ans = (end_idx - start_idx + 1, start_idx, end_idx)

                char_left = filtered_s[l][1]
                window_counts[char_left] -= 1
                if window_counts[char_left] < t_count[char_left]:
                    formed -= 1
                l += 1
            
            r += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]