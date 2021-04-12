#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """使用队列，从一端将数组尾部的数出队列，然后从另一端进队列，另一端为原数组的头"""
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
            k < len(nums) 时，其实最终目的就是将数组尾部的k个元素移动到数组的头部
            k >= len(nums)时，则只需要移动 k % len(nums) 个元素即可
        """
        nums_length = len(nums)
        # 处理特殊情况
        if nums_length == 1:
            return

        def reverse(a, start, end):
            i = start
            while i < int(start + (end-start + 1) / 2):
                a[i], a[start + end - 1 - i] = a[start + end - 1 - i], a[i]
                i += 1
            return a

        # 旋转所有数组
        k = k % nums_length
        reverse(nums, 0, nums_length)
        reverse(nums, 0,  k)
        reverse(nums, k, nums_length)
# @lc code=end
