#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow3(self, x: float, n: int) -> float:
        # 直接递归，但是当n特别大的时候会超出运行时间限制
        if n == 0:
            return 1.0
        if n > 0:
            return self.myPow(x, n-1) * x
        else:
            return self.myPow(x, n + 1) * (1 / x)

    def myPow2(self, x: float, n: int) -> float:
        # 采用快速幂的方法，举个栗子更好理解，如果需要计算x^77次方
        # 那么我们可以依次计算
        # x^2  x^4  (x^8 * x = x^9)  (x^18 * x = x^19)  x^38 (x^76 * x = x^77)
        # 即每次是前一次的平方，或者是前一次的平方乘以 x
        # 推广到一般情况则有：
        # 需要计算 x^n，那么我们需要计算 x^[n/2], 如果n/2是奇数，那么则需要多乘以 x, 直到 n/2 = 0
        def quick(mi_n):
            if mi_n == 0:
                return 1.0
            y = quick(mi_n // 2)
            return y * y if mi_n % 2 == 0 else y * y * x
        return quick(n) if n > 0 else 1.0 / quick(-n)

    def myPow(self, x: float, n: int) -> float:
        # 快速幂的迭代法，即上面公式从左往右推到
        # 将幂指数表示为2进制，其中为1的数位则是需要多乘以x的位置
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
# @lc code=end
