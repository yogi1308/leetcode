class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l + r) // 2
            needed = 1
            curr = 0

            for w in weights:
                if curr + w > mid:
                    needed += 1
                    if needed > days:
                        break
                    curr = 0
                curr += w

            if needed <= days:
                r = mid
            else:
                l = mid + 1

        return l
