#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid ** 2 < x:
                l = mid + 1
                ans = mid
            elif mid ** 2 > x:
                r = mid - 1
            else:
                return mid
        return ans

    def mySqrt2(self, x: int) -> int:
        p = 1
        if x < 0:
            return None
        elif x > 1:
            l = 1
            r = x / 2
        else:
            l = 0
            r = x + 0.25
        while l < r:
            mid = (l + r) / 2
            current_num = mid ** 2
            if abs(current_num - x) <= p:
                return current_num
            elif current_num < x:
                l = mid
            else:
                r = mid
# @lc code=end
