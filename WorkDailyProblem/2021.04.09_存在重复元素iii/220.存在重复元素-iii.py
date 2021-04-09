#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """
            暴力方法是直接通过O(n^2)方的两次遍历
            这里我们采用桶排序的思想，将nums中的数按照[0, t], [t+1, 2t+1]。。。分组策略存到每个桶中
        """
        # 处理特殊情况，测试样例 nums = [1,5,9,1,5,9], k = 2, t = 3
        if len(nums) == 0 or k < 0 or k < 0:
            return False
        # 设置桶的大小，这样利用 num // w 来判断每个值所处的桶的序号
        w = t + 1
        # 初始化一个map存储每个桶
        bub_map = dict()
        for index, num in enumerate(nums):
            # 桶的序号，这里需要考虑下num为负数的情况
            # 桶的序号和对应的范围关系， [bub_index * t + bub_index, bub_index * 2 * t + bub_index]
            bub_index = num // w
            if bub_index in bub_map.keys():
                # 如果bub_index在map中，则代表存在一个数，两者的值相差t，因为在同一个桶中
                return True
            # 由于前一个桶中的值也可能和当前桶的值相差t，比如[0, 3] 中的 2 和 [4, 7]中的 5
            # 如果在前一个桶中，且符合不大于t的条件
            if bub_index - 1 in bub_map and abs(num - bub_map[bub_index - 1]) <= t:
                return True
            # 如果在再一个桶中，且符合不大于t的条件
            if bub_index + 1 in bub_map and abs(num - bub_map[bub_index + 1]) <= t:
                return True
            # 桶存入map
            bub_map[bub_index] = num
            # 始终保证滑动窗口是k，即索引相差不超过k
            if index >= k:
                bub_map.pop(nums[index - k] // w)
        return False
# @lc code=end

