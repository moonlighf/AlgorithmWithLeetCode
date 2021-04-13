#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # 原字符串处理两边的空格
        s = s.strip()
        # 字符串根据空格分割
        s_arr = s.split(" ")
        res = ""
        # 去除因为多个空格导致的数组中的空字符串的元素， 然后逆序拼接
        for index in range(len(s_arr)-1, -1, -1):
            if s_arr[index] != "":
                res = res + " " + s_arr[index]
        return res.strip()
# @lc code=end
