#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """暴力方法是直接通过O(n^2)方的两次遍历，这里可以利用哈希表的key的唯一性来进行处理"""
        sup_map = defaultdict(int)
        # 遍历数组，将数值作为哈希表的key
        for num in nums:
            sup_map[num] += 1
        # 如果有重复元素，那么其key对应的value就大于1
        for key, values in sup_map.items():
            if values >= 2:
                return True
        return False
# @lc code=end
