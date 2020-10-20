'''
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

 

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, target):
        if root == None :
            return([])

        res = []
        def dfs(root, road):
            if root.left == None and root.right == None:
                if sum(road) == target: res.append(road)
                return 
            if root.left != None: dfs(root.left, road+[root.left.val])
            if root.right != None: dfs(root.right, road+[root.right.val])

        dfs(root,[root.val])
        return(res)


node5 = TreeNode(5)
node4 = TreeNode(4)
node11 = TreeNode(11)
node7 = TreeNode(7)
node8 = TreeNode(8)
node13 = TreeNode(13)
node44 = TreeNode(4)
node55 = TreeNode(5)
node1 = TreeNode(1)
node2 = TreeNode(2)

node5.left = node4
node5.right = node8
node4.left = node11
node11.left = node7
node11.right = node2
node8.left = node13
node8.right = node44
node44.left = node55
node44.right = node1

a = Solution()
print(a.pathSum(node5, 22))
