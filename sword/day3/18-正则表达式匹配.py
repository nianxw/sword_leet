'''
请实现一个函数用来匹配包含 '.' 和 '*' 的正则表达式。模式中的字符 '.' 表示任意一个字符，而 '*' 表示它前面的字符可以出现任意次（含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。
'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s = len(s)
        len_p = len(p)

        dp = [[False]*(len_p+1) for _n in range(len_s+1)]

        # base

        # 当s、p都为空时，可以匹配
        # 当p为空,s不为空时，匹配不上
        dp[0][0] = True

        for j in range(1, len_p+1):
            if p[j-1] == '*':
                # 越界问题不需考虑，因为'*'必然是跟在一个字符后面,所以当j等于1时，进不来这个判断
                dp[0][j] = dp[0][j-2]

        for i in range(1, len_s+1):
            for j in range(1, len_p+1):
                if p[j-1] in (s[i-1], '.'):
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if p[j-1] == '*':
                        if p[j-2] in (s[i-1], '.'):
                            if dp[i][j-2] or dp[i][j-1] or dp[i-1][j]:
                                dp[i][j] = True
                        else:
                            dp[i][j] = dp[i][j-2]
        return dp[len_s][len_p]