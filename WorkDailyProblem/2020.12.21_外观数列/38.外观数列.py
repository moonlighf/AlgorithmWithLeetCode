#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        # 处理特殊情况以及边界情况
        if n == 1:
            return "1"
        # 获取待描述的字符串
        unhandled_str = self.countAndSay(n-1)
        # 遍历字符串，获取连续相同的字符，然后用指定方法进行描述
        start_str = unhandled_str[0]
        handled_str = ""
        str_count = 0
        for index in range(len(unhandled_str)):
            if unhandled_str[index] != start_str:
                handled_str = handled_str + str(str_count) + start_str
                start_str = unhandled_str[index]
                str_count = 1
            else:
                str_count += 1
        handled_str = handled_str + str(str_count) + start_str
        return handled_str
# @lc code=end
