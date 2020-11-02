'''
数字以0123456789101112131415…的格式序列化到一个字符序列中。
在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

 

示例 1：

输入：n = 3
输出：3
示例 2：

输入：n = 11
输出：0

'''


'''
数字排列可以与自然数自然的换算可变成：

位数 = 9*(10**0+2*10**2+3*10**3+...)
'''


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        while n > 9*(10**i)*(i+1):
            n -= 9*(10**i)*(i+1)
            i += 1
        x = n // (i+1)
        y = n % (i+1)
        cur_num = 10**i - 1 + x
        if y == 0:
            return cur_num % 10
        else:
            cur_num += 1
            for i in range(i+2-y):
                tmp = cur_num // 10
                r = cur_num % 10
                cur_num = tmp
            return r

a = Solution()
print(a.findNthDigit(19))
