'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

 

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
x
'''


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix is None:
            return None
        res = []
        a, b = 0, 0
        c, d = len(matrix)-1, len(matrix[0])-1

        while a <= c and b <= d:
            for index in range(b, d+1):
                res.append(matrix[a][index])

            for index in range(a+1, c+1):
                res.append(matrix[index][d])

            if a < c:
                for index in range(d-1, b, -1):
                    res.append(matrix[c][index])
            if b < d:
                for index in range(c, a, -1):
                    res.append(matrix[index][b])

            a += 1
            b += 1
            c -= 1
            d -= 1
        return res


a = Solution()
print(a.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))