#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 获取数组长度
        nums_length = len(nums)
        # nums_length长度的数组最多只能表示nums_length个正整数，则缺少的最小正整数一定位于[1,nums_length + 1]
        # 遍历数组，将[1, nums_length]之间数n放到指定下标处，满足 nums[n-1] = n
        for index in range(nums_length):
            # 注意这里不能直接使用if，不然无法处理[3,4,-1,1]这种情况，因为原数组修改带来的影响
            # 通过while就可以循环到完全符合要求，因为此处的while是常数级，所以整体还是O(N)
            while 1 <= nums[index] <= nums_length and nums[nums[index] - 1] != nums[index]:
                nums[nums[index] - 1], nums[index] = nums[index], nums[nums[index] - 1]
        # 此时理论上nums已经满足nums[n-1] = n的关系，所以再次遍历，如果不满足，则证明缺失了其中某个值
        for index in range(nums_length):
            if nums[index] != index + 1:
                return index + 1
        return nums_length + 1
# @lc code=end
