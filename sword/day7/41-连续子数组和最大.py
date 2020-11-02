'''
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

 

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

'''


class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]  # 全局最大
        cur_max = nums[0]  # 以当前元素为结尾时最大值，第一步时，自身是最大的

        for i in range(1, len(nums)):
            cur_max = max(cur_max+nums[i], nums[i])
            max_sum = max(max_sum, cur_max)  # 比较每一步最大，获得全局最大
        return max_sum