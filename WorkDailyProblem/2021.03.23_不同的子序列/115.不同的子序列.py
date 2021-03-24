#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res_num = 0

    def numDistinct2(self, s: str, t: str) -> int:
        s_len, t_len = len(s), len(t)

        def back_track(res, s, s_index):
            if len(res) == t_len:
                if "".join(res) == t:
                    self.res_num += 1
            for index in range(s_index, s_len):
                if "".join(res) + s[index] != t[:len(res) + 1]:
                    continue
                res.append(s[index])
                back_track(res, s, index+1)
                res.pop()

        back_track([], s, 0)
        return self.res_num

    def numDistinct(self, s: str, t: str) -> int:
        """动态规划"""
        s_len, t_len = len(s), len(t)
        # 处理特殊情况
        if t_len > s_len:
            return 0
        # 声明dp数组，其中dp[i][j]表示s[i:]子集中中包含t[j:]的个数
        dp = [[0] * (t_len + 1) for _ in range(s_len+1)]
        # 初始化dp数组的边界条件
        # 1，i=m,j!=n，则s[i:]为空字符串，一定不会包含t[j:]
        for index in range(t_len):
            dp[s_len][index] = 0
        # 2，i!=m,j=n，则t[j:]为空字符串，是任何字符串的子集
        for index in range(s_len + 1):
            dp[index][t_len] = 1
        # 遍历，更新dp数组的值
        for i in range(s_len-1, -1, -1):
            for j in range(t_len-1, -1, -1):
                # 如果此时s[i:]的长度小于t[j:]的长度则跳过
                if len(s[i:]) < len(t[j:]):
                    continue
                # 如果是s[i] 和 t[j]不相同的话，代表在s[i+1]的基础上增加的s[i]字符不能构成t[j:]
                if s[i] != t[j]:
                    dp[i][j] = dp[i+1][j]
                # 如果是s[i] 和 t[j]相同，那么则要考虑s[i:]和t[j:]是否匹配
                else:
                    # 如果s[i:]和t[j:]匹配，那么考虑，t[j+1: ]是s[i+1:]的子序列，dp[i][j]  = dp[i+1][j+1]
                    # 如果s[i:]和t[j:]不匹配，那么考虑，t[j: ]是s[i+1:]的子序列，dp[i][j]  = dp[i+1][j]
                    dp[i][j] = dp[i+1][j] + dp[i+1][j+1]
        return dp[0][0]
# @lc code=end
