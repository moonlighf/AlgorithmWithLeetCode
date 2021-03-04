#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small_link, large_link = ListNode(), ListNode()
        small_link_head, large_link_head = small_link, large_link
        while head is not None:
            # 如果该节点值小于指定值，则拼接到small链表后面
            if head.val < x:
                small_link.next = head
                small_link = small_link.next
            else:
                large_link.next = head
                large_link = large_link.next
            head = head.next
        # 此时两条链表分别代表大于等于指定值的链表和小于指定值的链表
        # 注意的是large链表最后节点需要指向None
        large_link.next = None
        small_link.next = large_link_head.next
        return small_link_head.next
# @lc code=end

