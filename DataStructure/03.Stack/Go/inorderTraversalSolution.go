package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorderTraversal(root *TreeNode) []int {
	// 递归法
	if root == nil {
		return nil
	}
	return append(append(inorderTraversal(root.Left), root.Val), inorderTraversal(root.Right)...)
}

func inorderTraversal2(root *TreeNode) []int {
	// 迭代法
	var res []int
	// 初始化一个栈用于辅助存储
	var stack []TreeNode
	currentNode := root
	for currentNode != nil || len(stack) > 0 {
		for currentNode != nil{
			stack = append(stack, *currentNode)
			currentNode = currentNode.Left
		}
		// 然后开始取出节点存入res
		currentNode = &stack[len(stack)-1]
		res = append(res, stack[len(stack)-1].Val)
		stack = stack[:len(stack)-1]
		currentNode = currentNode.Right
	}
	return res
}


func main() {
	var a4 = &TreeNode{4, nil, nil}
	var a5 = &TreeNode{5, nil, nil}
	var a2 = &TreeNode{2, a4, a5}
	var a3 = &TreeNode{3, nil, nil}
	var a1 = &TreeNode{1, a2, a3}
	fmt.Println(inorderTraversal2(a1))
}
