package main


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
