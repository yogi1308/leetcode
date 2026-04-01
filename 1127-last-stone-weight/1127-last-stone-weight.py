class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i] * -1
        heapq.heapify(stones)
        while len(stones) > 1:
            l1 = heapq.heappop(stones) * -1
            l2 = heapq.heappop(stones) * -1
            remains = abs(l1 - l2)
            remains = remains * -1
            heapq.heappush(stones, remains)
        return stones[0] * -1