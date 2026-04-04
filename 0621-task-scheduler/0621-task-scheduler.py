class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)

        cycles = 0
        gap = n
        while heap:
            taskcompleted = []
            while gap >= 0 and heap:
                task = heapq.heappop(heap)
                taskcompleted.append(task)
                cycles += 1
                gap -= 1
            
            for task in taskcompleted:
                if task != -1:
                    heapq.heappush(heap, task + 1)

            while gap >= 0 and heap:
                cycles += 1
                gap -= 1
                
            gap = n

        return cycles
