#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a, b = 0, 0
        for num in nums:
            a = (a ^ num) & ~b
            b = (b ^ num) & ~a
        return a

    def singleNumber2(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            mask = 1 << i
            cnt = 0
            for j in range(len(nums)):
                # 利用nums[j] & mask取出每位的值，将等于1的值加起来，因为除了目标值外的值都是k个，那么最终的值一定是
                # kN + 目标值的当前位的值
                if nums[j] & mask != 0:
                    cnt += 1
            # 然后将每位除以 k 取余数即是目标值当前位的值
            if cnt % 3 != 0:
                res |= mask
        return res
# @lc code=end
