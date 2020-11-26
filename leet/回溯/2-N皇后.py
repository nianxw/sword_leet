'''
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

~皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。

'''


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = []
        self.res = [['.']*n for _ in range(n)]

        def dfs(i):
            if i == n:
                self.result.append(self.transform(self.res[:]))
                return
            for j in range(n):
                if self.valid(i, j, n):
                    self.res[i][j] = 'Q'
                    dfs(i+1)
                    self.res[i][j] = '.'
        dfs(0)
        return self.result

    def valid(self, i, j, n):
        a = 1
        while 0 <= i-a <= i-1 and 0 <= j-a <= j-1:
            if self.res[i-a][j-a] == 'Q':
                return False
            a += 1

        a = 1
        while 0 <= i-a <= n-1 and 0 <= j+a <= n-1:
            if self.res[i-a][j+a] == 'Q':
                return False
            a += 1

        a = 1
        while 0 <= i-a <= i-1:
            if self.res[i-a][j] == 'Q':
                return False
            a += 1
        return True

    def transform(self, m):
        res = []
        for i in range(len(m)):
            res.append(''.join(m[i]))
        return res


a = Solution()
print(a.solveNQueens(4))


# 改进版，判断是否合理的函数不需要这么麻烦，只需要维护三个数组即可