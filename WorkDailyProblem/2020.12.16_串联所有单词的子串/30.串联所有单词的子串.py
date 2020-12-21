#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 获取字符串的长度以及单词个数
        str_length, words_num = len(s), len(words)
        # 处理特殊情况
        if words_num == 0:
            return []
        # 获取每个单词的长度，因为每个单词是等长的，所以直接取第一个单词的长度
        word_length = len(words[0])
        # 处理特殊情况
        if words_num * word_length > str_length:
            return []
        # 遍历待查询的字符串
        result = []
        for str_index in range(str_length):
            # 然后以每个字符作为起始字符，往后数单词的长度组成的字符串作为单词，讲指定数量的单词存入数组，然后比较数组和单词数组是否相同
            if str_length - str_index < words_num * word_length:
                break
            compared_words = []
            for num in range(words_num):
                compared_words.append(
                    s[str_index + word_length * num: str_index + word_length * (num+1)])
            # 如果待待比较的数组和单词数组相同，则认为单词数组可以通过某种组合得到
            if sorted(compared_words) == sorted(words):
                result.append(str_index)
        return result
# @lc code=end
