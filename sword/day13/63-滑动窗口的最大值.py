'''
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

'''

# 采用双端队列解决滑动窗口最值问题
# 对于当前题目，要求最大值，则此时双端队列的头部数据应为最大值，因此队列应为递减序列


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k <= 0:
            return []
        res = []
        deque = [] # 其中存放的是索引
        for i in range(len(nums)):
            # 若队列头部元素位于窗口之外，则应弹出头部元素
            while deque and deque[0] <= i - k:
                deque.pop(0)

            # 若队列尾部元素小于等于当前nums[i]，则弹出尾部元素，原因如下：
            # 首先，每次添加进来的元素必然在窗口内，
            # 若大于等于前面的元素，弹出前面元素，不会影响到当前以及后续窗口最值
            # 并且当窗口左边界移动时，当前索引也会晚于前面索引弹出
            while deque and nums[deque[-1]] <= nums[i]:
                deque.pop()
            deque.append(i)

            # 当索引达到窗口大小时，记录最值
            if i >= k - 1:
              res.append(nums[deque[0]])
        return res