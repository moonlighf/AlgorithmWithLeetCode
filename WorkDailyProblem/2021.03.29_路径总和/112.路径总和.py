#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = False
        
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # 处理特殊情况
        if root is None:
            return False
        # 初始化结果值为False，如果有出现满足的情况，则修改为True

        def dfs(temp_node, temp_target):
            # 如果到达叶子节点，即可以判断是否和指定target相等，如果是，则修改res
            if temp_node.left is None and temp_node.right is None:
                if temp_target == targetSum:
                    self.res = True
                return
            # 如果没有到达叶子节点，则递归的将左右子树进行相加
            elif temp_node.right is None and temp_node.left is not None:
                dfs(temp_node.left, temp_target + temp_node.left.val)

            elif temp_node.right is not None and temp_node.left is None:
                dfs(temp_node.right, temp_target + temp_node.right.val)

            else:
                dfs(temp_node.left, temp_target + temp_node.left.val)
                if self.res is True:
                    return
                dfs(temp_node.right, temp_target + temp_node.right.val)
            return

        dfs(root, root.val)
        return self.res
# @lc code=end

