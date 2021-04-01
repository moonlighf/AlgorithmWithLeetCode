#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # 处理特殊情况
        if root is None:
            return 0
        res = 0

        def dfs(node: TreeNode, temp_str: str):
            if node.left is None and node.right is None:
                # 此时代表已经递归到二叉树的叶子节点（即node为叶子节点），所以将此时的值加上叶子节点的值
                # 然后再加到res中
                nonlocal res
                res += int(temp_str + str(node.val))
                return
            temp_str = temp_str + str(node.val)
            # 这里需要注意的是只有左右子树不为空的时候才需要继续递归，不然会出现None.left的引用
            if node.left is not None:
                dfs(node.left, temp_str)
            if node.right is not None:
                dfs(node.right, temp_str)

        dfs(root, "")
        return res
# @lc code=end
