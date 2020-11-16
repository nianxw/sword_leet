'''
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isBalanced_(root)[0]

    def isBalanced_(self, root):

        if not root:
            return True, 0
        
        left = self.isBalanced_(root.left)
        if not left[0]:
            return False, 0
        right = self.isBalanced_(root.right)
        if not right[0]:
            return False, 0
        
        if abs(left[1] - right[1]) > 1:
            return False, 0
        
        return True, max(left[1], right[1]) + 1
