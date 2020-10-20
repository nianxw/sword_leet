'''
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]
'''

# 之字形的需要两个栈


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        h1 = [root]
        h2 = []
        res = []

        while h1:
            tmp1 = []
            while h1:
                node = h1.pop()
                tmp1.append(node.val)
                if node.left:
                    h2.append(node.left)
                if node.right:
                    h2.append(node.right)
            if tmp1:
                res.append(tmp1)

            tmp2 = []
            while h2:
                node = h2.pop()
                tmp2.append(node.val)
                if node.right:
                    h1.append(node.right)
                if node.left:
                    h1.append(node.left)
            if tmp2:
                res.append(tmp2)
        return res