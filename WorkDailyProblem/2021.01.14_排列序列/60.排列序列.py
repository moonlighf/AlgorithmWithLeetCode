#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 生成阶乘对应的数组，数组值代表下标index的阶乘，即a[n] = n!
        factorial_ary = [1 for _ in range(n + 1)]
        for index in range(2, n + 1):
            factorial_ary[index] = factorial_ary[index - 1] * index
        # 存储路径
        track = []
        # 判断数字是否使用
        used = [False for _ in range(n + 1)]
        # 记录回溯的次数，也就是路径树的层数
        level = 0
        path = self.back_track(n, k, track, factorial_ary, used, level)
        return "".join([str(temp) for temp in path])

    def back_track(self, n, k, track, factorial_ary, used, level):
        # 回溯到树的底部的条件
        if len(track) == n:
            return
        # 记录全排列的数，注意，这里就是精髓的地方，不通过回溯，直接通过数学的方法来提前算出该条路径的数量
        # 因为n的全排列的个数是n!，所以回溯时候一旦确定一个节点，就能知道该路径有多少个数，从而和k比较判断该路径是否还需要回溯
        cnt = factorial_ary[n - 1 - level]
        for i in range(1, n + 1):
            # 代表该数已经被使用： 和之前通过 if i in track 判断是同样的目的
            if used[i]:
                continue
            # 如果此时的该条路径的回溯的次数大于k值，那么代表我们最后需要的值一定在此次回溯中，否则可以跳过此次回溯
            if cnt < k:
                k -= cnt
                continue
            track.append(i)
            used[i] = True
            self.back_track(n, k, track, factorial_ary, used, level + 1)
            # 直接return，后面的数没必要尝试
            return track
# @lc code=end
