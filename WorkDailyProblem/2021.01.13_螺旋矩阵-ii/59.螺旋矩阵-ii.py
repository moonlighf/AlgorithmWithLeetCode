#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        right, left, top, bottom = n-1, 0, 0, n-1
        temp_count = 1
        while left <= right and top <= bottom:
            # 从左往右运行
            for col in range(left, right+1):
                res[top][col] = temp_count
                temp_count += 1
            # 从上往下运行
            for row in range(top + 1, bottom + 1):
                res[row][right] = temp_count
                temp_count += 1
            # 避免提前出现超越边界的情况
            if left < right and top < bottom:
                # 从右往左运行
                for col in range(right - 1, left - 1, -1):
                    res[bottom][col] = temp_count
                    temp_count += 1
                # 从下往上运行
                for row in range(bottom - 1, top, -1):
                    res[row][left] = temp_count
                    temp_count += 1
            # 从新修改新的边界值
            right, left, top, bottom = right - 1, left + 1, top + 1, bottom - 1
        return res
# @lc code=end
