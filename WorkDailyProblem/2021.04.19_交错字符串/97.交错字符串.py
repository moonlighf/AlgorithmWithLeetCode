#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
            动态规划，利用dp[i][j]表示表示s1的前i个字符串 和 s2 的前 j个字符串能否表示s3的前i+j个字符串
        """
        s1_length, s2_length = len(s1), len(s2)
        # 处理特殊情况
        if s1_length + s2_length != len(s3):
            return False
        # 初始化dp数组
        dp = [[False] * (s2_length + 1) for _ in range(s1_length + 1)]
        # dp数组的边界条件初始化
        # s1字符串空字符串和s2字符串空字符，能否组成s3字符串的空字符串，必定为真
        dp[0][0] = True
        # 遍历，填充dp数组
        for inner in range(0, s1_length + 1):
            for outer in range(0, s2_length + 1):
                if inner > 0:
                    # 如果s1[inner] == s3[inner + outer]，代表dp[inner][outer]的值取决于dp[inner-1][outer]
                    if s1[inner - 1] == s3[inner + outer - 1]:
                        dp[inner][outer] = dp[inner - 1][outer]
                if outer > 0:
                    # 如果s2[outer] == s3[inner + outer]，代表dp[inner][outer]的值取决于dp[inner][outer-1]
                    # 这里和dp[inner][outer]求或是为了保证上面处理后dp[inner][outer]已经为真
                    if s2[outer - 1] == s3[inner + outer - 1]:
                        dp[inner][outer] = dp[inner][outer] | dp[inner][outer - 1]
        return dp[s1_length][s2_length]
# @lc code=end
