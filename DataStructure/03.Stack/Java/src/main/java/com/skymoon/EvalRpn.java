package com.skymoon;

import java.util.Deque;
import java.util.LinkedList;

/**
 * @author skymo
 */
public class EvalRpn {
    public static int evalRPN(String[] tokens) {
        // 初始化一个栈，这里采用双端队列实现
        Deque<Integer> stack = new LinkedList<Integer>();
        // 遍历tokens数组
        Integer num1, num2;
        for (String token : tokens) {
            // 如果是数字则直接存入栈，如果是运算符则pop出栈顶两个元素进行计算
            switch (token) {
                case "+":
                    num1 = stack.pop();
                    num2 = stack.pop();
                    stack.push(num2 + num1);
                    break;
                case "-":
                    num1 = stack.pop();
                    num2 = stack.pop();
                    stack.push(num2 - num1);
                    break;
                case "*":
                    num1 = stack.pop();
                    num2 = stack.pop();
                    stack.push(num2 * num1);
                    break;
                case "/":
                    num1 = stack.pop();
                    num2 = stack.pop();
                    stack.push(num2 / num1);
                    break;
                default:
                    // 如果是数字则直接入栈
                    stack.push(Integer.valueOf(token));

            }
        }
        return stack.getFirst();
    }


    public static void main(String[] args) {
        String[] tokens = new String[]{"2", "1", "+", "3", "*"};
        System.out.println(evalRPN(tokens));
    }
}
