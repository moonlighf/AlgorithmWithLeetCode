#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """由于出现了重复元素，那么之前找拐点的思路就存在问题，因为可能出现没有大小关系的拐点，例如[2,2,2,2]"""
        nums_length = len(nums)
        # 处理特殊情况
        if nums_length == 1:
            return nums[0]
        # 初始化二分法的起点
        left, right = 0, nums_length - 1
        # 如果此时的数组末尾已经大于数组起点，那么证明此数组已经是有序的，否则此时的起点在旋转前应该在末尾的后边
        # 由于可能存在重复元素，那么此处可能相等，但是相等的时候是不能说明有序的，例如[3,4,5,1,2,3]
        # 二分查找整个数组
        while right > left:
            # 如果已经是有序数组，那么直接返回
            if nums[right] > nums[left]:
                return nums[left]
            # 首先确定数组的中点
            mid = left + (right-left) // 2
            # 此时还是根据之前的思路需要确定下一步查找的范围
            # 如果中点值大于left值，代表左边[left: mid+1]是有序的，那么最小值一定出现在右边
            if nums[mid] > nums[left]:
                left = mid + 1
            # 如果中点值小于left值，代表左边[left: mid+1]是无序的，那么最小值一定出现在左边
            elif nums[mid] < nums[left]:
                right = mid
            # 如果中点值等于left值，则此时是无法判断是应该在左边区间还是右边区间的
            # 但是我们可以知道[left:mid+1]之间的值都等于 nums[left]（nums[mid]）
            # 那么我就可以直接将左边区间边界扩展1个，注意不能直接合并（即left=mid）,例如，[10,1,10,10,10]
            else:
                left = left + 1
        return nums[left]
# @lc code=end
