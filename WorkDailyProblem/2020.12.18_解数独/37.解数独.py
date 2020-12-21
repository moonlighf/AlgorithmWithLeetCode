#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def __init__(self):
        self.valid = False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 通过row[][]数组和col[][]数组以及block[][]数组代表每个数字在每行、每列、每个块是否出现过
        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _a in range(3)] for _b in range(3)]
        spaces = list()
        # 遍历数独数组
        row_num, col_num = len(board), len(board[0])
        for i in range(row_num):
            for j in range(col_num):
                if board[i][j] != ".":
                    row[i][int(board[i][j])-1] = True
                    col[j][int(board[i][j])-1] = True
                    block[i//3][j//3][int(board[i][j])-1] = True
                else:
                    spaces.append((i, j))
        self.dfs(0, spaces, row, col, block, board)

    def dfs(self, pos, spaces, row, col, block, board):
        # 如果已经填充完毕，则将状态判断字段置为True
        if pos == len(spaces):
            self.valid = True
            return

        # 从待填充的位置数组取出待填充的行列号
        i, j = spaces[pos]
        # 遍历1-9开始尝试填充到待填充的位置，因为存储的时候默认减了1，所以遍历0-8
        for digit in range(9):
            # 如果待填充位置所在行列及block都没有此时填入的数字的话（均为False），则认为可能可以填充该数
            if col[j][digit] == row[i][digit] == block[i // 3][j // 3][digit] is False:
                # 将存储属性的列表置为True，作为之后的判断条件
                row[i][digit] = col[j][digit] = block[i // 3][j // 3][digit] = True
                # 修改数独列表，代表已经填入数字
                board[i][j] = str(digit + 1)
                # 开始操作下一个待填充的位置（递归）
                self.dfs(pos + 1, spaces, row, col, block, board)
                # 递归到最后的时候，重新置为False
                row[i][digit] = col[j][digit] = block[i //
                                                      3][j // 3][digit] = False
            if self.valid:
                return
# @lc code=end
