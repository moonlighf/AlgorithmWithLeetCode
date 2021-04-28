#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        """
            前缀和+二分查找
        """
        nums_length = len(nums)
        # 处理特殊情况
        if nums_length == 0:
            return 0
        # 构建前缀和数组，即nums数组的前n项和，sum_arr[i] = sum(num[:i])
        sum_arr = [0]
        for i in range(nums_length):
            sum_arr.append(sum_arr[-1] + nums[i])
        # 基于前缀和数组，对于每一个起点index利用二分查找，查找到一个值符合target
        res = nums_length + 1
        for index in range(1, nums_length+1):
            # 举例：
            # nums      =  [2,3,1,2,4,3]         target=7
            # sum_arr = [0,2,5,6,8,12,15]
            # 那么当index=2的时候，需要判断的就不是是[5,6,8,12,15]中大于7的最小值，
            # 这里要么将前缀和数组全都减去nums[0]，要么就是目标值全部加上nums[0]
            new_target = target + sum_arr[index - 1] if index > 1 else target
            target_index = self.bin_arr(
                sum_arr, index, nums_length, new_target)
            # 如果返回-1，则代表以当前index为起始索引不存在一个大于等于target的值
            # 如果返回非-1,那么更新最小的索引
            if target_index != -1:
                if target_index - index + 1 < res:
                    res = target_index - index + 1
        # 如果此时res 还是 nums_length + 1，则代表没有符合的
        return res if res != nums_length + 1 else 0

    def bin_arr(self, nums, l, r, target):
        # 利用二分查找从数组nums中找到大于等于target的最小索引位置
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if nums[l] >= target:
            return l
        else:
            return -1

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
            双指针
        """
        nums_length = len(nums)
        # 处理特殊情况
        if nums_length == 0:
            return 0
        # 定义两个指针位于数组的起点
        left, right = 0, 0
        sum_val, res = 0, nums_length + 1
        # 不断右移right指针，直到满足大于目标值
        while right < nums_length:
            sum_val = sum_val + nums[right]
            # 如果此时nums[left]到nums[right]之间的和已经大于目标值，则判断是否更新res值，同时left指针左移
            while sum_val >= target:
                if right - left + 1 < res:
                    res = right - left + 1
                sum_val = sum_val - nums[left]
                left += 1
            right += 1
        return res if res != nums_length + 1 else 0
# @lc code=end
