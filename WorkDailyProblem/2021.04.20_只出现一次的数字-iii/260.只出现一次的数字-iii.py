#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 对所有数值进行一次异或操作，由于异或的特性，那么相同的值的异或值为0，最终结果即为两个目标值的异或值
        res = nums[0]
        for index in range(1, len(nums)):
            res = res ^ nums[index]
        # 根据异或的计算方法，相同位置如果相同则为0，不同则为1，所以对于res（用二进制表示），其各个数位用xi表示，那么则有
        # （1）如果xi=1，则表示两个目标值ai和bi当前数位值不同
        # （2）如果xi=0，则表示两个目标值ai和bi当前数位值相同
        # 据此，将两个目标值分到两个组内，这里我们选取最低不为0的位作为判断
        div = 1
        while div & res == 0:
            div <<= 1
        a, b = 0, 0
        # 然后分组之后的，各自组包括一个目标值和多个相同值，这样对该组进行全体异或即可
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]
# @lc code=end
