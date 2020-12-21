#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        flag = 0
        for index in range(nums_len):
            if nums[index] == target:
                return index
            if nums[index] > target and flag == 0:
                return index
        return nums_len
# @lc code=end
