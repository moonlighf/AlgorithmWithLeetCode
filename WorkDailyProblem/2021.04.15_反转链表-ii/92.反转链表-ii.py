#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 设置 dummyNode 是这一类问题的一般做法
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node

        # 以链表  1-2-3-4-5 为例
        # S1: pre, cur, next = 1,2,3
        # S2: pre -> cur.next   cur -> next.next   next -> cur

        # 快进到开始处理的节点的前两个节点
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        # 开始处理 left 到 right 中间的数据
        # 经过第一次处理后，链表变成 1-3-2-4-5，此时的 pre, cur, next = 1,2,3 仍然成立，所以需要新的初始化next为cur.next
        # 此时需要 1-4 2-5  4-3
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy_node.next
# @lc code=end

