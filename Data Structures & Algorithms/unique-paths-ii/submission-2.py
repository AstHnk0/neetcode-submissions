class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def dfs(r, c, rows, cols, obstacleGrid):
            if r == rows or c == cols or obstacleGrid[r][c] == 1:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == rows - 1 and c == cols - 1:
                return 1
            cache[r][c] = (dfs(r + 1, c, rows, cols, obstacleGrid) + dfs(r, c + 1, rows, cols, obstacleGrid))
            return cache[r][c]
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[0] * cols for _ in range(rows)]
        return dfs(0, 0, rows, cols, obstacleGrid)