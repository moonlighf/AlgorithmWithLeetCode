package com.skymoon;

import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

public class InorderTraversal {

    public static List<Integer> inorderTraversal(TreeNode root) {
        // 递归算法
        // 递归结束条件
        List < Integer > res = new ArrayList < > ();
        helper(root, res);
        return res;
    }

    public static List<Integer> inorderTraversal2(TreeNode root) {
        // 迭代算法
        // 初始化一个list作为结果存储
        List < Integer > res = new ArrayList < > ();
        // 初始化一个双端队列（栈）作为辅助处理
        Deque<TreeNode> stack = new LinkedList<TreeNode>();

        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()){
            // 先从根节点的左子节点遍历到叶子节点
            // 后续每次循环相当于从当前节点左边到最终端
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            res.add(curr.val);
            curr = curr.right;
        }
        return res;
    }

    public static void helper(TreeNode root, List<Integer> res) {
        if (root != null) {
            // 递归结束条件
            if (root.left != null) {
                helper(root.left, res);
            }
            res.add(root.val);
            if (root.right != null) {
                helper(root.right, res);
            }
        }
    }


    public static void main(String[] args) {
        // 创建一个二叉树
        TreeNode a1 = new TreeNode(1);
        TreeNode a2 = new TreeNode(2);
        TreeNode a3 = new TreeNode(3);
        TreeNode a4 = new TreeNode(4);
        TreeNode a5 = new TreeNode(5);
        a1.left = a2;
        a1.right = a3;
        a2.left = a4;
        a2.right = a5;
        System.out.println(inorderTraversal2(a1));

    }
}
