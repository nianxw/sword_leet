'''
46. 全排列

给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return None
        res = []

        def dfs(nums, path):
            if len(path) == len(nums):
                res.append(path[:])  # 深拷贝：全值改变，当前拷贝值不变，因为地址不同
                return

            for num in nums:
                if num not in path:
                    path.append(num)
                    dfs(nums, path)
                    path.remove(num)
        dfs(nums, [])
        return res


a = Solution()
r = a.permute([1,2,3])
print(r)