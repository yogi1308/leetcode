class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            mid = ((r - l) // 2) + l
            cnt_days = 1
            sum_weights = 0
            for weight in weights:
                if sum_weights + weight <= mid:
                    sum_weights += weight
                else:
                    cnt_days += 1
                    sum_weights = weight
                if cnt_days > days: break
            if cnt_days <= days: r = mid
            else: l = mid + 1
        return l
