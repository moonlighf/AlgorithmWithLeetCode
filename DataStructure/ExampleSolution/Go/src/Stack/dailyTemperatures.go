package main

import (
	"fmt"
)

func dailyTemperatures(T []int) []int {
	// 初始化一个栈用于存储温度
	var stack []int
	// 初始化一个结果数组(切片)
	var res = make([]int, len(T))
	// 遍历温度数组
	for i:=0; i< len(T); i++{
		temperature := T[i]
		for len(stack) > 0 && temperature > T[stack[len(stack)-1]] {
			// 如果待入栈的温度大于栈顶的温度（且栈中还有元素的话）
			// 栈顶元素pop出来
			prevIndex := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			res[prevIndex] = i - prevIndex
		}
		stack = append(stack, i)
	}
	return res
}

func main() {
	var temperatures =[]int{73, 74, 75, 71, 69, 72, 76, 73}
	var status = dailyTemperatures(temperatures)
	fmt.Println(status)
}
