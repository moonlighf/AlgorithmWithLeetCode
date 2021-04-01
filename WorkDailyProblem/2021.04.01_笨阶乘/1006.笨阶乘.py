#
# @lc app=leetcode.cn id=1006 lang=python3
#
# [1006] 笨阶乘
#

# @lc code=start
class Solution:
    def clumsy2(self, N: int) -> int:
        """根据数学运算上的定义实际上就是 * / +后的值作为一个整体，然后依次相减"""
        # 处理特殊情况
        if N == 0:
            return 0
        if N == 1:
            return 1
        res, temp = [], N
        flag = 0
        for num in range(N-1, 0, -1):
            index = N - num
            if index % 4 == 1:
                temp = temp * num
                flag = 1
            elif index % 4 == 2:
                temp = -(-temp // num) if temp < 0 // num else temp // num
                res.append(temp)
                flag = 0
            elif index % 4 == 3:
                res.append(num)
                flag = 0
            else:
                temp = -num
                flag = 1
        # 由于最后一部分可能不到加法位置，所以需要将这部分没存到数组中
        if flag == 1:
            res.append(temp)
        # 第一次遍历完后，res中存储了每个乘除加运算之后的值，然后将这些值相减即可
        target = res[0]
        for index in range(1, len(res)):
            target += res[index]

        return target

    def clumsy(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        res, temp = 0, N
        flag = 0
        for num in range(N-1, 0, -1):
            index = N - num
            if index % 4 == 1:
                temp = temp * num
                flag = 1
            elif index % 4 == 2:
                temp = -(-temp // num) if temp < 0 // num else temp // num
                res += temp
                flag = 0
            elif index % 4 == 3:
                res += num
                flag = 0
            else:
                temp = -num
                flag = 1
        if flag == 1:
            return res + temp
        return res

# @lc code=end
