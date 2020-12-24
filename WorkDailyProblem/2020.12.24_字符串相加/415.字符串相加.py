#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
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
