'''
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''

# 参考：
# https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/1.5-qi-ta-jing-dian-wen-ti/tuan-mie-gu-piao-wen-ti

# 采用动态规划解决所有题型
# dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
# dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])

# dp[i][k][0]表示的含义是 在第i天手上没有持股票，至今至多进行了K次交易

# 例如：dp[3][2][1]: 今天是第3天，手上持有股票，至今至多进行了2次交易

# base case: dp[-1][k][1] = dp[i][0][1] = -infinity, dp[-1][k][0] = dp[i][0][0] = 0


'''
对于这道题目来说, k = 1
dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1]+prices[i])
dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0]-prices[i])

令 dp_0 = dp[i][1][0], dp_1 = dp[i][1][1], 此时 dp[i-1][0][0] = 0

-----> dp_0 = max(dp_0, dp_1 + prices[i])
-----> dp_1 = max(dp_1, -prices[i])
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        d_0 = 0
        d_1 = -prices[0]

        for i in range(1, len(prices)):
            d_0 = max(d_0, d_1 + prices[i])
            d_1 = max(d_1, -prices[i])
        return max(d_0, d_1)
