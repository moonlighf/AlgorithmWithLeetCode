#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 处理特殊情况
        if num1 == "0" or num2 == "0":
            return "0"
        # 记录两个字符串的长度
        num1_length, num2_length = len(num1), len(num2)
        ans = "0"
        # 两个指针从字符串末尾向字符串头遍历，模拟对应数位相乘
        # *********************************************************************************
        #        1 2 3 4          1 2 3 4        1 2 3 4           1 2 3 4
        #      x   5 6 7   ->  x        7     x        6        x        5
        #     ----------      ------------ + ----------- * 10 + ----------- * 100
        #        8 6 3 8          8 6 3 8        7 4 0 4           6 1 7 0
        #      7 4 0 4
        #    6 1 7 0
        #   ------------
        #    6 9 9 6 7 8
        # *********************************************************************************
        # 从乘数最后一位开始遍历，分别乘以被乘数的各个数位
        for j in range(num2_length - 1, -1, -1):
            y = ord(num2[j]) - ord('0')
            temp = ""
            next_val = 0
            for i in range(num1_length - 1, -1, -1):
                x = ord(num1[i]) - ord('0')
                res = x * y + next_val
                # 本位值
                current_val = res % 10
                # 进位值
                next_val = res // 10
                temp = str(current_val) + temp
            # 如果被乘数已经遍历到最后一位仍然有进位值，则需要对当前temp补位
            if next_val != 0:
                temp = str(next_val) + temp
            # 此时就和 415 题中的字符串相加成了相同的思路
            ans = self.addStrings(str(temp) + "0" * (num2_length - j - 1), ans)
        return ans

    def addStrings(self, num1: str, num2: str) -> str:
        # 初始化两个指针指向字符串末尾
        i, j, add = len(num1) - 1, len(num2) - 1, 0
        ans = ""
        # 两个指针从字符串末尾向字符串头遍历，模拟对应数位相加
        # 如果num1和num2数位相同，那么i和j同时遍历到头部
        # 如果num1和num2数位不相同，那么先遍历到头部的指针（数位少的数）需要补0
        # 同时需要注意进位的情况，即相同数位相加大于10
        while i >= 0 or j >= 0 or add != 0:
            # 由于不能使用int转数值，所以将字符串通过ord转asc码
            x = 0 if i < 0 else ord(num1[i]) - ord('0')
            y = 0 if j < 0 else ord(num2[j]) - ord('0')
            res = x + y + add
            # 通过取商记录本位的数值
            ans = str(res % 10) + ans
            # 记录需要像前一位进的数值
            add = res // 10
            i, j = i - 1, j - 1
        return ans
# @lc code=end
