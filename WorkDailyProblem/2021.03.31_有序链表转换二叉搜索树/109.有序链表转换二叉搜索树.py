#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST2(self, head: ListNode) -> TreeNode:
        # 其实这题和108题将有序数组转换为二叉搜索树很相似，所以也存在以下思路
        # （1）将有序链表转换为有序数组，然后根据108题的方法转换，但该方法会引入额外的O(n)的空间复杂度
        # （2）借用108题的思路，同样是找中点作为根节点，然后左右剩下的值作为左右子树递归

        def get_mid(start: TreeNode, end: TreeNode):
            """获取一个链表的中点，这里采用快慢指针的方法，即快指针是慢指针前进速度的两倍，这样快指针到末尾时，慢指针刚好到中间"""
            fast, slow = start, start
            # end的next可能是None，所以对应偶数情况，需要注意fast.next也不能等于end
            while fast != end and fast.next != end:
                fast = fast.next.next
                slow = slow.next
            return slow

        def dfs(left, right):
            if left == right:
                return None
            # 获取中间节点作为根节点
            mid_node = get_mid(left, right)
            root = TreeNode(mid_node.val)
            root.left = dfs(left, mid_node)
            root.right = dfs(mid_node.next, right)
            return root

        return dfs(head, None)

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def get_link_length(node):
            """获取链表的长度"""
            count_length = 0
            while node is not None:
                count_length += 1
                node = node.next
            return count_length

        def dfs(left, right):
            """直接按照中序遍历"""
            if left > right:
                return None
            mid = (left + right) // 2
            # 初始化根节点，但是因为是中序遍历，此时还没有遍历到根节点，需要到根节点的时候来填充值
            root = TreeNode()
            root.left = dfs(left, mid-1)
            # 声明head不是局部变量,也不是全局变量,而是外部嵌套函数内的变量。
            nonlocal head
            # 填充根节点的值
            root.val = head.val
            head = head.next
            root.right = dfs(mid+1, right)
            return root

        link_length = get_link_length(head)
        return dfs(0, link_length - 1)

# @lc code=end
