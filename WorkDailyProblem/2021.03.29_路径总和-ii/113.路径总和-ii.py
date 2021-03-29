#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        # 处理特殊情况
        if root is None:
            return []
        # 初始化最终结果列表和每次遍历的结果列表
        res, temp_res = [], [root.val]

        def dfs(temp_node, temp_target):
            # 如果到达叶子节点，即可以判断是否和指定target相等，如果是，则添加到res中
            if temp_node.left is None and temp_node.right is None:
                if temp_target == targetSum:
                    res.append(temp_res[:])
                return
            # 如果没有到达叶子节点，则递归的将左右子树进行相加
            elif temp_node.right is None and temp_node.left is not None:
                temp_res.append(temp_node.left.val)
                dfs(temp_node.left, temp_target + temp_node.left.val)
                temp_res.pop()
            elif temp_node.right is not None and temp_node.left is None:
                temp_res.append(temp_node.right.val)
                dfs(temp_node.right, temp_target + temp_node.right.val)
                temp_res.pop()
            else:
                temp_res.append(temp_node.left.val)
                dfs(temp_node.left, temp_target + temp_node.left.val)
                temp_res.pop()
                temp_res.append(temp_node.right.val)
                dfs(temp_node.right, temp_target + temp_node.right.val)
                temp_res.pop()
            return

        dfs(root, root.val)
        return res
# @lc code=end

