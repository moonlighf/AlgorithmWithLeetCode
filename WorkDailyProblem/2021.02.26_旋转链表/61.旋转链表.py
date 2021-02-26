#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 处理特殊情况
        if head is None or head.next is None or k == 0:
            return head
        head_back = head
        # 初始化node_num用于统计该链表的长度
        node_num = 1
        # 遍历链表找到链表的尾部
        while head.next is not None:
            head = head.next
            node_num += 1
        # 此时链表尾部和链表头部相连，构成循环链表
        head.next = head_back
        # 根据K值找到新的链表（旋转后链表）的头和尾
        # 这里需要注意的是实际需要旋转的次数为k和链表长度相除的余数，因为每node_num次旋转就会恢复原样
        k = k % node_num
        new_tail = node_num - k
        # 遍历链表，然后找到新链表的尾部，让其指向null
        for index in range(new_tail):
            head = head.next
            index += 1
        new_head = head.next
        head.next = None
        return new_head

    def rotateRight2(self, head: ListNode, k: int) -> ListNode:
        # 处理特殊情况
        if head is None or head.next is None or k == 0:
            return head
        # 初始化一个双端队列，允许在队列的头和队列的尾进行插入和删除操作
        dq = deque()
        # 初始化node_num用于统计该链表的长度
        node_num = 0
        # 循环链表，将每个端点值放入双端链表
        while head is not None:
            dq.append(head.val)
            head = head.next
            node_num += 1
        # 根据k值进行重新排序，这里需要注意的是实际需要旋转的次数为k和链表长度相除的余数
        k = k % node_num
        # 根据实际旋转次数进行链表的旋转，即将对队列末尾的元素放到队头
        while k > 0:
            dq.appendleft(dq.pop())
            k -= 1
        # 根据此时的队列重建链表
        temp = ListNode(dq[0])
        ans_node = temp
        for index in range(1, node_num):
            temp.next = ListNode(dq[index])
            temp = temp.next
        return ans_node
# @lc code=end
