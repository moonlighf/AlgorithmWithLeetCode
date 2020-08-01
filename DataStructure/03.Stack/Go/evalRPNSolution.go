package main

import (
	"fmt"
	"strconv"
)

func evalRPN(tokens []string) int {
	// 初始化一个栈（此处用切片代替），存储待计算的数字
	// 或者切片的方式这样声明
	// stack := make([]int, len(tokens))
	var stack []int
	// 遍历原始元素数组
	// 遍历也可以采用 for i, _ :=  range tokens {} 的形式 其中i是下标
	for i:=0; i < len(tokens); i++{
		// 如果是运算符，则弹出两个栈顶元素进行运算，并将结果入栈
		switch tokens[i] {
		case "+":
			func(n1 int, n2 int) {
				stack = stack[:len(stack)-2]
				stack = append(stack, n2+n1)
			}(stack[len(stack)-1], stack[len(stack)-2])
		case "-":
			func(n1 int, n2 int) {
				stack = stack[:len(stack)-2]
				stack = append(stack, n2-n1)
			}(stack[len(stack)-1], stack[len(stack)-2])
		case "*":
			func(n1 int, n2 int) {
				stack = stack[:len(stack)-2]
				stack = append(stack, n2*n1)
			}(stack[len(stack)-1], stack[len(stack)-2])
		case "/":
			func(n1 int, n2 int) {
				stack = stack[:len(stack)-2]
				stack = append(stack, n2/n1)
			}(stack[len(stack)-1], stack[len(stack)-2])
		default:
			num, _ := strconv.Atoi(tokens[i])
			stack = append(stack, num)
		}
	}
	return stack[0]
}

func main() {
	var tokens =  []string{"2", "1", "+", "3", "*"}
	fmt.Println(evalRPN(tokens))
}
