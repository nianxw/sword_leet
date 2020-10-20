'''
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

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
  [9,20],
  [15,7]
]
'''


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
        res = []
        while h1:
            tmp = []
            for i in range(len(h1)):
                node = h1.pop(0)
                tmp.append(node.val)
                if node.left:
                    h1.append(node.left)
                if node.right:
                    h1.append(node.right)
            res.append(tmp)
        return res