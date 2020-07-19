# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         25_reverseKGroup
# Description:  25. K 个一组翻转链表
# Author:       skymoon9406@gmail.com
# Date:         2020/7/11
# -------------------------------------------------------------------------------


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        1. 将 curr 指向的下一节点保存到 next 指针；
        2. curr 指向 prev，一起前进一步；
        3. 重复之前步骤，直到 k 个元素翻转完毕；
        4. 当完成了局部的翻转后，prev 就是最终的新的链表头，curr 指向了下一个要被处理的局部，
        而原来的头指针 head 成为了链表的尾巴。
        """
        # 初始化三个指针prev，curr，next分别指向头结点的前一个节点，头结点，和头结点的下一个节点
        # 运行过程中分别表示前一个节点，当前节点，下一个节点
        prev = ListNode(-1)
        curr = head
        n = k
        # 判断剩余的数量，剩余数量小于k则不需要反转, 直接将此时的head指向上一次的尾部
        tail = curr
        for i in range(0, k):
            if tail is None:
                return head
            tail = tail.next
        # 完成局部的翻转，以链表1->2->3->4->5为例，
        # 局部翻转后，链表变成 N<-1<-2 3->4->5，curr和next指向了下一个要被处理的局部 3，prev就是最终的新的链表头 2
        while curr is not None and n > 0:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            n -= 1
        # prev成为新的链表头，curr指向了下一个要被处理的局部的第一个元素，原来的头指针head成为了链表的尾巴
        new_head = prev
        # 将上一轮翻转后的尾结点指向下一轮翻转后的头节点
        head.next = self.reverseKGroup(curr, k)
        return new_head

    def output_ListNode(self, head: ListNode):
        """用于输出链表，方便观察是否解法正确"""
        while head is not None:
            print(head.val)
            head = head.next


if __name__ == '__main__':
    # 初始化一个链表
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    a5 = ListNode(5)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    _solution = Solution()
    res = _solution.reverseKGroup(a1, 2)
    _solution.output_ListNode(res)
