'''
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

示例 1:
输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
'''


class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        res[0][0] = grid[0][0]
        for i in range(1, n):
            res[0][i] = res[0][i-1] + grid[0][i]
        for j in range(1, m):
            res[j][0] = res[j-1][0] + grid[j][0]

        for j in range(1, m):
            for i in range(1, n):
                res[j][i] = max(res[j-1][i], res[j][i-1]) + grid[j][i]
        return res[m-1][n-1]

    # 优化为滚动数组，空间复杂度变成O(N)
    def maxValue_optimize(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        res = [0 for _ in range(n)]
        res[0] = grid[0][0]
        for i in range(1, n):
            res[i] = res[i-1] + grid[0][i]

        for j in range(1, m):
            for i in range(n):
                if i == 0:
                    res[i] = res[i] + grid[j][i]
                else:
                    res[i] = max(res[i-1], res[i]) + grid[j][i]
        return res[n-1]

a = Solution()
print(a.maxValue_optimize([[1,2],[5,6],[1,1]]))