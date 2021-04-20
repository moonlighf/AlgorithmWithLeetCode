/* *****************************************************
 * @File Name   : test
 * @Author      : SkyMoon
 * @Email       : skymoon9406@gmail.com
 * @Create Date : 2021/4/1
 * @Description :
 * *****************************************************/
package main

import (
	"fmt"
)


func main() {
	needle, haystack := "issipi", "mississippi"
	fmt.Println(strStr(haystack, needle))
	needle, haystack = "ll", "hello"
	fmt.Println(strStr(haystack, needle))
	needle, haystack = "issip", "mississippi"
	fmt.Println(strStr(haystack, needle))
}


func strStr(haystack string, needle string) int {
	hLength, nLength := len(haystack), len(needle)
	// 处理特殊情况
	if nLength == 0{
		return 0
	}
	if hLength <nLength {
		return - 1
	}
	if hLength == nLength {
		if haystack == needle {
			return 0
		}else {
			return  - 1
		}
	}
	// 初始化两个指针，分别指向两个字符串的头部
	lPoint, rPoint := 0 , 0
	ans := -1
	// 利用两个指针分别从h字符串的头部开始遍历
	for rPoint <= hLength {
		// 如果两个字符串中间的字符串长度大于n字符串的长度，那么才可能出现n字符串，否则右边指针后移
		// 相当于找到一个和n字符串长度相同的窗口，然后判断和n字符串是否相同，如果相同则返回，否则移动左右指针形成新的窗口
		if rPoint - lPoint + 1 > nLength {
			if haystack[lPoint:rPoint] == needle {
				ans = lPoint
				break
			} else {
				lPoint++
			}
		}
		rPoint++
	}
	return ans
}


func strStr2(haystack string, needle string) int {
	// 暴力解法，直接利用两次循环
	n, m := len(haystack), len(needle)
outer:
	for i := 0; i+m <= n; i++ {
		for j := range needle {
			if haystack[i+j] != needle[j] {
				continue outer
			}
		}
		return i
	}
	return -1
}

func strStr3(haystack, needle string) int {
	// KMP算法
	// 处理特殊情况
	n, m := len(haystack), len(needle)
	if m == 0 {
		return 0
	}
	// 创建pi函数
	pi := make([]int, m)
	for i, j := 1, 0; i < m; i++ {
		for j > 0 && needle[i] != needle[j] {
			j = pi[j-1]
		}
		if needle[i] == needle[j] {
			j++
		}
		pi[i] = j
	}
	for i, j := 0, 0; i < n; i++ {
		for j > 0 && haystack[i] != needle[j] {
			j = pi[j-1]
		}
		if haystack[i] == needle[j] {
			j++
		}
		if j == m {
			return i - m + 1
		}
	}
	return -1
}
