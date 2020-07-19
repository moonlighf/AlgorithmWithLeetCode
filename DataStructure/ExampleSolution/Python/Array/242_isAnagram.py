# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         242_isAnagram
# Description:  242. 有效的字母异位词
# Author:       skymoon9406@gmail.com
# Date:         2020/7/11
# -------------------------------------------------------------------------------
from collections import defaultdict


class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        """
        方法一：可以利用两个长度都为 26 的字符数组来统计每个字符串中小写字母出现的次数，然后再对比是否相等；
        """
        # 处理特殊情况
        if len(s) != len(t):
            return False
        # 声明两个数组来储存输入字符串中字母出现的次数
        s_array, t_array = [0] * 26, [0] * 26
        # 遍历两个字符串来统计字符串中字母出现的次数
        str_len = len(s)
        for i in range(str_len):
            # 通过ord函数转换为ASCII码，直接用下标代表字母的位置
            s_array[ord(s[i]) - ord("a")] += 1
            t_array[ord(t[i]) - ord("a")] += 1
        return True if s_array == t_array else False

    def isAnagram2(self, s: str, t: str) -> bool:
        """
        方法二：可以只利用一个长度为 26 的字符数组，将出现在字符串 s 里的字符个数加 1，而出现在字符串 t 里
        的字符个数减 1，最后判断每个小写字母的个数是否都为 0。
        """
        # 处理特殊情况
        if len(s) != len(t):
            return False
        # 声明一个数组来储存输入字符串中字母出现的次数
        count_num_array = [0] * 26
        # 遍历两个字符串来统计字符串中字母出现的次数
        str_len = len(s)
        for i in range(str_len):
            # 通过ord函数转换为ASCII码，直接用下标代表字母的位置
            count_num_array[ord(s[i]) - ord("a")] += 1
            count_num_array[ord(t[i]) - ord("a")] -= 1
        # 遍历判断每个小写字母的个数是否都为 0
        for i in count_num_array:
            if i != 0:
                return False
        return True

    def isAnagram3(self, s: str, t: str) -> bool:
        """
        方法三：将方法二中的数组转化为哈希表
        """
        # 处理特殊情况
        if len(s) != len(t):
            return False
        # 声明一个哈希表（dict）来储存输入字符串中字母出现的次数
        # 这里为了方便可以使用自带的defaultdict
        count_num_dict = defaultdict(int)
        # 遍历字符串s，统计其字符出现的次数
        for temp_s in s:
            # 因为是使用defaultdict类型的dict，可以直接加减
            count_num_dict[temp_s] += 1
        # 遍历字符串t，统计其字符出现的次数
        for temp_t in t:
            # 因为是使用defaultdict类型的dict，可以直接加减
            count_num_dict[temp_t] -= 1
            if count_num_dict[temp_t] < 0:
                return False
        return True

    def isAnagram4(self, s: str, t: str) -> bool:
        """
        方法四：排序后判断是否相等
        """
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    print(Solution().isAnagram4("anagram", "nagaram"))
