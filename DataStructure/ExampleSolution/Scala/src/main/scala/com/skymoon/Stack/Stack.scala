package com.skymoon.Stack

class Stack[T] {
  private var elements: List[T] = Nil


  def push(element: T) {
    // 在现有List前增加元素，构成新的List，使用符号 ::
    // 使用形式： newList = newEle::oldList
    // 在现有List后增加元素，构成新的List，使用符号 :+
    // 使用形式： newList = oldList:+newEle
    elements = element :: elements
  }

  def peek() {
    elements.head
  }

  def pop(): T = {
    //head返回的是列表第一个元素的值
    val current = elements.head
    //tail返回的是除第一个元素外的其它值构成的新列表，这体现出列表具有递归的链表结构
    elements = elements.tail
    current
  }
}
