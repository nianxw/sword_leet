'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

# 1. 中序遍历，首尾相连
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        res = []
        s = []
        while s or root:
            while root:
                s.append(root)
                root = root.left
            if s:
                node = s.pop()
                res.append(node)
                root = node.right
        cur = res[0]
        head = cur
        for i in range(1, len(res)):
            node = res[i]
            cur.right = node
            node.left = cur
            cur = cur.right
        head.left = cur
        cur.right = head
        return head


# 2. 直接递归原函数，因为头节点包含了其尾节点的信息

class Solution(object):
    def treeToDoublyList(self, root):
        if not root:
            return None
        left = self.treeToDoublyList(root.left)
        right = self.treeToDoublyList(root.right)
        if not left and not right:
            root.left = root
            root.right = root
            return root
        elif not left:
            root.right = right
            root.left = right.left
            right.left.right = root
            right.left = root
            return root
        elif not right:
            root.left = left.left
            root.right = left
            left.left.right = root
            left.left = root
            return left
        else:
            root.left = left.left
            root.right = right
            left.left.right = root
            left.left = right.left
            right.left.right = left
            right.left = root
            return left
