'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
提示：

1 <= board.length <= 200
1 <= board[i].length <= 200
'''

# 回溯法
# 核心：1.每次比较元素是否一致，不一致则退回；2.用矩阵记录访问情况，在退回时，恢复访问记录
# 抽离所有的边界统一进行判断


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word is None or board is None:
            return False
        n = len(board)
        m = len(board[0])
        flag_matrix = [[0 for x in range(m)] for y in range(n)]
        for i in range(n):
            for j in range(m):
                if self.dfs(board, word, i, j, 0, flag_matrix):
                    return True
        return False

    def dfs(self, board, word, i, j, index, flag_matrix):
        if index >= len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if flag_matrix[i][j] == 1 or board[i][j] != word[index]:
            return False

        flag_matrix[i][j] = 1
        if self.dfs(board, word, i+1, j, index+1, flag_matrix) or \
           self.dfs(board, word, i, j+1, index+1, flag_matrix) or \
           self.dfs(board, word, i-1, j, index+1, flag_matrix) or \
           self.dfs(board, word, i, j-1, index+1, flag_matrix):
            return True
        flag_matrix[i][j] = 0
        return False



a = Solution()
r = a.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB")
print(r)








