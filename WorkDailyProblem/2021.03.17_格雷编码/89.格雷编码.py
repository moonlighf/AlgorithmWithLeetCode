#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        # 根据输入的n位数，那么最大能表示的数G(n) = 2^n - 1，集合一共包含 G(n) = 2^n 个元素
        # 处理特殊情况
        if n == 0:
            return [0]
        res = []
        for i in self.helper(n):
            # 二进制转换为十进制
            res.append(int(i, 2))
        return res

    def helper(self, n):
        result = []
        if n == 1:
            return ["0", "1"]
        elif n > 1:
            # n级的编码的生成，是从n - 1 级编码的最后一个编码开始倒序遍历，
            # 每遍历一个编码，就将这个编码 + 1 后的码字添加到结果列表的后面，
            # 然后再将这个编码 + 0，放于原位。
            result = self.helper(n - 1)
            index = len(result) - 1
            while index >= 0:
                temp = result[index]
                temp += "1"
                result.append(temp)
                result[index] += "0"
                index -= 1
        return result
# @lc code=end

