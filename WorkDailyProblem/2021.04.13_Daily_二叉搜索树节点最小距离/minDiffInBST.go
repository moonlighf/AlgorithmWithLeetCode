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
	"math"
)

// Definition for a binary tree node.
type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}


func main() {
	root :=TreeNode{4, nil, nil}
	t1 :=TreeNode{2, nil, nil}
	t2 :=TreeNode{6, nil, nil}
	t3 :=TreeNode{1, nil, nil}
	t4 :=TreeNode{3, nil, nil}

	root.Left = &t1
	root.Right = &t2
	t1.Left = &t3
	t1.Right = &t4
	fmt.Println(minDiffInBST(&root))
}

func minDiffInBST(root *TreeNode) int {
	// 由于是一个搜索二叉树，所以满足 左子树所有节点 < 中 < 右子树所有节点，所以最小值一定出现在相邻节点
	// 由于二叉搜索树的中序遍历是递增序列，所以只需要找到其中序遍历相邻元素的最小值即可
	// 朴素的方法是经过一次中序遍历将值保存在一个数组中再进行遍历求解，我们也可以在中序遍历的过程中用 pre 变量保存前驱节点的值
	ans, pre := math.MaxInt64, -1
	var dfs func(*TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			return
		}
		dfs(node.Left)
		if pre != -1 && node.Val-pre < ans {
			ans = node.Val - pre
		}
		pre = node.Val
		dfs(node.Right)
	}
	dfs(root)
	return ans
}