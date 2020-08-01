package main

import (
	"fmt"
)

type MinStack struct {
	// 通过数组（切片）来模拟栈
	RealStack []int
	HelpStack []int
}

func Constructor() MinStack {
	return MinStack{
		RealStack: []int{},
		HelpStack: []int{},
	}
}
func (this *MinStack) Push(x int)  {
	// 往原始栈中添加元素
	this.RealStack = append(this.RealStack, x)
	// 同时需要保证辅助栈的栈顶元素仍然是最小元素
	// 如果辅助栈栈顶元素为空需要入栈，或者如果待入栈元素小于辅助栈的栈顶元素，需要入栈
	if len(this.HelpStack) ==0 || this.HelpStack[len(this.HelpStack)-1] > x {
		this.HelpStack = append(this.HelpStack, x)
	}else {
		// 如果待入栈元素大于辅助栈的栈顶元素，为保证辅助栈出栈是长度一致，将最小值继续入栈
		this.HelpStack = append(this.HelpStack, this.HelpStack[len(this.HelpStack)-1])
	}
}


func (this *MinStack) Pop()  {
	// 如果原始栈不为空，则直接从原始栈栈顶弹出元素，注意辅助栈也要做同样的操作
	if len(this.RealStack) !=0 {
		this.RealStack = this.RealStack[:len(this.RealStack)-1]
		this.HelpStack = this.HelpStack[:len(this.HelpStack)-1]
	}
}


func (this *MinStack) Top() int {
	// 如果栈不为空，直接返回原始栈的栈顶元素
	if len(this.RealStack) > 0 {
		return this.RealStack[len(this.RealStack)-1]
	}else {
		return 0
	}
}


func (this *MinStack) GetMin() int {
	// 如果栈不为空，直接返回辅助栈的栈顶元素
	if len(this.HelpStack) > 0 {
		return this.HelpStack[len(this.HelpStack)-1]
	} else {
		// 如果为空栈只能返回0，因为golang语言的零值特性
		return 0
	}
}

func main() {
	obj := Constructor()
	obj.Push(3)
	obj.Push(4)
	obj.Push(5)
	obj.Push(6)
	obj.Pop()
	param3 := obj.Top()
	param4 := obj.GetMin()
	fmt.Println(param3)
	fmt.Println(param4)
}
