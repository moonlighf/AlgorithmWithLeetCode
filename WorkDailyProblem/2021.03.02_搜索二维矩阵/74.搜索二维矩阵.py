#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 处理特殊情况
        if matrix is None or len(matrix) == 0:
            return False
        # 获取矩阵的行列
        row, col = len(matrix), len(matrix[0])
        # 由于矩阵最后一列是每行的最大值，所以可以根据target的值判断可能在哪一行
        # 即找到第一个比target大的值
        first_large_index = -1
        for i in range(row):
            if matrix[i][col-1] > target:
                first_large_index = i
                break
            if matrix[i][col-1] == target:
                return True
        # 如果没有找到，即first_large_index = -1 那么代表不存在target可能存在的行
        # 如果有找到，那么则判断该行的最小值（行首元素）是否要小于target值，如果不是，直接返回False
        if first_large_index == -1 or matrix[first_large_index][0] > target:
            return False
        # 然后遍历该行判断是否存在该元素
        for i in range(col):
            if matrix[first_large_index][i] == target:
                return True
        return False
# @lc code=end
