#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """贪心算法，直接遍历，"""
        nums = len(gas)
        # 处理特殊情况
        if nums == 0:
            return -1
        # 遍历消耗数组，以每一个值作为起点
        for i in range(nums):
            remain = gas[i] - cost[i]
            # 如果当前车站的汽油存储不足以支撑到达下一个车站，则此处不能充当起点
            if remain < 0:
                continue
            flag = 0
            # 如果可以则继续判断之后的加油站汽油是否够用
            for j in range(i + 1, nums):
                # 此时的剩余因为上一个车站的
                cur = remain + gas[j]
                remain = cur - cost[j]
                # 代表到不了下一站，所以以i为起点万会存在有个汽油站无法到达，所以直接break
                if remain < 0:
                    flag = -1
                    break
            # 继续遍历i前面的车站，以保证回到i加油站
            for j in range(0, i):
                # 此时的剩余因为上一个车站的
                cur = remain + gas[j]
                remain = cur - cost[j]
                # 代表到不了下一站，所以以i为起点万会存在有个汽油站无法到达，所以直接break
                if remain < 0:
                    flag = -1
                    break
            if flag == 0:
                return i
        return -1
# @lc code=end

