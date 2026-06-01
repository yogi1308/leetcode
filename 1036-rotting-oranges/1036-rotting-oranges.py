class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0 
        fresh = set()
        rotten = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1: fresh.add((x, y))
                if grid[y][x] == 2: rotten.append((x, y))

        if not fresh: return 0

        q = deque()
        q.append(rotten)

        def add(rotten):
            adj = []
            print(rotten)
            for x, y in rotten:
                if x - 1 >= 0 and grid[y][x - 1] == 1:
                    adj.append((x - 1, y))
                    grid[y][x - 1] = 2
                    fresh.remove((x - 1, y))
                if y - 1 >= 0 and grid[y - 1][x] == 1:
                    adj.append((x, y - 1))
                    grid[y - 1][x] = 2
                    fresh.remove((x, y - 1))
                if x + 1 < len(grid[0]) and grid[y][x + 1] == 1:
                    adj.append((x + 1, y))
                    grid[y][x + 1] = 2
                    fresh.remove((x + 1, y))
                if y + 1 < len(grid) and grid[y + 1][x] == 1:
                    adj.append((x, y + 1))
                    grid[y + 1][x] = 2
                    fresh.remove((x, y + 1))
            return adj


        while q:
            lastRotten = q.popleft()
            adj = add(lastRotten)
            if adj: q.append(adj)
            minutes += 1

        if not fresh: return minutes -1
        return -1

