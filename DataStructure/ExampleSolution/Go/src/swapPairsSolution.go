package main

import "fmt"




func swapPairs(head *ListNode) *ListNode {
	// 声明一个节点作为伪头节点
	dump := &ListNode{Val: -1}
	dump.Next = head

	// 声明一个prev节点, 用来记录两个节点交换后前面那个节点的前一个节点
	prev := dump
	//开始迭代交换两个节点
	for head != nil && head.Next !=nil{
		// 初始化两个待交换的节点
		leftNode := head
		rightNode := head.Next

		// 交换两个节点之前，需要将prev节点指向新的待交换的起点
		prev.Next = rightNode
		// 交换两个节点
		leftNode.Next = rightNode.Next
		rightNode.Next = leftNode

		// 重置head节点保证迭代的正常运行， head指向此次交换后的尾部的下一个节点
		head =leftNode.Next
		prev = leftNode
	}

	return dump.Next
}




func main() {
	var a1 = &ListNode{Val: 1}
	var a2 = &ListNode{Val: 2}
	var a3 = &ListNode{Val: 3}
	var a4 = &ListNode{Val: 4}
	var a5 = &ListNode{Val: 5}
	a1.Next = a2
	a2.Next = a3
	a3.Next = a4
	a4.Next = a5
	fmt.Println("before swap: ")
	outPutListNode(a1)
	fmt.Println("after swap: ")
	newHead := swapPairs(a1)
	outPutListNode(newHead)
}
