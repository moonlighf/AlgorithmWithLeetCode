#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res = 0

    def totalNQueens(self, n: int) -> int:
        board = [["."] * n for _ in range(n)]
        self.back_track(0, board)
        return self.res

    def back_track(self, row, board):
        if row == len(board):
            self.res += 1
            return
        for col in range(len(board)):
            if self.valid_board(board, row, col):
                continue
            board[row][col] = "Q"
            self.back_track(row + 1, board)
            board[row][col] = "."

    def valid_board(self, board, row, col):
        n = len(board)
        # 列
        for i in range(n):
            if board[i][col] == "Q":
                return True
        # 左上
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return True
            i -= 1
            j -= 1
        # 右上
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return True
            i -= 1
            j += 1

        return False

# @lc code=end
