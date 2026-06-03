class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        for x in range(len(heights[0])):
            pacific.add((x, 0))
            atlantic.add((x, len(heights) - 1))
        for y in range(len(heights)):
            pacific.add((0, y))
            atlantic.add((len(heights[0]) - 1, y))
        
        def dfs(x, y, ocean):
            visited = pacific if ocean == "p" else atlantic
            if x - 1 >= 0 and heights[y][x - 1] >= heights[y][x] and (x - 1, y) not in visited:
                visited.add((x - 1, y))
                dfs(x - 1, y, ocean)
            if x + 1 < len(heights[0]) and heights[y][x + 1] >= heights[y][x] and (x + 1, y) not in visited:
                visited.add((x + 1, y))
                dfs(x + 1, y, ocean)
            if y - 1 >= 0 and heights[y - 1][x] >= heights[y][x] and (x, y - 1) not in visited:
                visited.add((x, y - 1))
                dfs(x, y - 1, ocean)
            if y + 1 < len(heights) and heights[y + 1][x] >= heights[y][x] and (x, y + 1) not in visited:
                visited.add((x, y + 1))
                dfs(x, y + 1, ocean)

        for x, y in pacific.copy(): dfs(x, y, "p")
        for x, y in atlantic.copy(): dfs(x, y, "a")

        common = []
        for (x, y) in pacific:
            if (x, y) in atlantic: common.append([y, x])

        return common
