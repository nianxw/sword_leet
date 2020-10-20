'''
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
'''

# 这类题目一般用栈或者队列就可以
# 按层遍历基本都用队列，一个不够可以用两个
# 深度遍历基本都用栈


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
        :rtype: List[int]
        """
        if not root:
            return []
        help_array = [root]
        res = []
        while help_array:
            node = help_array.pop(0)
            res.append(node.val)
            if node.left:
                help_array.append(node.left)
            if node.right:
                help_array.append(node.right)
        return res