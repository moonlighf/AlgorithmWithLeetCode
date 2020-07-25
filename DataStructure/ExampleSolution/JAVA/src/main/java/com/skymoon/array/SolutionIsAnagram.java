package com.skymoon.array;

import java.util.Arrays;
import java.util.HashMap;

/** @author skymoon */
public class SolutionIsAnagram {
  private static boolean isAnagram1(String s, String t) {
    /* **************************************************************************
     * 主要思路：利用两个长度都为 26 的字符数组来统计每个字符串中小写字母出现的次数，
     * 然后再对比是否相等；
     *  **************************************************************************/
    // 获取两个输入字符串的长度
    int sLength = s.length();
    int tLength = t.length();
    // 处理特殊情况, 如果两者长度不等，直接就不可能为异位词
    if (sLength != tLength) {
      return false;
    }
    // 声明两个数组来储存输入字符串中字母出现的次数
    int[] sArray = new int[26];
    int[] tArray = new int[26];
    // 遍历两个字符串，分别统计出现的字符的次数, 97为a的ascii码
    for (int i = 0; i < sLength; i++) {
      sArray[(int) s.charAt(i) - 97] += 1;
      tArray[(int) t.charAt(i) - 97] += 1;
    }
    // 判断两个数组是否相等, 这里不能使用==，这样只能判断地址
    return Arrays.equals(sArray, tArray);
  }

  private static boolean isAnagram2(String s, String t) {
    /* **************************************************************************
     * 主要思路：利用一个长度为 26 的字符数组，将出现在字符串 s 里的字符个数加 1，
     * 而出现在字符串 t 里的字符个数减 1，最后判断每个小写字母的个数是否都为 0。
     *  **************************************************************************/
    // 获取两个输入字符串的长度
    int sLength = s.length();
    int tLength = t.length();
    // 处理特殊情况, 如果两者长度不等，直接就不可能为异位词
    if (sLength != tLength) {
      return false;
    }
    // 声明两个数组来储存输入字符串中字母出现的次数
    int[] countNumArray = new int[26];
    // 遍历两个字符串，分别统计出现的字符的次数, 97为a的ascii码
    for (int i = 0; i < sLength; i++) {
      countNumArray[(int) s.charAt(i) - 97] += 1;
      countNumArray[(int) t.charAt(i) - 97] -= 1;
    }
    // 循环判断数组每个字符是否等于0
    for (int i : countNumArray) {
      if (i != 0) {
        return false;
      }
    }
    return true;
  }

  private static boolean isAnagram3(String s, String t) {
    /* **************************************************************************
     * 主要思路：将方法二中的数组转化为哈希表
     *  **************************************************************************/
    // 获取两个输入字符串的长度
    int sLength = s.length();
    int tLength = t.length();
    // 处理特殊情况, 如果两者长度不等，直接就不可能为异位词
    if (sLength != tLength) {
      return false;
    }
    // 声明一个哈希表来储存输入字符串中字母出现的次数
    HashMap<Character, Integer> countNumMap = new HashMap<Character, Integer>();
    // 遍历两个字符串，分别统计出现的字符的次数
    for (int i = 0; i < sLength; i++) {
      if (countNumMap.containsKey(s.charAt(i))) {
        countNumMap.put(s.charAt(i), countNumMap.get(s.charAt(i)) + 1);
      } else {
        countNumMap.put(s.charAt(i), 1);
      }
    }
    for (int i = 0; i < tLength; i++) {
      if (countNumMap.containsKey(t.charAt(i))) {
        countNumMap.put(t.charAt(i), countNumMap.get(t.charAt(i)) - 1);
        // 此时如果已经变成负数，则可以提前退出
        if (countNumMap.get(t.charAt(i)) < 0) {
          return false;
        }
      } else {
        return false;
      }
    }
    return true;
  }

  public static void main(String[] args) {
    // 运行测试是否方法成功
    String s = "aa";
    String t = "bb";
    boolean status = isAnagram2(s, t);
    System.out.println(status);
  }
}
