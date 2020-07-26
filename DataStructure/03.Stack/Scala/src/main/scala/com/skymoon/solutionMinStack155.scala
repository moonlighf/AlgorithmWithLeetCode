package com.skymoon

class MinStack() {

  /** initialize your data structure here. */
  // 初始化两个站，分别作为原始栈和辅助栈，辅助栈用于辅助存储最小值于栈顶，方便能在常数时间内找到最小值
  var realStack: List[Int] = Nil
  var helpStack: List[Int] = Nil

  def push(x: Int): Unit = {
    realStack = x :: realStack
    if (helpStack.isEmpty || helpStack.head > x) {
      helpStack = x :: helpStack
    } else {
      helpStack = helpStack.head :: helpStack
    }
  }

  def pop(): Int = {
    // 对于不为空的原始栈，直接pop出去栈顶元素即可
    if (realStack.nonEmpty) {
      // 保持同步pop出辅助栈的栈顶元素
      helpStack = helpStack.tail
      // 删除栈顶元素，并返回栈顶元素
      val current = realStack.head
      realStack = realStack.tail
      current
    } else {
      0
    }
  }

  def top(): Int = {
    // 如果原始栈不为空则直接返回栈顶元素
    if (realStack.nonEmpty) {
      realStack.head
    } else {
      0
    }
  }

  def getMin(): Int = {
    // 如果辅助栈不为空，则返回辅助栈的栈顶元素
    if (helpStack.nonEmpty) {
      helpStack.head
    } else {
      0
    }
  }

}

object solutionMinStack155 {

  def main(args: Array[String]): Unit = {
    // 测试主函数
    val obj = new MinStack()
    obj.push(5)
    obj.push(4)
    obj.push(3)
    obj.push(6)
    obj.push(7)
    obj.pop()
    val param_3 = obj.top()
    val param_4 = obj.getMin()
    println(param_3)
    println(param_4)
  }
}
