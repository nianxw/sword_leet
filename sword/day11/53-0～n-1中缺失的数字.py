'''
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

 
示例 1:

输入: [0,1,3]
输出: 2
示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
'''


# 因为这里是排序数组，所以数组分成两个部分
# 1.左部分：nums[i] = i
# 2.右部分：nums[i] != i
# 所以只需要找到右部分的左边界即可

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] == 1:
            return 0
        s = 0
        e = len(nums) - 1

        while s <= e:
            mid = (s+e) // 2

            if nums[mid] == mid:
                s = mid + 1
            else:
                e = mid - 1
        return s

