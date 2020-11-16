'''
11.13

字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。
比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

 

示例 1：

输入: s = "abcdefg", k = 2
输出: "cdefgab"
示例 2：

输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"
'''

class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        self.reverse_s(s, 0, n-1)
        self.reverse_s(s, n, len(s)-1)
        self.reverse_s(s, 0, len(s)-1)
        return s

    def reverse_s(self, s, i, j):
        while i < j:
            tmp1 = s[i]
            tmp2 = s[j]
            s[i] = tmp2
            s[j] = tmp1
            i += 1
            j -= 1

s = "abcdefg"
a = Solution()
print(a.reverseLeftWords(s, 2))