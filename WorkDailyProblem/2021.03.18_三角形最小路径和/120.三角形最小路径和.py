#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        # 获取三角形的层数
        num = len(triangle)
        # 处理特殊情况，即空三角形和仅有一层的情况
        if num == 0 or (num == 1 and len(triangle[0]) == 0):
            return 0
        if num == 1 and len(triangle[0]) == 1:
            return triangle[0][0]
        # 初始化dp数组表示最短路径和，其中dp[i][j]表示到达第i层第j列（i,j）的最短路径和
        # 那么 dp[i][j] = min(dp[i-1][j], dp[i-1][j-1])  + triangle[i][j]
        dp = [[0] * num for _ in range(num)]
        # 更新dp数组的边界条件
        dp[0][0] = triangle[0][0]
        # 遍历三角形，更新dp数组
        for index in range(1, num):
            # 每一层的最左侧只能由上一侧的最左边移过来
            dp[index][0] = dp[index-1][0] + triangle[index][0]
            # 每一层的最右侧只能由上一侧的最右边移过来
            dp[index][index] = dp[index - 1][index - 1] + triangle[index][index]
            # 由于每层元素个数等于层数（index + 1），
            for j in range(1, index):
                dp[index][j] = min(
                    dp[index-1][j-1], dp[index-1][j]) + triangle[index][j]
        # 那么最终结果则是最后一层的最小值
        return min(dp[num-1])

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 获取三角形的层数
        num = len(triangle)
        # 处理特殊情况，即空三角形和仅有一层的情况
        if num == 0 or (num == 1 and len(triangle[0]) == 0):
            return 0
        if num == 1 and len(triangle[0]) == 1:
            return triangle[0][0]
        # 初始化dp数组表示最短路径和，其中dp[i][j]表示到达第i层第j列（i,j）的最短路径和
        # 那么 dp[i][j] = min(dp[i-1][j], dp[i-1][j-1])  + triangle[i][j]
        # 但是，我们发现dp[i][j]只和之前一层有关，所以只需要存储前一层的值即可
        # dp_pre 表示到达上一层的每个点的最短路径和
        # dp_cur 表示到达当前层的每个点的最短路径和
        # 则dp_cur[i] = min(dp_pre[i], dp[i-1]) + triangle[cen][i]
        dp_pre = [0] * num
        dp_cur = [0] * num
        # 更新dp数组的边界条件
        dp_pre[0] = triangle[0][0]
        # 遍历三角形，更新dp数组
        for index in range(1, num):
            # 每一层的最左侧只能由上一侧的最左边移过来
            dp_cur[0] = dp_pre[0] + triangle[index][0]
            # 每一层的最右侧只能由上一侧的最右边移过来
            dp_cur[index] = dp_pre[index-1] + triangle[index][index]
            for j in range(1, index):
                dp_cur[j] = min(dp_pre[j], dp_pre[j-1]) + triangle[index][j]
            # 注意这里要深度拷贝
            dp_pre = dp_cur[:]
        # 那么最终结果则是最后一层的最小值
        return min(dp_cur)
# @lc code=end
