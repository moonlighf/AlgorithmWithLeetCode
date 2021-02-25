#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 记录不需要合并区间的列表
        without_merge_list, merge_list = [], copy.deepcopy(newInterval)
        # 获取待遍历数组的长度
        arr_length = len(intervals)
        # 遍历数组
        for index in range(arr_length):
            temp_list = intervals[index]
            # 判断该区间是否需要合并
            merge_status = self.judge_merge(temp_list, merge_list)
            if merge_status:
                # 如果需要合并，则更新待合并的区间
                merge_list = copy.deepcopy(merge_status)
            else:
                # 如果不需要合并，则把该区间放到不需要合并的区间列表中
                without_merge_list.append(temp_list)
        # 此时已经获得不需要合并的区间列表和合并完成的区间列表，只需要将合并完成的区间列表添加到其中即可
        # 找到merge_list_left大于的最后一个区间即可，如果没找到则插入到最开始
        max_index = -1
        for index in range(len(without_merge_list)):
            if merge_list[0] > without_merge_list[index][0]:
                max_index = index
        without_merge_list.insert(max_index + 1, merge_list)
        return without_merge_list

    def judge_merge(self, temp1_list, temp2_list):
        """
        判断是否需要合并区间，如果不需要返回false，否则返回合并后的区间
        :param temp1_list:
        :param temp2_list:
        :return:
        """
        # temp2_left > temp1_right  [3, 4]   [5, 6]
        if temp2_list[0] > temp1_list[1]:
            return False
        # temp2_right < temp1_left  [4, 7]   [1, 2]
        if temp2_list[1] < temp1_list[0]:
            return False
        return [min(temp1_list[0], temp2_list[0]), max(temp1_list[1], temp2_list[1])]
# @lc code=end
