'''
班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
示例 1:
输入: [[1,1,0], [1,1,0], [0,0,1]] 输出: 2 说明：已知学生0和学生1互为朋友，他们在一个朋友圈。 第2个学生自己在一个朋友圈。所以返回2。 示例 2:
输入: [[1,1,0], [1,1,1], [0,1,1]] 输出: 1 说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
'''

# 1.最简单的并查集实现（无优化）

from collections import defaultdict


# 查根
def find(x, parent):
    r = x
    while r != parent[r]:
        r = parent[r]
    return r


def union(x, y, parent):
    x_root = find(x, parent)
    y_root = find(y, parent)
    # 将x作为根节点
    if x_root != y_root:
        parent[y_root] = x_root


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        parent = defaultdict(int) # 字典或者列表都可以
        # parent = [i for i in range(len(M))]  # [0, 1, 2]
        ans = set()
        if not M:
            return 0
        for i in range(len(M)):
            parent[i] = i
        for i in range(len(M)):
            for j in range(i, len(M[0])):
                if M[i][j] == 1:
                    union(i, j, parent)
        # 所有节点的都有哪些情况，一种情况代表一个连通分量
        for i in parent:
            ans.add(find(i, parent))

        return len(ans)


a = Solution()
print(a.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))


# 2.优化

def find1(x, parent):
    r = x
    while r != parent[r]:
        r = parent[r]
    return r


def union1(x, y, parent, size):
    x_root = find1(x, parent)
    y_root = find1(y, parent)
    # 将x作为根节点
    if x_root != y_root:
        if size[x_root] > size[y_root]:
            parent[y_root] = x_root
            size[x_root] += size[y_root]
        else:
            parent[x_root] = y_root
            size[y_root] += size[x_root]

class Solution1(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        parent = defaultdict(int)  # 字典或者列表都可以
        size = defaultdict(int)
        # parent = [i for i in range(len(M))]  # [0, 1, 2]
        ans = set()
        if not M:
            return 0
        for i in range(len(M)):
            parent[i] = i
            size[i] = 1
        for i in range(len(M)):
            for j in range(i, len(M[0])):
                if M[i][j] == 1:
                    union1(i, j, parent, size)
        # 所有节点的都有哪些情况，一种情况代表一个连通分量
        for i in parent:
            ans.add(find(i, parent))

        return len(ans)