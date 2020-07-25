package main

func isValid(s string) bool {
	// 处理特殊情况，针对字符串长度非偶数的字符串直接返回false
	var strLength = len(s)
	if strLength % 2 != 0 {
		return false
	}
	// 初始化一个栈用于储存括号，在go里面用变成的序列slice来模拟
	var stack []string
	// 初始化一个hashmap用于存储所有括号的对应关系 go语言中的map是安全的，即使元素不在map中，查找失败将返回value类型对应的零值
	bracketsMap := map[string]string{
		"{": "}",
		"[": "]",
		"(": ")",
	}
	// 遍历括号字符串
	for _, tempStr := range s {
		if _, ok := bracketsMap[string(tempStr)]; ok {
			// 如果是左括号，即是bracketMap的key，那么直接入栈
			stack = append(stack, string(tempStr))
		}else if len(stack) > 0{
			// 如果是右括号，那么把栈顶元素出栈并判断
			var topEle = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if string(tempStr) != bracketsMap[topEle]{
				return false
			}
		}else {
			return false
		}
	}
	if len(stack) == 0{
		return true
	} else {
		return false
	}
}

func main() {
	var bracketsStr = "()[]{}"
	var status = isValid(bracketsStr)
	println(status)
}
