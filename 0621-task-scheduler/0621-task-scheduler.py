class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hmap = {}
        for task in tasks:
            hmap[task] = hmap.get(task, 0) + 1
        heap = []
        for task in hmap:
            heap.append([hmap[task] * -1, task])
        heapq.heapify(heap)
        hmap = {}

        cycles = 0
        while heap:
            gap = n
            taskcompleted = []
            while gap >= 0 and heap:
                taskcompleted.append(heapq.heappop(heap))
                cycles += 1
                gap -= 1
            
            for task in taskcompleted:
                if task[0] + 1 != 0:
                    heapq.heappush(heap, [(task[0] + 1), task[1]])

            if heap: cycles += 1 + gap

        return cycles
