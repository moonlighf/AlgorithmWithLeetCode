#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
from typing import List


class Solution:
    def jump2(self, nums: List[int]) -> int:
        # 超时！！！ 时间复杂度O(n……2)

        # 获取数组的长度
        nums_len = len(nums)
        # 初始化最长位置数组，代表每个位置所能到达的最远位置
        dp_max = [0] * nums_len
        for i in range(nums_len):
            dp_max[i] = i + nums[i]
        # 初始化dp数组，其中dp[i]表示到达位置i所需要的最少步骤，
        # 那么dp[i]就等于能到达 i 位置的位置的最小值值，即 dp[i] = min(dp[能到达 i 位置的位置] + 1)
        # 最终的结果即为 dp[nums_len-1]
        dp = [0] * nums_len
        for i in range(1, nums_len):
            start_index = i - 1
            min_step = dp[start_index]
            # 往前遍历找到能跳到位置 i 的其他下标
            # 然后记录这些到达这些下标的最小值
            while start_index >= 0:
                if dp_max[start_index] >= i and dp[start_index] <= min_step:
                    min_step = dp[start_index]
                start_index -= 1
            # dp[i]就等于能到达 i 位置的位置的最小步骤 + 1
            dp[i] = min_step + 1
        return dp[nums_len-1]

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_index, end, step = 0, 0, 0
        # 贪心的正向遍历
        # 因为已经知道必定能倒到达最后一个位置，所以尽量每一步到达更远的位置
        # 例如[2, 3, 1 ,2, 4, 2, 3]， 从下标0开始，能到达的最远位置为2，但由于其中下标1的时候能最远下标4
        # 所以为了满足尽可能用最少的步骤走最远的路，应该先到下标1再到下标4
        for i in range(n - 1):
            # max_index代表当前能到达的最远位置
            if max_index >= i:
                max_index = max(max_index, i + nums[i])
                # end 代表边界，当到达变边界的时候步骤需要+1，代表要从这里面选一个下标来跳跃，新的边界就是
                # 此时已经遍历的下标中能到达的最远位置
                if i == end:
                    end = max_index
                    step += 1
        return step
# @lc code=end
