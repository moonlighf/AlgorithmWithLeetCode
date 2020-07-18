package main

import "fmt"

func outPutListNode(head *ListNode)  {
	for head != nil{
		fmt.Println(head.Val)
		head = head.Next
	}

}