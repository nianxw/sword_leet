'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
'''


class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        if numbers is None:
            return None
        s = 0
        e = len(numbers) - 1
        while s < e:
            mid = (s + e) // 2
            if numbers[mid] > numbers[e]:
                s = mid + 1
            elif numbers[mid] < numbers[e]:
                e = mid
            else:
                # 这里是考虑了相等的情况，此时，让右边界变小，总归会经过最小值
                # 如果让左边界变大的话，则可能会漏掉最小值，因为这里都是和右边界的值比较的
                e -= 1
        return numbers[s]


a = Solution()

print(a.minArray([3,3,1,3, 3, 3, 3]))