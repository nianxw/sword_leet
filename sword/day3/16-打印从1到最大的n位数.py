'''
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
 

说明：

用返回一个整数列表来代替打印
n 为正整数
'''


class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return range(1, 10**n)


def printNumbers(n):
    def dfs(n, index, s, is_begin):
        if index == n:
            if s:
                print(s)
            return
        for i in range(10):
            if i != 0:
                dfs(n, index+1, s+str(i), False)
            else:
                if is_begin:
                    dfs(n, index+1, s, True)
                else:
                    dfs(n, index+1, s+str(i), False)

    dfs(n, 0, '', True)

printNumbers(2)
