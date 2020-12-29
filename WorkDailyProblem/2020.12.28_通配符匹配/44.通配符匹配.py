#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 获取字符串和匹配模式的长度
        s_len, p_len = len(s), len(p)
        # 初始化动态规划数组dp，其中dp[i][j]代表s的前i个字符串能否被匹配模式p的前j个字符串匹配
        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        # 初始化动态规划数组的边界条件
        # dp[0][0]代表s为空字符串且匹配模式为空
        dp[0][0] = True
        # dp[i][0]表示匹配模式为空，待匹配字符串非空，那么一定无法匹配，即dp[i][0] = False
        # dp[0][j]表示匹配模非空，待匹配字符串为空，那么仅仅只有匹配模式的前j个字符串都为*的时候才能匹配，一旦出现一个不为*，那么之后
        # 的也一定不能匹配
        for j in range(1, p_len + 1):
            if p[j-1] == "*":
                dp[0][j] = True
            else:
                break
        # 遍历，填充dp数组，最后待求值即为dp[s_len][p_len]
        # 如果p[j-1](代表p的第j个字符)为"?", 那么dp[i][j] 仅仅取决于 dp[i-1][j-1]，因为 ? 可以代表任何一个非空字符
        # 如果p[j-1](代表p的第j个字符)为"*", 那么dp[i-1][j] 和 dp[i][j-1]的逻辑与，因为 * 可以代表任何多个字符串
        # 如果p[j-1](代表p的第j个字符)为字母, 那么结果即为 p[j-1] == s[i-1] 和 dp[i-1][j-1]的逻辑与
        for i in range(1, s_len + 1):
            for j in range(1, p_len+1):
                if p[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = p[j-1] == s[i-1] and dp[i-1][j-1]
        return dp[s_len][p_len]
# @lc code=end
