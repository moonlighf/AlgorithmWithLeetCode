package com.skymoon;

/** @author skymoon */
public class SolutionSwapPairs {
  private static ListNode swapPairs(ListNode head) {
    // 以处理链表 1->2->3->4->5 为例， 此时为链表增加个伪头部 dump->1->2->3->4->5
    ListNode dump = new ListNode(-1);
    dump.next = head;

    ListNode prev = dump;

    while (head != null && head.next != null) {
      // 待交换的两个节点
      ListNode leftNode = head;
      ListNode rightNode = head.next;

      // 需要更新 prev.next 指向交换后的头。
      // 首次循环此时操作完后 dump.next 已经指向了原链表的第二个节点，也是最终新链表的头
      // 之后循坏到此时，是让上一次循环交换后的尾部指向此次循环交换后的头部
      prev.next = rightNode;
      leftNode.next = rightNode.next;
      rightNode.next = leftNode;

      // 重置head节点保证迭代的正常运行， head指向此次交换后的尾部的下一个节点
      // prev指向此次交换后的尾部
      head = leftNode.next;
      prev = leftNode;
    }
    return dump.next;
  }

  private static ListNode swapPairs2(ListNode head) {
    /*递归法*/
    // 处理特殊情况，也是递归的终止条件
    if (head == null || head.next == null) {
      return head;
    }
    // 声明两个待交换的节点
    ListNode leftNode = head;
    ListNode rightNode = head.next;

    // 利用递归进行交换
    // 交换之后变成 rightNode -> leftNode， 所以传入递归下次交换的应该是rightNode.next
    // 下次递归的结果应该接在本次递归的尾部，即leftNode的next
    leftNode.next = swapPairs2(rightNode.next);
    // 然后本次本次递归后的头部rightNode的next指向 leftNode
    rightNode.next = leftNode;

    // 返回本次递归的头部，用于连接到上一次递归的尾部
    return rightNode;
  }

  private static void outputListNode(ListNode head) {
    /*用于输出链表，观察是否算法正确*/

    while (head != null) {
      System.out.println(head.val);
      head = head.next;
    }
  }

  public static void main(String[] args) {
    // 创建一个链表，1,2,3,4,5为例
    ListNode a1 = new ListNode(1);
    ListNode a2 = new ListNode(2);
    ListNode a3 = new ListNode(3);
    ListNode a4 = new ListNode(4);
    ListNode a5 = new ListNode(5);
    a1.next = a2;
    a2.next = a3;
    a3.next = a4;
    a4.next = a5;

    ListNode newHead = swapPairs2(a1);
    outputListNode(newHead);
  }
}
