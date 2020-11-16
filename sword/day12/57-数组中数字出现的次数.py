'''
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
'''


# 解题思路：
'''
1.得到全部异或的结果K
2.K的二级制中为1的地方可以用于分组（因为为1的地方表示两个数字的二进制在这个位置为1和0）
3.利用并的操作分组，再进行异或即可找到两个数字

'''

class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k = self.yihuo(nums)
        count = 0
        while k % 2 != 1:
            k = k >> 1
            count += 1
        tmp = 2 ** count

        res = []
        r1 = []
        r2 = []
        for num in nums:
            if num & tmp == tmp:
                r1.append(num)
            else:
                r2.append(num)
        res.append(self.yihuo(r1))
        res.append(self.yihuo(r2))
        return res

    def yihuo(self, nums):
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        return res


a = Solution()
r = a.singleNumbers([4,1,4,6])
print(r)


