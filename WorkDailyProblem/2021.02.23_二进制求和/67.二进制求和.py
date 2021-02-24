#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        str_length1, str_length2 = len(a), len(b)
        result = []
        # 初始化计数值和默认的进位数
        index, flag = 0, 0
        while (str_length1 - index) > 0 or (str_length2 - index) > 0:
            if (str_length1 - index) <= 0:
                num1 = 0
                num2 = int(b[str_length2 - index - 1])
            elif (str_length2 - index) <= 0:
                num1 = int(a[str_length1 - index - 1])
                num2 = 0
            else:
                num1 = int(a[str_length1 - index - 1])
                num2 = int(b[str_length2 - index - 1])
            temp_num = num1 + num2 + flag
            flag = temp_num // 2
            current_num = temp_num - flag * 2
            result.insert(0, str(current_num))
            index += 1
        # 遍历完两个字符串，如果此时进位符仍不为0，则最高位补一位1
        if flag != 0:
            result.insert(0, "1")
        return "".join(result)
# @lc code=end

