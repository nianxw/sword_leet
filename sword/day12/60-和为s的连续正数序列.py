'''
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
'''


# 解法1：前N项和，减去target，看差值是否存在，存在的话，则连续片段为差值对应的位置到当前位置
class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        d = {0: 0}
        res = []
        r = 0
        for i in range(1, target):
            r += i
            d[r] = i
            if r >= target:
                if (r - target) in d:
                    if i - d[r - target] >= 2:
                        res.append(list(range(d[r - target]+1, i + 1)))
        return res

a = Solution()
print(a.findContinuousSequence(9))

# 解法2：滑动窗口，[i，j)，一般采用左闭右开，当窗口内片段和小于target，则j+1,否则i+1


class Solution1(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        i = 1
        j = 1
        s = 0
        res = []

        while i <= target // 2:  # 当起始位置大于target的一半时不符合要求
            if s < target:
                j += 1
                s += j - 1
            elif s > target:
                i += 1
                s -= i - 1
            else:
                res.append(list(range(i, j)))
                j += 1
                s += j - 1
        return res