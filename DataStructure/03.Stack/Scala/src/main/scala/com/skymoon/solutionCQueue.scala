package com.skymoon

class CQueue() {
  var resStack: List[Int] = Nil
  var helpStack: List[Int] = Nil

  def appendTail(value: Int): Unit = {
    helpStack = value::helpStack
  }

  def deleteHead(): Int = {
    // 如果res栈为空的话，则pop出help栈中的元素入res栈，这样元素顺序颠倒，符合队列的顺序
    if(resStack.isEmpty){
      while (helpStack.nonEmpty){
        val temp = helpStack.head
        helpStack = helpStack.tail
        resStack = temp :: resStack
      }
    }
    // 如果此时res栈仍然为空的话，代表并没有入栈元素，直接返回-1
    if(resStack.isEmpty){
      return -1
    }else {
      val temp = resStack.head
      resStack = resStack.tail
      return temp
    }

  }

}

object solutionCQueue {
  def main(args: Array[String]): Unit = {
    var obj = new CQueue()
    obj.appendTail(1)
    obj.appendTail(2)
    obj.appendTail(3)
    obj.appendTail(4)

    var param_2 = obj.deleteHead()
    println(param_2)
  }
}
