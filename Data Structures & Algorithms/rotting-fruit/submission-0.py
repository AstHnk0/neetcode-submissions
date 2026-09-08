class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(grid):
            ROWS, COLS = len(grid), len(grid[0])
            visit = set()
            queue = deque()
            fresh = 0
            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == 2:
                        queue.append((row, col))
                    if grid[row][col] == 1:
                        fresh += 1
            minutes = 0
            while queue and fresh > 0:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    neighbors = [1, 0], [0, 1], [-1, 0], [0, -1]
                    for dr, dc in neighbors:
                        if (min(dr + r, dc + c) < 0 or dr + r == ROWS or dc + c == COLS):
                            continue
                        if grid[dr + r][dc + c] != 1:
                            continue
                        else:
                            grid[dr + r][dc + c] = 2
                            fresh -= 1
                            queue.append((dr + r, dc + c))
                minutes += 1
            if fresh == 0:
                return minutes
            else:
                return -1
        return bfs(grid)




