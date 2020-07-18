package com.skymoon

// Definition for singly-linked list.
class ListNode(var _x: Int = 0) {
  var next: ListNode = _
  var x: Int = _x
}


object solutionsSwapPairs {
  def swapPairs(head: ListNode): ListNode = {
    // 由于scala是函数编程，所以对待函数参数尽量是不要改变的，所以尽量是通过其他变量来转换为可变
    var _head = head
    // 迭代法, 以处理链表 1->2->3->4->5 为例， 此时为链表增加个伪头部 dump->1->2->3->4->5
    val dump: ListNode = new ListNode(0)
    dump.next = _head
    // 开始迭代，设置终止条件。
    var prev: ListNode = dump
    while (_head != null && _head.next != null) {
      // 声明两个指针分别代表需要交换的节点
      val leftNode: ListNode = _head
      val rightNode: ListNode = _head.next

      prev.next = rightNode
      //交换两个节点
      leftNode.next = rightNode.next
      rightNode.next = leftNode

      _head = leftNode.next
      prev = leftNode
    }
    dump.next
  }

  def swapPairs2(head: ListNode): ListNode = {
    // 由于scala是函数编程，所以对待函数参数尽量是不要改变的，所以尽量是通过其他变量来转换为可变
    val _head = head
    // 递归法, 以处理链表 1->2->3->4->5 为例
    // 处理特殊情况
    if (_head == null || _head.next == null){
      return _head
    }
    // 声明两个节点作为要交换
    val leftNode = _head
    val rightNode = _head.next

    leftNode.next = swapPairs(rightNode.next)
    rightNode.next = leftNode

    rightNode
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
    val a1 = new ListNode(1)
    val a2 = new ListNode(2)
    val a3 = new ListNode(3)
    val a4 = new ListNode(4)
    val a5 = new ListNode(5)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    val newNode: ListNode = swapPairs2(a1)
    //输出看结果
    outputListNode(newNode)
  }
}
