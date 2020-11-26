'''
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。
'''

# 1. BFS

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        height = 1
        q = [root]

        while q:
            size = len(q)
            for i in range(size):
                cur_node = q.pop(0)
                if cur_node.left == None and cur_node.right == None:
                    return height
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            height += 1


# 2. DFS

class Solution1(object):
    def minDepth(self, root):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        min_depth = 10**9
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)
        
        return min_depth + 1