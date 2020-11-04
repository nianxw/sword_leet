'''
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''


# 不变更起始位置时，一直计算最大长度，变更最大长度时（注意：这里变更起始位置的条件是，起始位置在需要重复字符对应位置之前），不计算最大长度
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        alpha_dict = {}
        cur_start = 0
        max_len = 0
        for i in range(len(s)):
            if s[i] in alpha_dict:
                if cur_start <= alpha_dict[s[i]]:
                    cur_start = alpha_dict[s[i]] + 1
                    alpha_dict[s[i]] = i
                    continue
            max_len = max(max_len, i - cur_start + 1)
            alpha_dict[s[i]] = i
        return max_len

a = Solution()
print(a.lengthOfLongestSubstring("abcabcbb"))