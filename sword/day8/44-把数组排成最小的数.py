'''
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

示例 1:

输入: [10,2]
输出: "102"
示例 2:

输入: [3,30,34,5,9]
输出: "3033459"
'''


'''
排序规则

a + b > b + a, 则 a > b 字典序

'''


class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ''
        self.q_sort(nums, 0, len(nums)-1)
        return ''.join([str(_) for _ in nums])

    
    def q_sort(self, nums, L, R):
        p1, p2 = self.partition(nums, L, R)
        self.q_sort(nums, L, p1)
        self.q_sort(nums, p2, R)

    

    def partition(self, nums, L, R):
        less = L - 1
        more = R
        cur = L
        while cur < more:
            if self.compare(nums[cur], nums[R]) == 1:
                less += 1
                nums[less], nums[cur] = nums[cur], nums[less]
                cur += 1
            elif self.compare(nums[cur], nums[R]) == 0:
                more -= 1
                nums[cur], nums[more] = nums[more], nums[cur]
            else:
                cur += 1
        nums[more], nums[R] = nums[R], nums[more]
        return less, more + 1

    def compare(self, a, b):
        if int(str(a)+str(b)) > int(str(b)+str(a)):
            return 0
        elif int(str(a)+str(b)) < int(str(b)+str(a)):
            return 1
        else:
            return 2
    
        