package main

import (
	"fmt"
)


func reverseKGroup(head *ListNode, k int) *ListNode {
	// 初始化三个指针prev，curr，next分别指向头结点的前一个节点，头结点，和头结点的下一个节点
	prev := &ListNode{Val: -1}
	curr := head
	var n = k
	// 判断剩下的是否还需要进行翻转
	tail := head
	for i:=0; i<k; i++{
		if tail == nil{
			return head
		}
		tail = tail.Next
	}
	// 完成局部转换
	for curr != nil && n>0{
		nextNode := curr.Next
		curr.Next = prev
		prev = curr
		curr = nextNode
		n -=1
	}
	newHead := prev
	head.Next = reverseKGroup(curr, k)
	return newHead
}


func main() {
	var a1 = &ListNode{Val: 1}
	var a2 = &ListNode{Val: 2}
	var a3 = &ListNode{Val: 3}
	var a4 = &ListNode{Val: 4}
	var a5 = &ListNode{Val: 5}
	var a6 = &ListNode{Val: 6}
	a1.Next = a2
	a2.Next = a3
	a3.Next = a4
	a4.Next = a5
	a5.Next = a6
	fmt.Println("before swap: ")
	outPutListNode(a1)
	fmt.Println("after swap: ")
	newHead := reverseKGroup(a1, 3)
	outPutListNode(newHead)
}