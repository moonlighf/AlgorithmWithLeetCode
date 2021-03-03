#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates2(self, nums: List[int]) -> int:
        index, count = 1, 1
        while index < len(nums):
            if nums[index] == nums[index - 1]:
                count += 1
                if count > 2:
                    nums.pop(index)
                    index -= 1
            else:
                count = 1
            index += 1
        return len(nums)

    def removeDuplicates(self, nums: List[int]) -> int:
        j, count = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j
# @lc code=end
