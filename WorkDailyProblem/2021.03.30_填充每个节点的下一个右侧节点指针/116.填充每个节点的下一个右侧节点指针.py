#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        # 初始化队列, 根节点push进队列
        queue = [(root, 0)]
        pre_node, pre_level_num = None, 0
        while queue:
            node, level_num = queue.pop(0)
            # 如果当前的节点和前一个节点处于同一层，且前一个节点不为空，则当前节点的next指向前一个节点
            if level_num == pre_level_num and pre_node is not None:
                node.next = pre_node
            if node.right is not None:
                queue.append((node.right, level_num + 1))
            if node.left is not None:
                queue.append((node.left, level_num + 1))
            pre_node, pre_level_num = node, level_num
        return root


# @lc code=end
