'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true
'''


class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        if not postorder or len(postorder) == 1:
            return True
        index = 0
        while index < len(postorder) - 1:
            if postorder[index] > postorder[-1]:
                break
            index += 1
       
        left = postorder[: index]
        right = postorder[index: -1]
        for t in right:
            if t < postorder[-1]:
                return False
        if self.verifyPostorder(left) and self.verifyPostorder(right):
            return True
        return False


a = Solution()
print(a.verifyPostorder([1,3,2,6,5]))