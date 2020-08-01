package com.skymoon;

import java.util.Deque;
import java.util.LinkedList;

public class MinStack {

    private Deque<Integer> realStack;
    private Deque<Integer> helpStack;

    /** initialize your data structure here. */
    public MinStack() {
        realStack = new LinkedList<Integer>();
        helpStack = new LinkedList<Integer>();
    }

    public void push(int x) {
        // 对于原始栈，是直接push进栈
        realStack.push(x);
        // 对于辅助栈， 如果为空，或者小于栈顶元素，则可以入栈
        if (helpStack.size() ==0 || helpStack.peek() > x){
            helpStack.push(x);
        }else {
            helpStack.push(helpStack.peek());
        }
    }

    public void pop() {
        // 如果原始栈不为空，则pop出栈顶元素。为保证统一，也得处理辅助栈的栈顶元素
        if(!realStack.isEmpty()){
            helpStack.pop();
            realStack.pop();
        }
    }

    public int top() {
        // 直接返回原始栈的栈顶元素
        if(!realStack.isEmpty()){
            return realStack.peek();
        } else {
            return 0;
        }
    }

    public int getMin() {
        // 直接返回辅助栈的栈顶元素
        if(!helpStack.isEmpty()){
            return helpStack.peek();
        } else {
            return 0;
        }
    }


    public static void main(String[] args) {
        MinStack obj = new MinStack();
        obj.push(3);
        obj.push(4);
        obj.push(5);
        obj.push(6);
        obj.pop();
        int param3 = obj.top();
        int param4 = obj.getMin();
        System.out.println(param3);
        System.out.println(param4);

    }
}
