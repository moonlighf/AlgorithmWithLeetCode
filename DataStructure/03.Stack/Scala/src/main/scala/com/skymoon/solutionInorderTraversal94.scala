package com.skymoon

object solutionInorderTraversal94 {
  def decodeString(s: String): String = {
    // 初始化一个栈用于辅助运算
    var elements:List[String]=Nil

    // 遍历字符串
    for(index <- 0 until s.length){
      if(s.charAt(index) != ']'){
        // 如果不是"]", 则直接入栈
        elements = s.charAt(index).toString::elements
      } else{
        // 如果是"]"，这需要处理出待复制的字符串和待复制的次数
        var tempStr = ""
        while(elements.head != "[" && elements.nonEmpty){
          val element = elements.head
          elements = elements.tail
          tempStr = element.concat(tempStr)
        }
        // 去除栈中的就近的"["，从而方便取就近的复制次数
        elements = elements.tail
        // 然后需要取出来待复制的次数
        var temNumStr = ""
        while(elements.nonEmpty && elements.head.charAt(0) >= 48 && elements.head.charAt(0) <= 57){
          temNumStr = elements.head.concat(temNumStr)
          elements = elements.tail
        }
        // 次数转为数值型
        val temNumInt = temNumStr.toInt
        // 将待复制的字符串复制指定次数
        val afterStr = tempStr * temNumInt
        // 复制后的字符串写入到栈顶
        for( tem <- afterStr){
          elements = tem.toString::elements
        }
      }

    }
    var res = ""
    // 循序从栈中pop出元素组成字符串
    for( element <- elements){
      res = element.concat(res)
    }
    res
  }

  def main(args: Array[String]): Unit = {
    val tokens = "100[leetcode]"
    println(decodeString(tokens))
  }
}
