#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        def dfs(node, level):
            # 如果遍历到叶子节点，那么直接返回
            if node is None:
                return
            # 如果当前level刚好和res结果数组存储的结果长度相同，代表需要新增一个[]储存当前层数的值
            if level == len(res):
                res.append([])

            res[level].append(node.val)
            # 为了保证能是锯齿形的输出，那么在偶数层的时候需要反转，即从右往左存储
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        for index in range(len(res)):
            # 为了保证能是锯齿形的输出，那么在偶数层的时候需要反转，即从右往左存储
            if index % 2 != 0:
                res[index] = res[index][::-1]

        return res
# @lc code=end

