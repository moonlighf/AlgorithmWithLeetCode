#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 获取数组的长度，并对数组进行排序
        nums_length = len(nums)
        sorted_nums = sorted(nums)
        # 初始化存储结果的数组，数组第一个值代表最小差距，第二个值代表差距最小的三个数的和
        result = [sys.maxsize, 0]
        # 固定第一个值，然后利用双指针法
        for first_index in range(nums_length):
            # 如果本次循环的第一个数和上次循环的数相同，那么则跳过本次循环，因为循环尝试的三个数必定在上次已经尝试过
            if first_index > 0 and sorted_nums[first_index] == sorted_nums[first_index - 1]:
                continue
            # 利用双指针法来找到两个数，使得这三个数的和减去目标数的绝对值最小
            # 初始化左右指针分别位于第一个数之后和数组的末尾
            left, right = first_index + 1, nums_length - 1
            while left < right:
                sums = sorted_nums[first_index] + \
                    sorted_nums[left] + sorted_nums[right]
                distant = abs(sums - target)
                if distant < result[0]:
                    result[0], result[1] = distant, sums
                # 如果sums < target 则，sums值需要增大， 左指针右移
                if sums < target:
                    left += 1
                # 如果sums > target 则，sums值需要减小， 右指针左移
                if sums > target:
                    right -= 1
                # 如果sums = target 则，sums值即为所求
                if sums == target:
                    return sums
        return result[1]
# @lc code=end
