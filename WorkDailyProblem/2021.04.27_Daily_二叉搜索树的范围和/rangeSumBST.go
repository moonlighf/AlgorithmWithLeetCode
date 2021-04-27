/* *****************************************************
 * @File Name   : test
 * @Author      : SkyMoon
 * @Email       : skymoon9406@gmail.com
 * @Create Date : 2021/4/1
 * @Description :
 * *****************************************************/
package main

import (
	"fmt"
)

func main() {
	//root = [10,5,15,3,7,null,18]
	node1 := &TreeNode{10, nil, nil}
	node2 := &TreeNode{5, nil, nil}
	node3 := &TreeNode{15, nil, nil}
	node4 := &TreeNode{3, nil, nil}
	node5 := &TreeNode{7, nil, nil}
	node6 := &TreeNode{18, nil, nil}

	node1.Left = node2
	node1.Right = node3
	node2.Left = node4
	node2.Right = node5
	node3.Right = node6

	low := 7
	high := 15

	fmt.Println(rangeSumBST(node1, low, high))
}



type TreeNode struct {
   Val int
    Left *TreeNode
    Right *TreeNode
}

func rangeSumBST(root *TreeNode, low int, high int) int {
	sumVal := 0

	var inOrder  func(*TreeNode)
	inOrder = func(node *TreeNode) {
		if node == nil{
			return
		}
		inOrder(node.Left)
		if node.Val<= high && node.Val >= low{
			sumVal += node.Val
		}
		inOrder(node.Right)

	}
	inOrder(root)
	return sumVal
}

func rangeSumBST2(root *TreeNode, low int, high int) int {
	// 利用数组直接存储每个节点
	sum := 0
	q := []*TreeNode{root}
	for len(q) > 0 {
		node := q[0]
		q = q[1:]
		if node == nil {
			continue
		}
		// 由于是二叉搜索树，所以右子树一定大于左子树，此处值如果大于最大值或者小于最小值，则直接舍弃对应的一边的子树
		if node.Val > high {
			q = append(q, node.Left)
		} else if node.Val < low {
			q = append(q, node.Right)
		} else {
			// 针对满足要求的节点，则累加其值，并将其左右子节点加入队列
			sum += node.Val
			q = append(q, node.Left, node.Right)
		}
	}
	return sum
}