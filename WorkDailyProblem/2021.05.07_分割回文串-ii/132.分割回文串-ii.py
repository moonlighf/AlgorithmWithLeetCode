#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#

# @lc code=start
class Solution:
    def minCut2(self, s: str) -> int:
        """
            获取所有子串，然后判断每个子串是否是回文串，然后返回长度较短的
        """
        str_length = len(s)
        temp_res = []
        res = str_length + 1

        def back_tracking(str_index):
            # 当满足遍历完字符串时，将temp_res写入到res
            if str_index >= str_length:
                nonlocal res
                if len(temp_res) <= res:
                    res = len(temp_res)
                return

            for index in range(str_index, str_length):
                # 如果是回文串则，则将该字符串写入到temp_res中
                if self.helper(s[str_index:index + 1]):
                    temp_res.append(s[str_index:index + 1])
                    # 回溯继续做选择
                    back_tracking(index + 1)
                    # 撤销选择
                    temp_res.pop()

        back_tracking(0)
        return res - 1

    def helper(self, temp: str) -> bool:
        """判断一个字符串是否是回文串"""
        str_length = len(temp)
        if str_length == 0:
            return False
        left, right = 0, str_length - 1
        while left < right:
            if temp[left] == temp[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
    
    def minCut(self, s: str) -> int:
        n = len(s)

        # 设 g(i, j) 表示 s[i..j]是否为回文串
        g = [[True] * n for _ in range(n)]
        # 遍历字符串，填充g数组
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                # 当且的仅当s[i+1,j-1]为回文串，且首尾元素相同时，s[i,j]为回文串
                # 或者为空串时也为回文串，即i > j
                g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]

        # 设 f[i]表示字符串的前缀 s[0..i] 的最少分割次数
        f = [float("inf")] * n
        for i in range(n):
            # 如果s[0...i] 本身就是回文串，那么不需要分割即可得到回文串，即最小f[i] = 0
            if g[0][i]:
                f[i] = 0
            # 如果s[0...i]不是回文串，那么就要遍历这个前缀s[0...i]之间的字符串
            # 考虑最后分割出的回文串，即我们枚举最后一个回文串的起始位置 j+1，保证 s[j+1..i]是一个回文串，
            # 那么 f[i] 就可以从 f[j] 转移而来，附加 1 次额外的分割次数。
            else:
                for j in range(i):
                    if g[j + 1][i]:
                        f[i] = min(f[i], f[j] + 1)

        return int(f[n - 1])
# @lc code=end

