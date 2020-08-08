package com.skymoon;

import java.util.Deque;
import java.util.LinkedList;

public class RemoveDuplicates {
    public static String removeDuplicates(String S) {
        Deque<Character> stack = new LinkedList<Character>();
        // 遍历字符串
        for (int index=0; index< S.length(); index++){
            if (stack.isEmpty() || S.charAt(index) != stack.peek()){
                stack.push(S.charAt(index));
            }else {
                stack.pop();
            }
        }
        // 栈中元素全部pop出来组成字符串
        String resStr = "";
        while (!stack.isEmpty()){
            resStr = resStr.concat(stack.removeLast().toString());

        }
        return resStr;

    }

    public static void main(String[] args) {
        String a = "abbaca";
        String res = removeDuplicates(a);
        System.out.println(res);

    }
}
