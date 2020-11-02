'''
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
'''

class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0 or not arr:
            return []
        s = 0
        e = len(arr) - 1
        index = self.partition(arr, s, e)
        while index != k-1:
            if index < k-1:
                s = index + 1
                index = self.partition(arr, s, e)
            elif index > k-1:
                e = index - 1
                index = self.partition(arr, s, e)
        return arr[:k]

    def partition(self, arr, l, r):
        index = l - 1
        for i in range(l, r):
            if arr[i] <= arr[r]:
                index += 1
                arr[i], arr[index] = arr[index], arr[i]

        index += 1
        arr[index], arr[r] = arr[r], arr[index]
        return index



a = Solution()
b = a.getLeastNumbers([3,2,1], 2)
print(b)