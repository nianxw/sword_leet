'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
'''

# 解题思路:
# 1. '.'只能出现一次，且在e的前面
# 2. 'e'只能出现一次，且出现前有数字
# 3. '+'/'-'只能出现在开头和e后面一位


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        num_flag = False
        dot_flag = False
        e_flag = False
        for i in range(len(s)):
            if s[i] >= '0' and s[i] <= '9':
                num_flag = True
            elif s[i] == '.' and not dot_flag and not e_flag:
                dot_flag = True
            elif (s[i] == 'e' or s[i] == 'E') and num_flag and not e_flag:
                e_flag = True
                num_flag = False
            elif (s[i] == '+' or s[i] == '-') and (i == 0 or s[i-1] == 'e' or s[i-1] == 'E'):
                pass
            else:
                return False
        return num_flag