#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 对于输入的整数带符号的肯定不是回文数
        if x < 0:
            return False
        else:
            # 整数转为字符串便于处理
            x_str = str(x)
            # 字符串倒叙排列为新的字符串， 或者使用python方法 inverted_str = x_str[::-1]
            # 可以使用栈存储遍历之后的数字，这样达到进先出的逆序的效果
            inverted_str = []
            for temp_str in x_str:
                inverted_str.insert(0, temp_str)
            # 栈顺序输出然后判断和整数字符串对应位置是否相同，如果不相同则输出False，否则为True
            for index in range(len(inverted_str)):
                if inverted_str[index] != x_str[index]:
                    return False
            return True
# @lc code=end
