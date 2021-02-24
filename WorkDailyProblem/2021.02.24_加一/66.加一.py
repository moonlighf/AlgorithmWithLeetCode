#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 数组（待加数）的位数
        ary_length = len(digits)
        # 标记进位数
        flag = (digits[ary_length-1] + 1) // 10
        digits[ary_length - 1] = (digits[ary_length - 1] + 1) - flag * 10
        # 从数组倒数第二位（十位）往前遍历
        for index in range(ary_length-2, -1, -1):
            temp = flag
            flag = (digits[index] + flag) // 10
            digits[index] = (digits[index] + temp) - flag * 10
        if flag != 0:
            digits.insert(0, flag)
        return digits
# @lc code=end

