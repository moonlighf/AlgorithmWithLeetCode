#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
            常规解法就是遍历nums，然后判断每个值和其前后是否符合峰值的条件，这种方法时间复杂度为O(n)，但为了达到O(log n)的时间复杂度，
        就只能采用二分法
        """
        nums_length = len(nums)
        # 处理特殊情况
        if nums_length == 1:
            return 0
        if nums_length == 0:
            return None
        # 初始化二分法的左右起点
        start, end = 0, nums_length - 1
        while start < end:
            # 获取中间位置
            mid = start + (end - start) // 2
            # 判断下一步的二分区间是左边还是右边
            # 目前的mid可能出现的情况包括以下四种
            # [1,2,3]       [1,3,2] （和[2,3,1]一样）       [3,2,1]     [3,1,2]（和[2,1,3]一样）
            # 其中只有第二种符合峰值的情况。（注意，我们只考虑局部的情况，整体可能的变化很多）
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            # 如果nums[mid] < nums[mid + 1]则峰值可能出现在后面，注意，此处不能否点峰值可能出现在前面，但由于题目只需要找出一个，
            elif nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1
        return start
# @lc code=end
