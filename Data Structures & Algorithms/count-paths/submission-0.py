class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(r, c, rows, cols, cache):
            if r == rows or c == cols:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == rows - 1 and c == cols - 1:
                return 1
            cache[r][c] = (dfs(r + 1, c, rows, cols, cache) + dfs(r, c + 1, rows, cols, cache))
            return cache[r][c]
        cache = [[0] * n for _ in range(m)]
        return dfs(0, 0, m, n, cache)