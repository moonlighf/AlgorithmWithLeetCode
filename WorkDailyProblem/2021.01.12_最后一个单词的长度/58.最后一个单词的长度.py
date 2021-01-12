#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_len = len(s)
        word_len = 0
        last_word_len = 0
        for index in range(s_len):
            if s[index] == " ":
                if word_len != 0:
                    last_word_len = word_len
                word_len = 0
            else:
                word_len += 1

        if word_len == 0 and last_word_len != 0:
            return last_word_len
        return word_len
# @lc code=end
