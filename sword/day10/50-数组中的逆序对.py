'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

 

示例 1:

输入: [7,5,6,4]
输出: 5
'''

# 采用归并排序，merge的过程中，如果左边数组中的数大于右边数组中的数，则左边到最后都大于右边的这个数（有序数组）


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        return self.merge_sort(nums, 0, len(nums)-1)

    def merge_sort(self, nums, L, R):
        if len(nums) <= 1 or L >= R:
            return 0
        mid = L + (R-L)//2
        x1 = self.merge_sort(nums, L, mid)
        x2 = self.merge_sort(nums, mid+1, R)
        x3 = self.merge(nums, L, mid, R)
        return x1 + x2 + x3

    def merge(self, nums, L, mid, R):
        i = L
        j = mid + 1
        h = []
        res = 0
        while i <= mid and j <= R:
            if nums[i] <= nums[j]:
                h.append(nums[i])
                i += 1
            else:
                h.append(nums[j])
                j += 1
                res += mid - i + 1
        if i <= mid:
            h.extend(nums[i: mid + 1])
        if j <= R:
            h.extend(nums[j: R + 1])
        nums[L: R+1] = h
        return res
