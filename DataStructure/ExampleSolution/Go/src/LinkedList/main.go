package main

import "fmt"

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


	var a6 = &ListNode{Val: 1}
	var a7 = &ListNode{Val: 2}
	var a8 = &ListNode{Val: 3}
	var a9 = &ListNode{Val: 4}
	var a10 = &ListNode{Val: 5}
	a6.Next = a7
	a7.Next = a8
	a8.Next = a9
	a9.Next = a10
	fmt.Println("before swap2: ")
	outPutListNode(a6)
	fmt.Println("after swap2: ")
	newHead2 := reverseKGroup(a6, 3)
	outPutListNode(newHead2)
}

