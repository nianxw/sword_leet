'''
2011.11.2

给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

发现重复计算，则采用dp方法计算
'''


class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 1
        s = []
        while num != 0:
            s.append(num % 10)
            num = num // 10
        res = [0 for _ in range(len(s) + 1)]
        res[0] = 1
        res[1] = 1
        for i in range(2, len(s) + 1):
            if s[i-1] == 1:
                res[i] = res[i-1] + res[i-2]
            elif s[i-1] == 2 and s[i-2] <= 5:
                res[i] = res[i-1] + res[i-2]
            else:
                res[i] = res[i-1]
        return res[len(s)]

a = Solution()
b = a.translateNum(12258)
print(b)
                

