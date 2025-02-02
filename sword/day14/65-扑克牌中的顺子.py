'''
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

示例 1:

输入: [1,2,3,4,5]
输出: True
 

示例 2:

输入: [0,0,1,2,5]
输出: True
'''


class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        zero_count = 0
        i = 0
        while i < 5 and nums[i] == 0:
            zero_count += 1
        
        v = 0
        for j in range(zero_count+1, 5):
            tmp = nums[j] - nums[j-1] - 1
            if tmp < 0:
                return False
            v += nums[j] - nums[j-1] - 1
        if v > zero_count:
            return False
        return True


# 满足两个条件：无重复，最大值-最小值 < 5
class Solution1:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0: continue # 跳过大小王
            ma = max(ma, num) # 最大牌
            mi = min(mi, num) # 最小牌
            if num in repeat: return False # 若有重复，提前返回 false
            repeat.add(num) # 添加牌至 Set
        return ma - mi < 5 # 最大牌 - 最小牌 < 5 则可构成顺子 