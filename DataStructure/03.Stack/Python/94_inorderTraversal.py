# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         94_inorderTraversal
# Description:  
# Author:       skymoon9406@gmail.com
# Date:         2020/8/8
# -------------------------------------------------------------------------------


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal3(self, root: TreeNode):
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

    def inorderTraversal2(self, root: TreeNode):
        # 递归
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal(self, root: TreeNode):
        # 迭代
        res, stack = [], []
        curr = root
        while curr is not None or len(stack) > 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            # 从栈中取出节点存入res
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res


if __name__ == '__main__':
    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(3)
    a4 = TreeNode(4)
    a5 = TreeNode(5)
    a1.left = a2
    a1.right = a3
    a2.left = a4
    a3.right = a5
    print(Solution().inorderTraversal(a1))