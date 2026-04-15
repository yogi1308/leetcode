class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        if len(self.arr) % 2 == 1: return self.arr[len(self.arr) // 2]
        return (self.arr[len(self.arr) // 2] + self.arr[(len(self.arr) // 2) - 1]) / 2