/* *****************************************************
 * @File Name   : sumNumbers
 * @Author      : SkyMoon
 * @Email       : skymoon9406@gmail.com
 * @Create Date : 2021/3/17
 * @Description :
 * *****************************************************/
package main

import (
	"fmt"
	"strconv"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumNumbers(root *TreeNode) int {
	if root == nil{
		return 0
	}
	res := 0
	dfs(root, "", &res)
	return res
}

func dfs(node *TreeNode, tempStr string, res *int)  {
	if node.Left == nil && node.Right == nil{
		tempStr = tempStr +strconv.Itoa(node.Val)
		tempInt, _ := strconv.Atoi(tempStr)
		*res = *res + tempInt
	}
	tempStr = tempStr + strconv.Itoa(node.Val)
	if node.Left != nil{
		dfs(node.Left, tempStr, res)
	}

	if node.Right != nil{
		dfs(node.Right, tempStr, res)
	}
}

func main() {
	a1 := TreeNode{1, nil, nil}
	a2 := TreeNode{2, nil, nil}
	a3 := TreeNode{3, nil, nil}
	a4 := TreeNode{4, nil, nil}
	a5 := TreeNode{5, nil, nil}
	a6 := TreeNode{6, nil, nil}
	a7 := TreeNode{7, nil, nil}
	a1.Left = &a2
	a1.Right = &a3
	a2.Left = &a4
	a2.Right = &a5
	a3.Left = &a6
	a3.Right = &a7
	fmt.Println(sumNumbers(&a1))
}
