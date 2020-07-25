package com.skymoon.Stack

import scala.collection.mutable

object solutionIsValid {
  def isValid(s: String): Boolean = {
    /*
    利用一个栈，不断地往里压左括号，一旦遇上了一个右括号，我们就把栈顶的左括号弹出来，
    表示这是一个合法的组合，以此类推，直到最后判断栈里还有没有左括号剩余
     */
    // 处理特殊情况
    val strLength = s.length
    if (strLength % 2 !=0){
      return false
    }
    // 初始化一个栈用于存储括号，这里用数组代替，由于使用array定义的数组属于定长数组
    // 所以这里利用ArrayBuffer初始化变长数组
    val stackClass = mutable.Stack[String]()
    val backerMap = Map("{" -> "}", "[" -> "]", "(" -> ")")
    // 循环遍历字符串
    for(i <- 0 until strLength){
      // 如果是左括号则入栈
      if(backerMap.contains(s.charAt(i).toString)){
        stackClass.push(s.charAt(i).toString)
      } else if(stackClass.nonEmpty){
        // 如果两者匹配则继续，否则就终止
        // 由于需要按照顺序，所以不存在 ([)] 的情况
        val tempBacker= stackClass.pop()
        if (backerMap(tempBacker) != s.charAt(i).toString){
          return false
        }
      }else{
        return false
      }
    }
    if (stackClass.isEmpty) true else false
  }

  def main(args: Array[String]): Unit = {
    val status = isValid("()[]{}")
    println(status)
  }
}
