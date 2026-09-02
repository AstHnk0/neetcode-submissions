class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visitIsland = set()
        def dfs(grid, r, c):
            ROWS, COLS = len(grid), len(grid[0])
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visitIsland or grid[r][c] == 0:
                return 0
            visitIsland.add((r,c))
            return 1 + dfs(grid, r + 1, c) + dfs(grid, r - 1, c) + dfs(grid, r, c + 1) + dfs(grid, r, c - 1)
        maxArea = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visitIsland:
                    currentArea = dfs(grid, r, c)
                    maxArea = max(maxArea, currentArea)
        return maxArea
