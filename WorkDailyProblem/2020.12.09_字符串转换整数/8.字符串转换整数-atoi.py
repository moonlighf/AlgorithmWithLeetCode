#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        i, str_length = 0, len(s)
        # 记录字符串中空格个个数，当然，这里也可以用 lstrip() 函数
        while i < str_length and s[i] == ' ':
            i = i + 1
        # 处理特殊情况，例如空字符串和全都是空格
        if str_length == 0 or i == str_length:
            return 0
        flag = 1
        if s[i] == '-':
            flag = -1
        if s[i] == '+' or s[i] == '-':
            i = i + 1
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        ans = 0
        while i < str_length and '0' <= s[i] <= '9':
            ans = ans * 10 + int(s[i]) - int('0')
            i += 1
            if ans - 1 > INT_MAX:
                break
        ans = ans * flag
        if ans > INT_MAX:
            return INT_MAX
        return INT_MIN if ans < INT_MIN else ans

# @lc code=end
