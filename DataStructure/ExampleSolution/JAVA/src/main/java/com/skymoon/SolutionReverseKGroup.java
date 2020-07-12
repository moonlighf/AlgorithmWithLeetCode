package com.skymoon;

/** @author skymoon */
public class SolutionReverseKGroup {
  public static ListNode reverseKGroup(ListNode head, int k) {
      // 声明三个指针分别指向prev，curr，next
      ListNode prev = new ListNode(-1);
      ListNode curr = head;
      int n = k;
      // 判断链表剩余的数量是否比窗口小，小于窗口则不用翻转
      ListNode tail = curr;
      for (int i = 0; i < k; i++){
          if (tail == null){
              return head;
          }
          tail = tail.next;
      }
      // 局部翻转
      while (curr != null && n-- >0){
          // 初始化next 节点指向 curr节点的next
          ListNode next = curr.next;
          // 然后交换，使curr的next 指向其前面的prev节点
          curr.next = prev;
          // 然后 prev和curr 都向前移动一位
          prev = curr;
          curr = next;
      }
      // prev成为新的链表头，curr指向了下一个要被处理的局部的第一个元素，原来的头指针head成为了链表的尾巴
      ListNode newHead = prev;

      head.next = reverseKGroup(curr, k);
      return newHead;
  }

  private static void outputListNode(ListNode head) {
    /*用于输出链表，观察是否算法正确*/

    while (head != null) {
      System.out.println(head.val);
      head = head.next;
    }
  }

  public static void main(String[] args) {
    // 创建一个链表，6,7,8,9,2为例
    ListNode a1 = new ListNode(6);
    ListNode a2 = new ListNode(7);
    ListNode a3 = new ListNode(8);
    ListNode a4 = new ListNode(9);
    ListNode a5 = new ListNode(2);
    a1.next = a2;
    a2.next = a3;
    a3.next = a4;
    a4.next = a5;

    ListNode newHead = reverseKGroup(a1, 3);
    outputListNode(newHead);
  }
}
