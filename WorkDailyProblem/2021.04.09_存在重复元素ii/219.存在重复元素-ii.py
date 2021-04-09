#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """暴力方法是直接通过O(n^2)方的两次遍历，这里可以利用哈希表的key的唯一性来进行处理"""
        # 初始化一个hashmap，其key是数组的值，value是数组的索引
        sup_map = dict()
        # 遍历数组，将数值作为哈希表的key
        for index, value in enumerate(nums):
            if value not in sup_map.keys():
                sup_map[value] = index
            else:
                # 判断此时的value是否满足要求
                if abs(sup_map[value] - index) <= k:
                    return True
                # 如果不满足的话，那么就要判断此时的value赋值情况
                # 由于后面的索引index越来越大，所以为了保证索引差小于k，那么得以新的index为准
                else:
                    sup_map[value] = index
        return False
# @lc code=end

