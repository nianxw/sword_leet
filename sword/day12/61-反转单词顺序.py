'''
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。

示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        res = []
        i, j = 0, 0
        while i < len(s):
            while i < len(s) and s[i] == " ":
                i += 1
            j = i + 1
            while j < len(s) and s[j] != " ":
                j += 1
            if s[i:j]:
                res.append(s[i: j])
            i = j + 1
        return " ".join(res[::-1])


a = Solution()
print(a.reverseWords("  hello world!  "))