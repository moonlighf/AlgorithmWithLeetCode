#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin2(self, nums: List[int]) -> int:
        """找到旋转的拐点。由于旋转之前已经升序排列，所以旋转之后的最小值一定出现了既小于前面，又小于后面的情况"""
        nums_length = len(nums)
        # 处理特殊情况
        if nums_length == 1:
            return nums[0]
        for index in range(1, nums_length):
            # 如果刚好在最后的位置，那么只需要小于前面的值即可
            if index == nums_length-1 and nums[index] < nums[index-1]:
                return nums[index]
            # 其他情况只要找到拐点即可，即小于前面也小于后面的
            if nums[index] < nums[index-1] and nums[index] < nums[index + 1]:
                return nums[index]
        # 如果没找到的话，就是最开始那个为最小值
        return nums[0]

    def findMin(self, nums: List[int]) -> int:
        """之前找拐点的方法思路是可取的，但是时间复杂度还可以更优，即采用二分法"""
        nums_length = len(nums)
        # 处理特殊情况
        if nums_length == 1:
            return nums[0]
        # 初始化二分法的起点
        left, right = 0, nums_length - 1
        # 如果此时的数组末尾已经大于数组起点，那么证明此数组已经是有序的，否则此时的起点在旋转前应该在末尾的后边
        if nums[right] > nums[left]:
            return nums[0]
        # 二分查找整个数组
        while right > left:
            # 首先确定数组的中点
            mid = left + (right-left) // 2
            # 然后判断下一次需要查找的数组的范围，是中点右边还是左边
            # 如果中点值大于left值，代表左边[left: mid+1]是有序的，那么最小值一定出现在右边
            if nums[mid] > nums[left]:
                left = mid + 1
            # 如果中点值小于left值，代表左边[left: mid+1]是无序的，那么最小值一定出现在左边
            else:
                right = mid - 1
            # 终止条件，如果出现mid小于前面或者大于后面，则可以直接判断出拐点
            if nums[mid] > nums[mid+1]:
                return nums[mid + 1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
# @lc code=end
