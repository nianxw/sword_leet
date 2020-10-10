'''
实现函数double Power(double base, int exponent)，求base的exponent次方。
不得使用库函数，同时不需要考虑大数问题。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
 

说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
'''


# 采用递归的方式进行求解：
# 递归通项为：  {
# n = 0, res = 1
# n 为偶数时, res = [x**(n/2)]  *  [x**(n/2)]
# n 为奇数时，res = x ** (n -1)  * x
# }

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = -n
            x = 1 / x
        if n == 0:
            return 1
        if n % 2 == 0:
            return self.myPow(x, n // 2) ** 2
        else:
            return self.myPow(x, n - 1) * x

a = Solution()
r = a.myPow(2,9)
print(r)