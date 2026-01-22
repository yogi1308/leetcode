class TimeMap:
    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""

        array = self.timeMap[key]
        l, r = 0, len(array) - 1
        ans = -1

        while l <= r:
            mid = (l + r) // 2
            if array[mid][0] <= timestamp:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return "" if ans == -1 else array[ans][1]
