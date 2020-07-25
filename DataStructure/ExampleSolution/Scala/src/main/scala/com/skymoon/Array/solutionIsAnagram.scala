package com.skymoon.Array

import scala.collection.mutable

object solutionIsAnagram {
  def isAnagram(s: String, t: String): Boolean = {
    // 处理特殊情况, 两个字符串长度不相等时，必定不是
    val sLength = s.length
    val tLength = t.length
    if (sLength != tLength) {
      return false
    }
    // 声明两个数组分别存放两个字符串中字符出现的次数
    val sArray = new Array[Int](26)
    val tArray = new Array[Int](26)
    // 遍历两个字符串统计每个字符出现的次数, 97为"a"的ascii码
    for (i <- 0 until sLength) {
      sArray(s.charAt(i) - 97) += 1
      tArray(t.charAt(i) - 97) += 1
    }
    // 判断两个数组是否相等
    sArray sameElements tArray
  }

  def isAnagram2(s: String, t: String): Boolean = {
    // 处理特殊情况, 两个字符串长度不相等时，必定不是
    val sLength = s.length
    val tLength = t.length
    if (sLength != tLength) {
      return false
    }
    // 声明一个哈希表来保存每个字符串中字符出现的次数
    var countNumMap = new mutable.HashMap[Char,Int]()
    // 遍历字符串，统计字符出现的次数
    for (i <- 0 until sLength) {
      // 这里使用getOrElse简化了判断在不在的过程
      countNumMap(s.charAt(i)) = countNumMap.getOrElse(s.charAt(i), 0) + 1
    }
    for (i<- 0 until tLength){
      countNumMap(t.charAt(i)) = countNumMap.getOrElse(t.charAt(i), 0) - 1
      if (countNumMap(t.charAt(i)) < 0){
        return false
      }
    }
    true
  }



  def main(args: Array[String]): Unit = {
    val s = "anagram"
    val t = "nagaram"
    val status = isAnagram2(s, t)
    println(status)
  }
}
