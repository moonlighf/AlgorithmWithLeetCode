package com.skymoon.stack;

import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

public class SolutionDailyTemperatures {

  public static int[] dailyTemperatures(int[] T) {
    int length = T.length;
    // 初始化一个栈(实际上这里使用的是双端队列)和一个结果数组
    int[] ans = new int[length];
    Deque<Integer> stack = new LinkedList<Integer>();
    for (int i = 0; i < length; i++) {
      int temperature = T[i];
      while (!stack.isEmpty() && temperature > T[stack.peek()]) {
        int prevIndex = stack.pop();
        ans[prevIndex] = i - prevIndex;
      }
      stack.push(i);
    }
    return ans;
  }


  public static void main(String[] args) {
    int[] temperatures = new int[] {73, 74, 75, 71, 69, 72, 76, 73};
    System.out.println(Arrays.toString(dailyTemperatures(temperatures)));
  }
}
