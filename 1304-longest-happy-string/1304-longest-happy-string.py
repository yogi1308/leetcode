class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a != 0: heapq.heappush(heap, [a * -1, 'a'])
        if b != 0: heapq.heappush(heap, [b * -1, 'b'])
        if c != 0: heapq.heappush(heap, [c * -1, 'c'])
        res = ""
        q = ['', ''] 
        
        while heap:
            popped = heapq.heappop(heap)
            
            # Check if using this character would create a triple
            if res[-2:] == popped[1] * 2:
                if not heap:
                    break  # Nowhere to go, stop here
                
                # Grab the next best character instead
                next_popped = heapq.heappop(heap)
                res += next_popped[1]
                next_popped[0] += 1
                
                # Push both back to re-evaluate in the next loop
                if next_popped[0] < 0:
                    heapq.heappush(heap, next_popped)
                heapq.heappush(heap, popped)
            else:
                # Safe to use the most frequent character
                res += popped[1]
                popped[0] += 1
                if popped[0] < 0:
                    heapq.heappush(heap, popped)
                    
        return res