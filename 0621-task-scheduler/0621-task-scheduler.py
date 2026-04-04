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
        order = []
        while max(hmap.values()) > 0:
            taskcompleted = []
            while gap >= 0 and heap and max(hmap.values()) > 0:
                task = heapq.heappop(heap)
                taskcompleted.append(task)
                order.append(task[1])
                cycles += 1
                gap -= 1
            
            for task in taskcompleted:
                newtask = [(task[0] + 1), task[1]]
                if newtask[0] != 0:
                    heapq.heappush(heap, newtask)
                hmap[task[1]] = hmap[task[1]] - 1

            while gap >= 0 and max(hmap.values()) > 0:
                taskcompleted.append("idle")
                order.append("idle")
                cycles += 1
                gap -= 1
                
            gap = n

        return cycles
