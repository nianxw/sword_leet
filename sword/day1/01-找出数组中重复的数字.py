"""
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
"""

def findRepeatNumber1(nums):
    # 考虑时间，空间O(n)，时间O(1)
    num_dict = set()
    for num in nums:
        if num in num_dict:
            return num
        else:
            num_dict.add(num)


def findRepeatNumber2(nums):
    # 考虑空间，空间O(1)，时间O(nlogn)
    nums.sort()
    pre = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == pre:
            return pre
        else:
            pre = nums[i]


def findRepeatNumber3(nums):
    # 既考虑时间也考虑空间 空间O(1)，时间O(n)
    # 因为题目前提是一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内
    # 可以将每个数放在其对应的位置上，然后当某个数与其作为索引对应的值相同时，及其应该在的位置上的值与自身相等，则为重复数据
    n = len(nums)
    for i in range(n):
        while i != nums[i]:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            temp = nums[i]
            nums[i], nums[temp] = nums[temp], nums[i]
