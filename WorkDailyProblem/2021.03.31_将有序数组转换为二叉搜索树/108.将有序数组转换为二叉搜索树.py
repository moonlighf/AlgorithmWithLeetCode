#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 要解决该问题首先有两个点需要理解
        # (1)已经从小到大排序的nums刚好是二叉搜索树的中序遍历（左<中<右）
        # (2)保证左右字数节点数尽量相等时构成的二叉树为高度平衡的
        # 基于以上的理解，所以我们只需要找到数组的中间值作为根节点（这样能保证左右子树的节点数尽量相等），左右两边的值分别
        # 作为左右子树，然后递归即可
        nums_length = len(nums)
        # 处理特殊情况
        if nums_length == 0:
            return TreeNode()

        def dfs(left, right):
            if left > right:
                return None
            # 找到中间值，即中位数
            mid = (left + right) // 2
            # 然后递归左右子树即可
            root = TreeNode(nums[mid])
            root.left = dfs(left, mid-1)
            root.right = dfs(mid+1, right)
            return root

        return dfs(0, nums_length - 1)
# @lc code=end

