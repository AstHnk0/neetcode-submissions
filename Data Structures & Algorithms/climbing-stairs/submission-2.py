class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(n, i):
            if i in memo:
                return memo[i]
            if i == n:
                return 1
            elif i > n:
                return 0
            else:
                memo[i] = dfs(n, i + 1) + dfs(n, i + 2)
                return memo[i]
        return dfs(n, 0)



        