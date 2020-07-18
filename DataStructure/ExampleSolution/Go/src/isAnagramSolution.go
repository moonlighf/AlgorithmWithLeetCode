package main

import (
	"fmt"
)

func isAnagram(s string, t string) bool {
	// 处理特殊情况
	if len(s) != len(t){
		return false
	}
	// 声明一个哈希表(map)来储存输入字符串中字母出现的次数
	// go语言中的map是安全的，即使元素不在map中，查找失败将返回value类型对应的零值
	strCountNum := make(map[string]int)

	// 遍历两个字符串，统计其中各个字符出现的次数
	for _, tempStr := range s{
		// 由于这样遍历得到的tempStr是对应字符的ascii码，所以需要转换为string类型，才能在map中索引
		strCountNum[string(tempStr)] += 1
	}
	for _, tempStr := range t{
		strCountNum[string(tempStr)] -= 1
		// 提前结束遍历
		if strCountNum[string(tempStr)] < 0{
			return false
		}
	}
	return true
}

func main() {
	var s string = "anagram"
	var t string = "nagaram"
	fmt.Println(isAnagram(s, t))
}
