#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        # 初始化dp数组和其边界条件，其中dp[i]表示正整数i需要的最小完全平方数
        # 那么 dp[i] = min(dp[i-1], dp[i-4], dp[i-9]...) + 1，即减去所有小于他的完全平方数后的值 + 1
        dp = [float('inf')] * (n+1)
        dp[0], dp[1] = 0, 1
        # 初始化小于n的所有完全平方数
        num_squares = [i * i for i in range(1, int(n**(1/2)) + 1)]
        # 遍历更新dp数组
        for index in range(2, n+1):
            for num_square in num_squares:
                if index < num_square:
                    break
                dp[index] = min(dp[index], dp[index-num_square] + 1)
        return int(dp[n])        
# @lc code=end

