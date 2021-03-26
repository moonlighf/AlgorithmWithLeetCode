#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 递归结束条件
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        # 根据后序遍历确定二叉树的根节点，从而在中序遍历中分割出左子树和右子树
        root_val = postorder[-1]
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        root.left = self.buildTree(inorder[:root_index], postorder[:len(inorder[:root_index])])
        root.right = self.buildTree(inorder[root_index+1:], postorder[len(inorder[:root_index]):-1])
        return root
# @lc code=end

