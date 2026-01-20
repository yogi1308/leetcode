class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newList = []
        appended = False
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                newList.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                if not appended: 
                    newList.append(newInterval)
                    appended = True
                newList.append(intervals[i])
            else:
                newInterval = [min(*intervals[i], *newInterval), max(*intervals[i],*newInterval)]
        if not appended: newList.append(newInterval)
        return newList