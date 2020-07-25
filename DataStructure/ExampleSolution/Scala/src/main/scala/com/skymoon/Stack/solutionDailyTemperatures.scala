package com.skymoon.Stack
import scala.collection.mutable

object solutionDailyTemperatures {
  def dailyTemperatures(T: Array[Int]): Array[Int] = {
    val arrayLength = T.length
    // 初始化一个栈，为了方便，直接将第一个温度放入栈中
    val stackTemperature = mutable.Stack((T(0), 0))
    // 初始化结果数组
    val resultArray: Array[Int] = new Array[Int](arrayLength)
    // 遍历温度数组和栈顶温度比较
    for (i <- 0 until arrayLength){
      if (stackTemperature.top._1 < T(i)){
        // 如果栈顶元素小于此时待入栈元素，那么栈顶元素后面的第一个大于他的数就是此时的待入站元素，然后继续判断新的栈顶元素
        while (stackTemperature.nonEmpty && stackTemperature.top._1 < T(i)){
          val tempTem = stackTemperature.pop()
          resultArray(tempTem._2) = i - tempTem._2
        }
        stackTemperature.push((T(i), i))
      }else {
        // 如果栈顶元素大于此时待入栈元素，则此时待入栈元素入栈
        stackTemperature.push((T(i), i))
      }
    }

    resultArray
  }

  def main(args: Array[String]): Unit = {
    val temperatures = Array[Int](73, 74, 75, 71, 69, 72, 76, 73)
    val status = dailyTemperatures(temperatures)
    println(status.toList)
  }
}
