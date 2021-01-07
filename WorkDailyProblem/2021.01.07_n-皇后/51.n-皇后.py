#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        # 初始化一个棋盘
        board = [["."] * n for _ in range(n)]
        self.back_track(0, board)
        return self.res

    def generate_board(self, temp_board):
        temp_list = []
        for row in range(len(temp_board)):
            temp_list.append("".join(temp_board[row]))
        return temp_list

    def back_track(self, row, board):
        # 停止的条件，即决策树到达底层，这里是到达棋盘边缘，以每行来看，就是到达最后一行
        if row == len(board):
            self.res.append(self.generate_board(board))
            return
        # 遍历每一列
        for index in range(len(board)):
            # 对于不合法的列号（即和前面的皇后所在行、列、斜行相同）跳过
            if self.valid_index(board, row, index):
                continue
            # 针对合法的列号，此处标记为皇后
            board[row][index] = "Q"
            # 回溯到下一层，此处即到下一行，因为不能在同行，所以此处回溯到下一行
            self.back_track(row + 1, board)
            # 回溯，被放置皇后的位置重新恢复为 "."
            board[row][index] = "."

    def valid_index(self, board, row, col) -> bool:
        # 因为back_track中的代码针对每行最多放置一个皇后，所以不需要对该行是否已经有皇后进行判断
        # 判断该列是否已经有皇后
        for i in range(len(board)):
            if board[i][col] == "Q":
                return True
        # 由于是从上往下， 从左往右开始的，所以只需要判读左上和右上是否出现过皇后
        # 检测 左上
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return True
            i -= 1
            j -= 1
        # 检测 右上
        i, j = row - 1, col + 1
        while i >= 0 and j < len(board):
            if board[i][j] == "Q":
                return True
            i -= 1
            j += 1

        # 如果都没有则返回False
        return False
# @lc code=end
