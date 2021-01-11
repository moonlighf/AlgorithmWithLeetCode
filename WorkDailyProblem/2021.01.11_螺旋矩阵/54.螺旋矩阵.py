#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 处理特殊情况
        if not matrix or not matrix[0]:
            return list()
        # 获取最大的行数和列数
        max_row, max_col = len(matrix), len(matrix[0])
        # 设置起始的行列号
        row, col = 0, 0
        # 设置起始层数， 以 4 × 4的矩阵为例，则可以看出来第一层是 1-2-3-4-8-12-2-3-1-4-9-5
        # 第二层是 6-7-11-10，
        # 所以针对每层从顺时针遍历矩阵即可， 然后回到起点后增加层数
        # [
        #   [1,  2,  3,  4],
        #   [5,  6,  7,  8],
        #   [9, 10, 11, 12]
        #   [4,  1,  3,  2]
        # ]
        level = 0
        res = []
        while level <= max_row - level - 1 and level <= max_col - level - 1:
            # 从左往右
            for col in range(level, max_col - level):
                res.append(matrix[row][col])
            # 从上往下
            for row in range(level + 1, max_row - level):
                res.append(matrix[row][col])
            # 如果此时已经出现不符合边界的情况，则及时停止，主要是针对行列不相等情况
            # 比如[
            #   [1, 2, 3, 4],
            #   [5, 6, 7, 8],
            #   [9,10,11,12]
            # ]
            # 第二层运行到6-7后，此时不需要接着运行，所以直接跳过从右往左和从下往上的部分
            if level < max_row - level - 1 and level < max_col - level - 1:
                # 从右往左
                for col in range(max_col - level - 2, level - 1, -1):
                    res.append(matrix[row][col])
                # 从下网上
                for row in range(max_row - level - 2, level, -1):
                    res.append(matrix[row][col])
            # 进入下一层
            level += 1
        return res
# @lc code=end
