#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        # 生成一个数字的备选列表
        arr = [i for i in range(1, n+1)]
        self.back_track([], arr, k)
        return self.res

    def back_track(self, track, arr, k):
        if len(track) == k:
            self.res.append(copy.deepcopy(track))
        for num in arr:
            if num in track:
                continue
            if len(track) != 0 and num < track[-1]:
                continue
            track.append(num)
            self.back_track(track, arr, k)
            track.pop()
# @lc code=end
