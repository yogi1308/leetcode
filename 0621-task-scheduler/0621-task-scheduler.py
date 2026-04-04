class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hmap = {}
        for task in tasks:
            hmap[task] = hmap.get(task, 0) + 1
        heap = []
        for task in hmap:
            heap.append([hmap[task] * -1, task])
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
                newtask = [(task[0] + 1), task[1]]
                if newtask[0] != 0:
                    heapq.heappush(heap, newtask)

            while gap >= 0 and heap:
                cycles += 1
                gap -= 1
                
            gap = n

        return cycles
