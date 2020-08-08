package com.skymoon;


import java.util.Deque;
import java.util.LinkedList;

public class CQueue {
    Deque<Integer> stack1;
    Deque<Integer> stack2;

    public CQueue() {
        stack1 = new LinkedList<Integer>();
        stack2 = new LinkedList<Integer>();
    }

    public void appendTail(int value) {
        stack1.push(value);
    }

    public int deleteHead() {
        if (stack2.isEmpty()){
            while (!stack1.isEmpty()){
                stack2.push(stack1.poll());
            }
        }
        if(stack2.isEmpty()){
            return -1;
        }else {
            return stack2.pop();
        }
    }

    public static void main(String[] args) {
        CQueue obj = new CQueue();
        obj.appendTail(1);
        obj.appendTail(2);
        obj.appendTail(3);
        obj.appendTail(4);
        int param_2 = obj.deleteHead();
        System.out.println(param_2);
    }
}
