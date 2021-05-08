#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        nums_length = len(ratings)
        # 处理特殊情况
        if nums_length == 0:
            return 0
        # 首选要保证满足每个同学都能分到糖果，所以每个同学初始分到1个糖果
        res_nums = [1 for _ in range(nums_length)]
        # 从前往后遍历，如果出现i+1 > i的话，那么就在i分到糖果的基础上+1，以保证比i同学分到糖果多
        for i in range(1, nums_length):
            if ratings[i] > ratings[i-1]:
                res_nums[i] = res_nums[i-1] + 1
        # 从后往前遍历，从而保证i同学比i+1同学分数高时，分到的糖果多
        for i in range(nums_length-1, 0, -1):
            # 注意，这里可能出现在前一次遍历是，就已经有i-1的同学的糖果多的情况了
            # 例如[1,3,4,5,2]，经过第一次遍历后变成，[1,2,3,4,1]
            # 这样第四位同学此时已经比第五位同学多了，所以在第二次从后往前遍历时，不需要再增加糖果了
            if ratings[i] < ratings[i-1] and res_nums[i-1] <= res_nums[i]:
                res_nums[i-1] = res_nums[i] + 1
        return sum(res_nums)
# @lc code=end
