'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。


示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''


# 先找局部最小，再找局部最大值，计算差值
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        max_profit = 0
        tmp = prices[0]
        tmp_min = prices[0]
        i = 1
        while i < len(prices):
            while i < len(prices) and tmp >= prices[i]:
                tmp = prices[i]
                i += 1
            tmp_min = min(tmp_min, tmp)

            while i < len(prices) and tmp < prices[i]:
                tmp = prices[i]
                i += 1
            tmp_high = tmp

            max_profit = max(max_profit, tmp_high - tmp_low)
        return max_profit
