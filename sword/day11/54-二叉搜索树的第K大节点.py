'''
给定一棵二叉搜索树，请找出其中第k大的节点。
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 反中序遍历到第K个节点
# 右中左
# 1.将右->->->右节点一直压栈
# 2.弹出，移动到其左节点
# 3.如果指向为空，则继续弹出，否则，将其右节点全部压栈


class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None
        count = 0
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.right
            if stack:
                cur_node = stack.pop()
                count += 1
                if count == k:
                    return cur_node
                root = cur_node.left
