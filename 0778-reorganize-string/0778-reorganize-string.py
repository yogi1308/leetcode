import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [[-count, char] for char, count in Counter(s).items()]
        heapq.heapify(heap)
        
        string = ""
        prev = None  # holds [count, char] to push back next iteration

        while heap:
            count, char = heapq.heappop(heap)
            string += char

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if count + 1 != 0:
                prev = [count + 1, char]

        return string if len(string) == len(s) else ""