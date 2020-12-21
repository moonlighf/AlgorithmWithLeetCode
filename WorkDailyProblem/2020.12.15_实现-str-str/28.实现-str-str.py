#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 获取两个字符串的长度
        haystack_len, needle_len = len(haystack), len(needle)
        # 处理特殊情况
        if needle_len == 0:
            return 0
        if needle_len > haystack_len:
            return -1
        # 遍历haystack的每个字符作为起始，然后往后截取needle长度的字符串和needle比较是否相同
        for haystack_index in range(haystack_len):
            if haystack_index + needle_len > haystack_len:
                return -1
            else:
                compared_str = haystack[haystack_index: haystack_index + needle_len]
                if compared_str == needle:
                    return haystack_index
        return -1
# @lc code=end
