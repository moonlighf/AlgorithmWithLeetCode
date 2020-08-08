package com.skymoon

object solutionRemoveDuplicates {
  def removeDuplicates(S: String): String = {
    var stack: List[Char] = Nil
    for (temp <- S){
      if(stack.isEmpty || stack.head != temp){
        stack = temp::stack
      } else {
        stack = stack.tail
      }
    }
    // 栈中元素全部pop出来组成字符串
    var res = ""
    while (stack.nonEmpty){
      res = stack.head.toString.concat(res)
      stack = stack.tail
    }
    return res
  }


  def main(args: Array[String]): Unit = {
    val a = "abbaca"
    println(removeDuplicates(a))
  }
}
