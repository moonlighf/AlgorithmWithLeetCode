package main

import "fmt"

type CQueue struct {
	resStack  []int
	helpStack []int
}

func Constructor1() CQueue {
	return CQueue{
		resStack: []int{},
		helpStack: []int{},
	}
}

func (this *CQueue) AppendTail(value int) {
	this.helpStack = append(this.helpStack, value)
}

func (this *CQueue) DeleteHead() int {
	// 如果res栈为空的话，则pop出help栈中的元素入res栈，这样元素顺序颠倒，符合队列的顺序
	if len(this.resStack) == 0{
		for len(this.helpStack) > 0 {
			this.resStack = append(this.resStack, this.helpStack[len(this.helpStack)-1])
			this.helpStack = this.helpStack[:len(this.helpStack)-1]
		}
	}
	// 如果此时res栈仍然为空的话，代表并没有入栈元素，直接返回-1
	if len(this.resStack) == 0{
		return -1
	}else {
		temp := this.resStack[len(this.resStack)-1]
		this.resStack = this.resStack[:len(this.resStack)-1]
		return temp
	}
}

func main() {
	obj := Constructor1()
	obj.AppendTail(1)
	obj.AppendTail(2)
	obj.AppendTail(3)
	obj.AppendTail(4)
	param2 := obj.DeleteHead()
	fmt.Println(param2)
}
