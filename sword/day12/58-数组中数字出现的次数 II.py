'''
在一个数组 nums 中除一个数字只出现一次之外，
其他数字都出现了三次。请找出那个只出现一次的数字。

示例 1：

输入：nums = [3,4,3,3]
输出：4
示例 2：

输入：nums = [9,1,7,9,7,9,7]
输出：1
'''

# 解题思路：
'''
出现了3次数，则二进制中出现1的位置应该是3的倍数，
当出现非3的倍数，这个1来自于单身数字
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            x = 1 << i
            cnt = 0
            for num in nums:
                if num & x != 0:
                    cnt += 1    
            if cnt % 3 != 0:
                res += x
        return res - 2 ** 32 if res > 2 ** 31 - 1 else res

                    
