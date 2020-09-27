"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."
"""


def replaceSpace(s):
    s_new = ''
    for i in s:
        if i == ' ':
            s_new += '%20'
        else:
            s_new += i
    return s_new