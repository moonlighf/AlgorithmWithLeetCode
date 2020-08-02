package com.skymoon

class TreeNode(var _value: Int) {
  var value: Int = _value
  var left: TreeNode = null
  var right: TreeNode = null
}

object solutionDecodeString394 {
  def inorderTraversal(root: TreeNode): List[Int] = {
    // 递归法
    if (root == null)  {return Nil}
    // 直接通过:::连接两个LIST
    inorderTraversal(root.left) ::: List(root.value) ::: inorderTraversal(root.right)
  }

  def inorderTraversal2(root: TreeNode): List[Int] = {
    // 迭代法
    var res:List[Int] = Nil
    // 初始化一个栈作为辅助存储
    var stack: List[TreeNode] = Nil

    var currentNode:TreeNode = root
    while (currentNode != null || stack.nonEmpty){
      // 到达二叉树最底部的叶子节点
      while (currentNode != null) {
        stack = currentNode::stack
        currentNode = currentNode.left;
      }
      // 然后开始取出节点存入res
      currentNode = stack.head
      res = res:+ stack.head.value
      stack = stack.tail
      // 此时左中节点已经加存入res，所以对右节点做同样操作即可
      currentNode = currentNode.right
    }
    res
  }



  def main(args: Array[String]): Unit = {
    // 创建一个二叉树
    val a1 = new TreeNode(1)
    val a2 = new TreeNode(2)
    val a3 = new TreeNode(3)
    val a4 = new TreeNode(4)
    val a5 = new TreeNode(5)

    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5
    println(inorderTraversal2(a1));
  }
}
