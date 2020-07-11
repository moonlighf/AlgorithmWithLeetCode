# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         24_swapPairs
# Description:  24. 两两交换链表中的节点
# Author:       skymoon9406@gmail.com
# Date:         2020/7/11
# -------------------------------------------------------------------------------


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        1.从链表的头节点 head 开始递归。
        2.每次递归都负责交换一对节点。由 left_node 和 right_node 表示要交换的两个节点。
        3.下一次递归则是传递的是下一对需要交换的节点。若链表中还有节点，则继续递归。
        4.交换了两个节点以后，返回 right_node，因为它是交换后的新头。
        5.在所有节点交换完成以后，我们返回交换后的头，实际上是原始链表的第二个节点。
        """
        # 处理特殊情况
        if head is None or head.next is None:
            return head
        # 声明两个节点作为要交换的节点
        left_node = head
        right_node = head.next

        # 递归交换两个节点， 以交换链表 1->2->3->4->5 为例
        # 递归到最终，则是让3节点的next 指向 5节点，然后让 4 节点的next 指向 3 节点
        # 实际上 right_node.next = left_node 一句完成了当前两个节点的交换，然后返回当前递归局部的头节点，最为上一次递归
        # 的尾部
        # 若是链表长度为偶数，即以交换链表 1->2->3->4 为例
        # 递归到最终，则是让 3 节点的 next 指向 None， 即3节点变成尾节点，然后让 4 节点指向 3 节点，完成交换
        left_node.next = self.swapPairs(right_node.next)
        right_node.next = left_node

        return right_node

    def swapPairs2(self, head: ListNode) -> ListNode:
        """迭代法"""
        # 以处理链表 1->2->3->4->5 为例， 此时为链表增加个伪头部 dump->1->2->3->4->5
        dump = ListNode(-1)
        dump.next = head

        prev = dump
        while head is not None and head.next is not None:
            # 待交换的两个节点
            left_node = head
            right_node = head.next

            # 需要更新 prev.next 指向交换后的头。
            # 首次循环此时操作完后 dump.next 已经指向了原链表的第二个节点，也是最终新链表的头
            # 之后循坏到此时，是让上一次循环交换后的尾部指向此次循环交换后的头部
            prev.next = right_node
            # 交换两个节点
            left_node.next = right_node.next
            right_node.next = left_node

            # 重置head节点保证迭代的正常运行， head指向此次交换后的尾部的下一个节点
            # prev指向此次交换后的尾部
            head = left_node.next
            prev = left_node

        # dump节点的next 仍然指向head，但此时已经是新链表的头部了，也是是原来链表的第二个节点
        return dump.next

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
    res = _solution.swapPairs2(a1)
    _solution.output_ListNode(res)
