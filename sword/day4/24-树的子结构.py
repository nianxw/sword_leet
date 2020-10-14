'''
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        if A is None or B is None:
            return False
        return self.is_same(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def is_same(self, A, B):
        if B is None:
            return True  # 只要B为空了，此时必然为True
        if A is None:
            # 此时B不是空
            return False
        if A.val == B.val:
            if self.is_same(A.left, B.left) and self.is_same(A.right, B.right):
                return True
        return False