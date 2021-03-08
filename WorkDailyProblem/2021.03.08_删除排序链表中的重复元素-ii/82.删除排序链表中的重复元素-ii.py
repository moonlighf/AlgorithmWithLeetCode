#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 处理特殊情况
        if head is None or head.next is None:
            return head
        # 给链表增加一个头结点，方便之后使用
        dump_node = ListNode(None)
        dump_node.next = head
        prev = dump_node
        # 初始化两个指针来判断链表节点重复的次数
        cur_node = head
        # 开始遍历链表
        while cur_node is not None:
            next_node = cur_node
            count = 0
            # next_node指针前行，然后找到第一个不相等的节点
            while next_node is not None and next_node.val == cur_node.val:
                count += 1
                next_node = next_node.next
            # 判断此时的计数值
            # 如果大于1，代表相同的节点值超过1个，此时需要删除该重复节点，即prev的next指向此时的next_node
            if count > 1:
                prev.next = next_node
            # 如果不大于1，代表相同的节点值不超过1个，直接跳过
            else:
                prev = cur_node
            # cur 指针和next指针归位，即初始化为同时指向相同位置
            cur_node = next_node
        return dump_node.next
# @lc code=end

