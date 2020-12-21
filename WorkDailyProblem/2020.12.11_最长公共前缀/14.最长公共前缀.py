#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 处理特殊情况
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        # 获取字符串数组中的所有字符串的最小长度
        min_str_length = len(strs[0])
        for temp_str in strs:
            temp_str_length = len(temp_str)
            if temp_str_length <= min_str_length:
                min_str_length = temp_str_length
        if min_str_length == 0:
            return ""
        # 遍历字符串数组中的每个字符传
        m, base_str = 0, strs[0]
        while m < min_str_length:
            for str_index in range(1, len(strs)):
                if strs[str_index][m] != base_str[m]:
                    return base_str[:m]
            m += 1
        return base_str[:m]
# @lc code=end
