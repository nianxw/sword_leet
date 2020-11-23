'''
求 1+2+...+n ，要求不能使用
乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45
'''


# 逻辑短路：
# 1. 当 A&&B 中 A 为False时，则 B 不会被执行
# 2. 当 A||B 中 A 为True时，则 B 不会被执行


class Solution(object):
    def __init__(self):
        self.res = 0

    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 采用逻辑短路
        n > 1 and self.sumNums(n-1)
        self.res += n
        return self.res