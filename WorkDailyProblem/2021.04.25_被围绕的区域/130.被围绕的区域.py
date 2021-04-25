#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
    # 整体思路：遍历四个边界，找到四边中的 O ，然后用特殊字符进行替换，然后遍历矩阵，将其余的 O全部替换为X，#替换回 O
        row, col = len(board), len(board[0])

        def dfs(x, y):
            if x < 0 or x >= row or y < 0 or y >= col or board[x][y] != "O":
                return
            board[x][y] = "#"
            # 深度遍历该位置的周围四个位置
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        # 遍历第一列和最后一列，找到两个边界中的 O
        for i in range(row):
            dfs(i, 0)
            dfs(i, col - 1)
        # 遍历第一行和最后一行，找到两个边界中的 O
        for j in range(1, col):
            dfs(0, j)
            dfs(row - 1, j)

        # 重新遍历矩阵，将其余的 O全部替换为 X，#替换回 O
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
                else:
                    pass
# @lc code=end

