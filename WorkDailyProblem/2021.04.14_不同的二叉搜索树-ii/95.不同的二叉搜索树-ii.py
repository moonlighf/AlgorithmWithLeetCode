#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
            由于需要构建二叉搜索，所以可以知道[1,n]序列是其中序遍历，那么以其中任一值作为根节点构建二叉树即可，
        由于每次的根节点不同，所以构建的二叉搜索树一定不同
        """
        # 处理特殊情况
        if n == 0:
            return []

        def bfs(start, end):
            if start > end:
                return [None]

            all_trees = []
            for index in range(start, end+1):
                # 以其中一个值为根节点，那么起左边值作为左子树，右边值作为右子树
                left = bfs(start, index-1)
                right = bfs(index + 1, end)
                # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
                for l in left:
                    for r in right:
                        node = TreeNode(index)
                        node.left = l
                        node.right = r
                        all_trees.append(node)

            return all_trees

        return bfs(1, n)
# @lc code=end

