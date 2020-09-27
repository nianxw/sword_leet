"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
 

限制：

0 <= 节点个数 <= 5000
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder, inorder):
    if preorder == []:
        return None
    if inorder == []:
        return None
    node = TreeNode(preorder[0])
    index = inorder.index(preorder[0])
    node.left = buildTree(preorder[1: 1+index], inorder[: index])
    node.right = buildTree(preorder[1+index:], inorder[index+1:])
    return node
