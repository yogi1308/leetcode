class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l, r = 0, mountainArr.length() - 1
        peak = 0
        peak_val = 0
        while l < r:
            mid = (l + r) // 2
            mid_val = mountainArr.get(mid)
            mid_val_minus_1 = mountainArr.get(mid - 1)
            mid_val_plus_1 = mountainArr.get(mid + 1)
            if mid_val_minus_1 < mid_val and mid_val > mid_val_plus_1:
                peak = mid
                peak_val = mid_val
                break
            if mid_val < mid_val_plus_1: l = mid + 1
            elif mid_val < mid_val_minus_1: r = mid
        
        if target > peak_val: return -1
        l, r = 0, peak
        while l < r:
            mid = (l + r) // 2
            mid_val = mountainArr.get(mid)
            if mid_val == target:
                return mid
            if target < mid_val: r = mid
            else: l = mid + 1

        l, r = peak, mountainArr.length() - 1
        while l <= r:
            mid = (l + r) // 2
            mid_val = mountainArr.get(mid)
            if mid_val == target:
                return mid
            if target < mid_val: l = mid + 1
            else: r = mid -1
        return -1