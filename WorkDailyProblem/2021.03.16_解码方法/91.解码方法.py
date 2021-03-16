#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        str_length = len(s)
        # 处理特殊情况
        if str_length == 0:
            return 0
        if str_length == 1:
            return 1 if 0 < int(s[0]) < 27 else 0
        # 初始化dp数组 和 边界条件
        dp = [0] * str_length
        dp[0] = 1 if 0 < int(s[0]) < 27 else 0
        if dp[0] == 0:
            dp[1] = 0
        else:
            if int(s[:2]) < 27 and int(s[1]) != 0:
                dp[1] = 2
            if int(s[:2]) >= 27 and int(s[1]) != 0:
                dp[1] = 1
            if int(s[:2]) < 27 and int(s[1]) == 0:
                dp[1] = 1
        # 遍历字符串，填充dp数组
        for index in range(2, str_length):
            if dp[index - 1] == 0:
                dp[index] = dp[index - 1]
            else:
                if int(s[index-1: index + 1]) < 27 and int(s[index]) != 0 and int(s[index-1]) != 0:
                    dp[index] = dp[index - 1] + dp[index - 2]
                elif int(s[index]) == 0 and int(s[index-1: index + 1]) < 27 and int(s[index - 1]) != 0:
                    dp[index] = dp[index - 2]
                elif int(s[index]) != 0:
                    dp[index] = dp[index - 1]
        return dp[str_length-1]
# @lc code=end
