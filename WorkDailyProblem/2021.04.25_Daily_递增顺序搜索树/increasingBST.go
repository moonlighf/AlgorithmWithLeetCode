/* *****************************************************
 * @File Name   : test
 * @Author      : SkyMoon
 * @Email       : skymoon9406@gmail.com
 * @Create Date : 2021/4/1
 * @Description :
 * *****************************************************/
package main

func main() {
	//root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
	node1 := TreeNode{5, nil, nil}
	node2 := TreeNode{3, nil, nil}
	node3 := TreeNode{6, nil, nil}
	node4 := TreeNode{2, nil, nil}
	node5 := TreeNode{4, nil, nil}
	node6 := TreeNode{8, nil, nil}
	node7 := TreeNode{1, nil, nil}
	node8 := TreeNode{7, nil, nil}
	node9 := TreeNode{9, nil, nil}
	node1.Left = &node2
	node1.Right = &node3
	node2.Left = &node4
	node2.Right = &node5
	node4.Left = &node7
	node3.Right = &node6
	node6.Left = &node8
	node6.Right = &node9

	//fmt.Println(increasingBST(&node1))
	increasingBST(&node1)
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func increasingBST(root *TreeNode) *TreeNode {
	var valArr []int
	var inorder func(*TreeNode)
	inorder = func(node *TreeNode) {
		if node != nil {
			inorder(node.Left)
			valArr = append(valArr, node.Val)
			inorder(node.Right)
		}
	}
	inorder(root)
	// 遍历中序遍历数组，重新构建二叉搜索树
	resTree := &TreeNode{-1, nil, nil}
	curNode := resTree
	for _, num := range valArr{
		curNode.Right = &TreeNode{num, nil, nil}
		curNode = curNode.Right
	}

	return resTree.Right
}

func increasingBST2(root *TreeNode) *TreeNode {
	dummyNode := &TreeNode{}
	resNode := dummyNode

	var inorder func(*TreeNode)
	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}
		inorder(node.Left)

		// 在中序遍历的过程中修改节点指向
		resNode.Right = node
		node.Left = nil
		resNode = node

		inorder(node.Right)
	}
	inorder(root)

	return dummyNode.Right
}



