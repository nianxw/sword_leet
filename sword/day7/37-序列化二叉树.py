'''
请实现两个函数，分别用来序列化和反序列化二叉树。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
'''


# 1.dfs的方法
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.

#         :type root: TreeNode
#         :rtype: str
#         """
#         if not root:
#             return '#!'
#         left = self.serialize(root.left)
#         right = self.serialize(root.right)
#         return root.val + '!' + left + right

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.

#         :type data: str
#         :rtype: TreeNode
#         """
#         def dfs(s):
#             tmp_s = s.pop(0)
#             if tmp_s == '#':
#                 return None
#             node = TreeNode(tmp_s)
#             node.left = dfs(s)
#             node.right = dfs(s)
#             return node
#         s = data.split('!')
#         return dfs(s)


# 2. BFS的方法

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#!'
        res = ''
        q = [root]
        while q:
            node = q.pop(0)
            if node:
                res += str(node.val) + '!'
                q.append(node.left)
                q.append(node.right)
            else:
                res += '#!'
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '#!':
            return None
        res = data.split('!')
        root = TreeNode(int(res[0]))
        q = [root]
        i = 1
        while i < len(res):
            node = q.pop(0)
            left = res[i]
            right = res[i+1]
            if left != '#':
                node.left = TreeNode(int(left))
                q.append(node.left)
            if right != '#':
                node.right = TreeNode(int(right))
                q.append(node.right)
            i += 2
        return root 