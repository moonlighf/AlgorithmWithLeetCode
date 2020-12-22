#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def __init__(self):
        self.result = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates_sorted = sorted(candidates)
        current_sum, current_index, current_result = 0, 0, []
        self.dfs(candidates_sorted, target, current_sum,
                 current_index, current_result)
        # 去除重复的组合
        result = [list(t) for t in set(tuple(_) for _ in self.result)]
        return result

    def dfs(self, nums, target, current_sum, current_index, current_result):
        while current_index < len(nums):
            current_sum += nums[current_index]
            current_result.append(nums[current_index])
            if current_sum == target:
                self.result.append(current_result)
                return
            elif current_sum < target:
                # 注意在作为函数遍历的时候，这里的列表是浅拷贝，递归前后两个对象不是完全独立的
                self.dfs(nums, target, current_sum, current_index +
                         1, copy.deepcopy(current_result))
                current_result.pop()
                current_sum = current_sum - nums[current_index]
            else:
                # 此时已经大于目标值，由于已经排序，后面的值会更大，所以不必再遍历后面的，需要把此时current_result中的最后一位
                # 删除然后从最后一位数值的下标的后一位开始遍历后面数值，即回溯到上一层
                return
            current_index += 1

    def combinationSum3(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(begin, path, residue):
            # 如果此时path路径和 与 target 的差，即residue 刚好为0，则符合要求，加进res数组
            if residue == 0:
                res.append(path[:])
            for index in range(begin, size):
                # 如果此时待加入到path中的数值已经大于residue，则直接跳过后续的待验证值（因为已经排序candidates数组）
                if candidates[index] > residue:
                    break
                # ---------------------------------------------------------------------------------
                # 重点，如果没有这部分代码，则和combinationSum2完成的效果相同，最终的res存在重复元素，需要去重
                # 这里的去重原理
                # 这个方法最重要的作用是，可以让同一层级，不出现相同的元素。即
                #       1
                #      / \
                #     2   2  这种情况不会发生,即[1,2,2,5,6] 时候，递归会出现多次1+2（第一个2）+后续 ,1+2（第二个2）+后续
                #    /     \
                #   5       6
                # 但是却允许了不同层级之间的重复即：
                #       1
                #      /
                #     2      这种情况确是允许的
                #    /
                #   2
                #
                # 为何会有这种神奇的效果呢？
                # 首先 cur-1 == cur 是用于判定当前元素是否和之前元素相同的语句。这个语句就能砍掉例1。
                # 可是问题来了，如果把所有当前与之前一个元素相同的都砍掉，那么例二的情况也会消失。
                # 因为当第二个2出现的时候，他就和前一个2相同了。
                #
                # 那么如何保留例2呢？
                # 那么就用cur > begin 来避免这种情况，你发现例1中的两个2是处在同一个层级上的，
                # 例2的两个2是处在不同层级上的。
                # 在一个for循环中，所有被遍历到的数都是属于一个层级的。我们要让一个层级中，
                # 必须出现且只出现一个2，那么就放过第一个出现重复的2，但不放过后面出现的2。
                # 第一个出现的2的特点就是 cur == begin. 第二个出现的2 特点是cur > begin.
                # ---------------------------------------------------------------------------------
                if index > begin and candidates[index - 1] == candidates[index]:
                    continue

                # 如果此时待加入到path中的数值不大于residue，则考虑加入到path，然后进行递归
                path.append(candidates[index])
                # 递归
                dfs(index + 1, path, residue - candidates[index])
                # 递归完成后的回溯，即从path中pop出最后一个元素，回溯到上一层
                path.pop()

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        res = []
        dfs(0, [], target)
        return res
# @lc code=end
