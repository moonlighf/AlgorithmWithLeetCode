package com.skymoon;

import java.util.*;

public class DecodeString {
    public static String decodeString(String s) {
        // 初始化一个栈用于辅助处理
        Deque<String> stack = new LinkedList<>();
        for(int i=0; i< s.length(); i++){
            if("]".equals(String.valueOf(s.charAt(i)))){
                // step1.找到与之对应的"["
                List<String> tempArray = new ArrayList();
                // 从栈中pop出元素，直到找到"[" 存入到临时数组
                while (!stack.isEmpty() && !"[".equals(stack.peek())){
                    tempArray.add(0, stack.pop());
                }
                // 此时stack的栈顶元素已经是"["， 临时数组tempArray则为待复制的字母
                // pop出stack的栈顶"["
                stack.pop();
                // 然后开始pop出stack中的数字
                // 利用tempNum存储数字
                String tempNumStr = "";
                while (stack.size() >= 1 && stack.peek().charAt(0) >= 48 && stack.peek().charAt(0)<= 57){
                    tempNumStr = stack.peek().concat(tempNumStr);
                    stack.pop();
                }
                // 字符型的数字转换为整型
                int tempNumInt = Integer.parseInt(tempNumStr);
                // 将复制的字符串正向放到栈里
                String beforeStr = String.join("",tempArray);
                String afterStr = String.join("", Collections.nCopies(tempNumInt, beforeStr));
                // 按照每个字符放到栈尾
                for (int j = 0; j < afterStr.length(); j++) {
                    stack.push(String.valueOf(afterStr.charAt(j)));
                }

            }else {
                stack.push(String.valueOf(s.charAt(i)));
            }
        }
        // 最后把栈内的元素连接起来输出
        String res = "";
        while(stack.size() > 0) {
            res = res.concat(stack.removeLast());
        }
        return res;
    }


    public static void main(String[] args) {
        String tokens = "3[a]2[bc]";
        System.out.println(decodeString(tokens));
    }
}
