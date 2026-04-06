class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        seen = set()
        for character in s:
            if character not in seen:
                times = s.count(character) * -1
                heapq.heappush(heap, [times, character])
                seen.add(character)
        string = ""
        prev = []
        while heap:
            letter = heapq.heappop(heap)
            string += letter[1]

            if prev != [] and prev[0] != -1:
                prev = [prev[0] + 1, prev[1]]
                heapq.heappush(heap, prev)

            prev = letter

        return "" if len(string) != len(s) else string
            