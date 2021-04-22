#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom2(self, root: TreeNode) -> List[List[int]]:
        # 利用hashmap来存储每层level的节点值
        res_map = defaultdict(list)

        def dfs(node, level):
            # 如果已经到达叶子节点
            if node is None:
                return
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            res_map[level].append(node.val)

        dfs(root, 0)
        # 然后根据题意，将hashmap按照level逆序输出为二阶矩阵
        res = sorted(res_map.items(), key=lambda x: x[0], reverse=True)
        res = [temp[1] for temp in res]
        return res

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # 利用hashmap来存储每层level的节点值
        res = []

        def dfs(node, level):
            # 如果已经到达叶子节点
            if node is None:
                return
            # 如果此时的深度刚好和res数组的长度相同，则创建新的当层的存储列表
            if level == len(res):
                res.append([])
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            res[level].append(node.val)

        dfs(root, 0)
        return res[::-1]

    def levelOrderBottom3(self, root: TreeNode) -> List[List[int]]:
        levelOrder = list()
        if not root:
            return levelOrder

        q = deque([root])
        while q:
            level = list()
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levelOrder.append(level)

        return levelOrder[::-1]
# @lc code=end
