package com.skymoon.LinkedList

object solutionReverseKGroup {
  def reverseKGroup(head: ListNode, k: Int): ListNode = {
    // 初始化三个指针prev，curr，next分别指向头结点的前一个节点，头结点，和头结点的下一个节点
    var prev: ListNode = new ListNode(-1)
    var curr = head
    var n = k
    // 判断是否还需要翻转
    var tail = curr
    for(i <- 0 until k){
      if( tail == null){
        return head
      }
      tail = tail.next
    }

    // 局部翻转
    while(curr != null && n > 0){
      val next: ListNode = curr.next
      curr.next = prev
      prev = curr
      curr = next
      n = n - 1
    }
    val newHead = prev
    head.next = reverseKGroup(curr, k)

    newHead
  }


  def outputListNode(head: ListNode):Unit={
    /*
    主要用于输出链表的所有节点的值
     */
    // 由于scala是函数编程，所以对待函数参数尽量是不要改变的，所以尽量是通过其他变量来转换为可变
    var _head: ListNode = head
    while (_head != null){
      println(_head.x)
      _head = _head.next
    }
  }


  def main(args: Array[String]): Unit = {
    val a1 = new ListNode(6)
    val a2 = new ListNode(7)
    val a3 = new ListNode(8)
    val a4 = new ListNode(9)
    val a5 = new ListNode(10)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    val newNode: ListNode = reverseKGroup(a1, 2)
    //输出看结果
    outputListNode(newNode)
  }
}
