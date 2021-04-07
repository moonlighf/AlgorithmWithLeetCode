#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
            时间复杂度O(n)的算法是直接遍历，然后判断
            但是此处，由于已经是局部有序（因为旋转导致部分有序）的，所以可以考虑二分查找
            此处涉及的性质，对于一个数组nums，如果nums[start] < nums[end]则代表其是有序的，由于有重复元素，所以等于不能说明
        """
        # 处理特殊情况
        length_nums = len(nums)
        if length_nums == 0:
            return False
        if length_nums == 1:
            return nums[0] == target
        # 初始化双指针的位置
        start, end = 0, len(nums) - 1
        while start <= end:
            # 获取中间的位置
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            # 判断目标值是在mid的左边还是右边
            # 如果此时二分中间值和左边区间头相等，则左边缩一
            if nums[start] == nums[mid]:
                start = start + 1
            # 如果此时二分中间值和右边区间尾相等，则右边缩一
            elif nums[mid] == nums[end]:
                end = end - 1
            elif nums[start] < nums[mid]:
                # 证明左边[start, mid]是有序的，此时如果target在左边范围内，则继续二分左边区间
                if nums[start] <= target < nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                # 证明右边[mid, end]是有序的，此时如果target在右边范围内，则继续二分右边区间
                if nums[mid] < target <= nums[end]:
                    start = mid
                else:
                    end = mid
        return False

# @lc code=end
