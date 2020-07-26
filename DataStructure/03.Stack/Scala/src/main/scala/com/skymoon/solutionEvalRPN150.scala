package com.skymoon

object solutionEvalRPN150 {

  def evalRPN(tokens: Array[String]): Int = {
    // 初始化一个栈用于存储数字
    var elements:List[String]=Nil

    // 利用匿名函数构建 字符串符号到函数方法的对应关系
    val plus = (a:Int, b:Int) => a+b
    val sub = (a:Int, b:Int) => a-b
    val multi = (a:Int, b:Int) => a*b
    val div = (a:Int, b:Int) => a/b

    val ways = Map(
      "+" -> plus,
      "-" -> sub,
      "*" -> multi,
      "/" -> div
    )

    val tokensLength = tokens.length
    // 遍历含有数字和运算符的列表
    for(i <- 0 until tokensLength){
      if(tokens(i)== "+" || tokens(i)== "-" || tokens(i)== "*" || tokens(i)== "/"){
        // 如果是运算符，则从栈顶pop两个数字进行计算
        val num1 = elements.head
        elements = elements.tail
        val num2 = elements.head
        elements = elements.tail
        val res = ways(tokens(i))(num2.toInt, num1.toInt)
        elements = res.toString::elements
      } else {
        // 如果是数字直接入栈
        elements = tokens(i)::elements
      }
    }
    // 最后输出栈顶元素即可
    elements.head.toInt
  }

  def main(args: Array[String]): Unit = {
    // 测试主函数
    val temp1 = Array[String]("4","13","5","/","+")
    println(evalRPN(temp1))

  }
}
