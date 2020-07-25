package com.skymoon.stack;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class SolutionIsValid {
  private static final Map<Character, Character> map =
      new HashMap<Character, Character>() {
        {
          put('{', '}');
          put('[', ']');
          put('(', ')');
          put('?', '?');
        }
      };

  public static boolean isValid(String s) {
    // 处理特殊情况，字符串长度非偶数的，直接判断不能凑对
    int strLength = s.length();
    if (strLength % 2 != 0) {
      return false;
    }

    // 初始化一个栈用于存储括号
    Stack<Character> stack = new Stack<Character>();
    // 遍历字符串
    for (int i = 0; i < strLength; i++) {
      char c = s.charAt(i);

      if (map.containsKey(c)) {
        // 如果是左括号，即入栈
        stack.push(c);
      } else if (!stack.empty()) {
        // 如果是右括号且栈不为空，则看是否能和栈顶的左括号匹配
        char topElement = stack.pop();
        if (c != map.get(topElement)) {
          return false;
        }

      } else {
        return false;
      }
    }

    return stack.isEmpty();
  }

  public static void main(String[] args) {
    // 主函数，测试是否输出正确
    String backerTemp = "()[]{}";
    System.out.println(isValid(backerTemp));
  }
}
