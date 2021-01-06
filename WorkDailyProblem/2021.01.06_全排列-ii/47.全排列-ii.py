#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        track = []
        # track 代表已选择的路径列表， choices代表待选择的路径列表
        self.back_track(nums, track, copy.deepcopy(nums))
        return self.res

    def back_track(self, nums, track, choices):
        # 当待选择的路径列表为空时，代表已经回溯到决策树底层，此时直接返回即可
        if len(choices) == 0:
            self.res.append(copy.deepcopy(track))
            return
        # 用于记录同层已经出现的元素，防止重复选择，即防止出现如下情况
        #      1(B)               1(A)
        #    1(A)        和      1(B)
        #  3                   3
        # temp 记录第一层已经出现过1(B)，那么下次出现1(A)的时候则不会回溯其后面的路径，因为这必定会重复
        temp = []
        # 遍历待选择路径列表
        for index in range(len(choices)):
            # 如果已经出现在temp列表中，即表示此条路径必定重复，直接跳过该条路径之后的回溯
            if choices[index] in temp:
                continue
            # 否则加入temp列表，记录该层已经有的选择值
            temp.append(choices[index])
            # 加入选择的路径值到track列表
            track.append(choices[index])
            # 将已经选择的路径值从待选择路径列表中删除，然后进行回溯
            # 由于python中函数参数的引用传递，为防止影响遍历的choices，所以只能深度copy一个新的变量传入回溯
            new_choices = copy.deepcopy(choices)
            new_choices.pop(index)
            self.back_track(nums, track, new_choices)
            # 从路径中删除已经选择的路径值
            track.pop(-1)

# @lc code=end
