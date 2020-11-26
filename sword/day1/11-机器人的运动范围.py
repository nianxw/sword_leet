'''
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。
请问该机器人能够到达多少个格子？

 

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20
'''


class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 1
        visited = [[0 for x in range(n)] for y in range(m)]
        return self.dfs(0, 0, m, n, k, visited)

    def get_index(self, index):
        a = index // 10
        b = index % 10
        return a + b

    def dfs(self, i, j, m, n, k, visited):
        if i < 0 or i >= m or j < 0 or j >= n:
            return 0
        cur_k = self.get_index(i) + self.get_index(j)
        if cur_k > k or visited[i][j] == 1:
            return 0
        visited[i][j] = 1
        res = self.dfs(i+1, j, m, n, k, visited) + self.dfs(i-1, j, m, n, k, visited) + self.dfs(i, j+1, m, n, k, visited) + self.dfs(i, j-1, m, n, k, visited)
        # visited[i][j] = 0
        return res + 1

a = Solution()

print(a.movingCount(2, 3, 1))