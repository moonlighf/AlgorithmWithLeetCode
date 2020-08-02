package main

import (
	"fmt"
	"strconv"
	"strings"
)

func decodeString(s string) string {
	// 初始化一个辅助栈用于辅助运算
	var stack[]int32
	for _, chr1 := range s{
		if chr1 != ']'{
			// 如果不是"]"则直接入栈
			stack = append(stack, chr1)
		} else {
			// 如果是"]" 则需要往前pop出相应的字符串和数字进行复制后再入栈
			// pop出待复制的字符串
			var tempStr = ""
			for stack[len(stack)-1] != '[' && len(stack)>0{
				tempStr = string(stack[len(stack)-1]) + tempStr
				stack = stack[:len(stack)-1]
			}
			// pop掉"["
			stack = stack[:len(stack)-1]
			// pop出待复制的字符串的次数
			var tempNumStr = ""
			for len(stack)>0 && stack[len(stack)-1] >=48 && stack[len(stack)-1]<= 57{
				tempNumStr = string(stack[len(stack)-1]) + tempNumStr
				stack = stack[:len(stack)-1]
			}
			tempNumInt, _ := strconv.Atoi(tempNumStr)
			// 将字符串复制
			afterStr := strings.Repeat(tempStr, tempNumInt)
			// 复制后的字符串入栈
			for _, chr2 := range afterStr{
				stack = append(stack, chr2)
			}
		}
	}
	// 将栈中的结果pop处理构成字符串
	res := ""
	for _, chr3 := range stack{
		res = res + string(chr3)
	}
	return res
}

func main() {
	var s =  "3[a2[c]]"
	fmt.Println(decodeString(s))
}