class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a != 0: heapq.heappush(heap, [a * -1, 'a'])
        if b != 0: heapq.heappush(heap, [b * -1, 'b'])
        if c != 0: heapq.heappush(heap, [c * -1, 'c'])
        print(heap)
        res = ""
        prev = []
        while heap:
            popped = heapq.heappop(heap)
            used = False
            if not (len(res) >= 2 and res[-1] == res[-2] and popped[1] == res[-1]): 
                res += popped[1]
                popped = [popped[0] + 1, popped[1]]
                while prev:
                    heapq.heappush(heap, prev.pop())
                if popped[0] < 0: heapq.heappush(heap, popped)
                used = True
            if not used: prev.append(popped)
                
        return res