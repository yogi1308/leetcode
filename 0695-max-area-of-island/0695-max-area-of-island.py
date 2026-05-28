class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        cnt = 0

        def dfs(x, y):
            nonlocal cnt
            grid[y][x] = 0
            cnt += 1
            if x-1 >= 0 and grid[y][x-1] == 1:
                dfs(x-1, y)
            if y-1 >= 0 and grid[y-1][x] == 1:
                dfs(x, y-1)
            if x+1 < len(grid[y]) and grid[y][x+1] == 1:
                dfs(x+1, y)
            if y+1 < len(grid) and grid[y+1][x] == 1:
                dfs(x, y+1)
            return

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1 :
                    dfs(x, y)
                    res = max(res, cnt)
                    cnt = 0
        
        return res