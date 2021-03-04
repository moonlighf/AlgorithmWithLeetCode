#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        head_temp = head
        while head.next is not None:
            next_val = head.next.val
            if head.val == next_val:
                head.next = head.next.next
            else:
                head = head.next
        return head_temp
# @lc code=end
