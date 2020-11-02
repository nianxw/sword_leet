'''
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。


示例 1：
输入：n = 12
输出：5

示例 2：
输入：n = 13
输出：6
'''


'''
递归求解：
思想和我想得差不多，不过我想的没那么清晰。

解法见：
https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/solution/javadi-gui-by-xujunyi/
'''

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.f(n)

    def f(self, n):
        if n <= 0:
            return 0
        a = 0  # n的位数
        b = 0  # n最高位的数字
        c = 0  # n-最高位的数字的其他值
        src_num = n
        while n != 0:
            x = n // 10
            y = n % 10
            n = x
            a += 1
        a = a - 1
        b = y
        c = src_num - b * (10**a)

        if b == 1:
            # 当最高位为1时，此时，多出来的1为c+1
            return c + 1 + self.f(c) + self.f((10**a)-1)
        else:
            # 当最高位不是1时，此时，考虑多出来的1为最高位为1时的数目，正好为1000-1999  为1000
            return 10**a + b*self.f(10**a-1) + self.f(c)

a = Solution()
print(a.countDigitOne(12))