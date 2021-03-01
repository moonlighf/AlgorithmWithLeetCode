#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid is None or len(obstacleGrid) == 0:
            return 0
        if len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1 and obstacleGrid[0][0] == 0:
            return 1
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        path = [[0] * col for _ in range(row)]
        # 针对第一行初始化矩阵值
        # 如果1不在第一行中，那么到达第一行所有位置的路径都只有一条，如果存在1障碍物（1），则到达障碍物后的位置路径为0条
        if 1 not in obstacleGrid[0][:]:
            for index in range(1, col):
                path[0][index] = 1
        else:
            error_index = obstacleGrid[0].index(1)
            for index in range(1, col):
                path[0][index] = 1 if index < error_index else 0
        # 针对第一列初始化矩阵值，注意不能用obstacleGrid[:][0]来取，只能用numpy来辅助，这里不引入numpy
        first_col = []
        for index in range(row):
            first_col.append(obstacleGrid[index][0])
        if 1 not in first_col:
            for index in range(1, row):
                path[index][0] = 1
        else:
            error_index = first_col.index(1)
            for index in range(1, row):
                path[index][0] = 1 if index < error_index else 0
        for i in range(1, row):
            for j in range(1, col):
                if (obstacleGrid[i][j-1] == 1 and obstacleGrid[i-1][j] == 1) or obstacleGrid[i][j] == 1:
                    path[i][j] = 0
                elif obstacleGrid[i][j-1] != 1 and obstacleGrid[i-1][j] != 1:
                    path[i][j] = path[i - 1][j] + path[i][j-1]
                elif obstacleGrid[i-1][j] == 1:
                    path[i][j] = path[i][j - 1]
                else:
                    path[i][j] = path[i - 1][j]
        return path[row-1][col-1]
# @lc code=end
