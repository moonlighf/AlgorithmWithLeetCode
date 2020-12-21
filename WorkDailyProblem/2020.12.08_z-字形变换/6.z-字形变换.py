#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        str_length = len(s)
        # 初始化一个空数组用于存储z字形的字符
        # 最大列数的计算方法：如图A和B为一个整体，即最大列数为 A或B这样整体数 * (n-2)
        #    A       B
        #    A    A  B    B  ......
        #    A  A    B  B
        #    A       B
        max_col = (int((str_length / (numRows + numRows - 2))) +
                   1) * (numRows - 1)
        matrix = [[0] * max_col for _ in range(numRows)]
        # 遍历字符串，按照z字型进行数组的填充
        i, j, c = 0, 0, 0
        while c < str_length:
            while i < numRows and c < str_length:
                matrix[i][j] = s[c]
                i += 1
                c += 1
            i -= 2
            while i >= 0 and c < str_length:
                j += 1
                matrix[i][j] = s[c]
                c += 1
                i -= 1
            i += 2
        result = ""
        # 遍历数组，构建结果字符串
        for i in range(numRows):
            for j in range(max_col):
                if matrix[i][j] != 0:
                    result = result + matrix[i][j]
        return result
# @lc code=end
