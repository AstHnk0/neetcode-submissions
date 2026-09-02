class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visitIsland = set()
        islandCounter = 0
        def dfs(grid, r, c):
            ROWS, COLS = len(grid), len(grid[0])
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visitIsland or grid[r][c] == "0":
                return
            if grid[r][c] == "1":
                visitIsland.add((r,c))
                dfs(grid, r + 1, c)
                dfs(grid, r - 1, c)
                dfs(grid, r, c + 1)
                dfs(grid, r, c - 1)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row,col) not in visitIsland:
                    islandCounter += 1
                    dfs(grid, row, col)     
        return islandCounter

