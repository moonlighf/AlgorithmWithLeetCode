#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 处理特殊情况
        if matrix is None or len(matrix) == 0:
            return None
        # 获取矩阵的行列
        row, col = len(matrix), len(matrix[0])
        # 遍历矩阵，找到为0的元素
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "a":
                    continue
                if matrix[i][j] == 0:
                    # 将该行和列不为0的元素修改为 "a"
                    for inner_j in range(col):
                        matrix[i][inner_j] = "a" if matrix[i][inner_j] != 0 else 0
                    for inner_i in range(row):
                        matrix[inner_i][j] = "a" if matrix[inner_i][j] != 0 else 0
        # 遍历矩阵，将所有为a的元素替换为0:
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "a":
                    matrix[i][j] = 0
# @lc code=end
