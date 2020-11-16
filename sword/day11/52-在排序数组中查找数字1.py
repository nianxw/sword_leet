'''
统计一个数字在排序数组中出现的次数。

 

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
'''


# 采用二分法分别找左、右边界


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index1 = self.find_left(nums, target)

        index2 = self.find_right(nums, target)
        return index2 - index1 - 1
    

    def find_left(self, nums, target):
        # 找左边界
        s = 0
        e = len(nums) - 1
        while s <= e:
            mid = s + (e - s) // 2
            if nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1
        return e


    def find_right(self, nums, target):
        # 找右边界
        s = 0
        e = len(nums) - 1
        while s <= e:
            mid = s + (e - s) // 2
            if nums[mid] <= target:
                s = mid + 1
            else:
                e = mid - 1
        return s