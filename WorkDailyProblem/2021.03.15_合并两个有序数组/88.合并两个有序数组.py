#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        nums1[:] = []
        # 设置两个指针分别指向num1和num2
        nums1_point, nums2_point = 0, 0
        while nums1_point < m and nums2_point < n:
            # 如果 num1 <= num2
            if nums1_copy[nums1_point] <= nums2[nums2_point]:
                nums1.append(nums1_copy[nums1_point])
                nums1_point += 1
            else:
                nums1.append(nums2[nums2_point])
                nums2_point += 1
        # 代表num2已经遍历完，此时需要将num1剩余的元素拼接到结果数组后面
        if nums1_point < m:
            nums1[nums1_point + nums2_point:] = nums1_copy[nums1_point:]
        # 代表num1已经遍历完，此时需要将num2剩余的元素拼接到结果数组后面
        if nums2_point < n:
            nums1[nums1_point + nums2_point:] = nums2[nums2_point:]

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 设置两个指针分别指向num1和num2, p指针指向num1的末尾
        nums1_point, nums2_point, p = m-1, n-1, m + n - 1
        while nums1_point >= 0 and nums2_point >= 0:
            # 如果 num1 <= num2
            if nums1[nums1_point] <= nums2[nums2_point]:
                nums1[p] = nums2[nums2_point]
                nums2_point -= 1
            # 如果 num1 > num2
            else:
                nums1[p] = nums1[nums1_point]
                nums1_point -= 1
            p -= 1
        # 当num2长度更长时，把num2中缺失的添加到num1中, 例如nums1=[0], m=0, nums2=[1], n=1
        nums1[:nums2_point + 1] = nums2[:nums2_point + 1]

# @lc code=end
