#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        # 处理特殊情况
        if n < 1:
            return 0
        # 利用digital表示当前数位，例如1表示个位，10表示十位，100表示百位
        digital = 1
        # 根据digital取出每个数位的当前值和前缀和后缀
        # 初始化为个位， 例如n为1234， 那么此时的前缀high为123， 当前数位cur为4，后缀low为0
        # 如果是十位的话，则三个值分别为12，3，4
        high, cur, low = n // 10, n % 10, 0
        res = 0
        # 只要前缀和当前数位有一个不为0，就可以继续循环
        while high != 0 or cur != 0:
            # 假设当前数位是十位，如果当前数位值为0，例如1204，那么，十位为1的情况有 0010-1119之间的数
            # 忽略十位，即000-119 共计 120个数（即固定十位为1，那么千位+百位可以从00变化到11，共计12中情况，个位从0变化到9，共计10中情况），
            # 即 12 * 10 = high * digital
            if cur == 0:
                res += high * digital
            # 假设当前数位是十位，如果当前数位值为1，例如1214，那么，十位为1的情况有 0010-1213之间的数
            # 忽略十位，即000-123，共计124个数
            # 即 (high + 1) * digital
            elif cur == 1:
                res += high * digital + low + 1
            else:
                res += (high + 1) * digital
            # 数位前移，
            low += cur * digital
            cur = high % 10
            high = high // 10
            # 继续下一位数位，即数位扩大十倍
            digital *= 10
        return res
# @lc code=end

