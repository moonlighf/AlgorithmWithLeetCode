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
	s1, s2 := "eebaacbcbcadaaedceaaacadccd", "eadcaacabaddaceacbceaabeccd"
	fmt.Println(isScramble(s1, s2))
}

func isScramble(s1 string, s2 string) bool {
	// 处理特殊情况
	if len(s1) != len(s2) {
		return false
	}

	n := len(s1)
	// dp数组用于存储之前的状态，防止在dfs中递归的时候重复计算
	dp := make([][][]int8, n)
	for i := range dp {
		dp[i] = make([][]int8, n)
		for j := range dp[i] {
			dp[i][j] = make([]int8, n+1)
			for k := range dp[i][j] {
				dp[i][j][k] = -1
			}
		}
	}

	var dfs func(i1, i2, length int) int8
	dfs = func(i1, i2, length int) (res int8) {
		d := &dp[i1][i2][length]
		if *d != -1 {
			return *d
		}
		defer func() { *d = res }()

		// 如果两个字符串相同，则一定是扰乱
		if s1[i1: i1+length] == s2[i2: i2+length]{
			return 1
		}
		// 如果两个字符串中的相同字符串的个数不同，则一定不是扰乱的
		if !getFrequency(s1[i1: i1+length], s2[i2: i2+length]){
			return 0
		}
		// 除了以上两种情况，则是通常情况，假设s1[i1: i1+length] 为t1， s2[i2: i2+length]为t2,
		// 则需要按照题意遍历两个字符串中的每个位置作为切割位，判断切割后的字符串是否为扰乱的
		// t1切割为t1l 和 t1r，t2切割为t2l 和 t2r
		// 则（1）t1l和t2l是扰乱的，t1r和t2r是扰乱的   （2）t1l和t2r是扰乱的，t1r和t2l是扰乱的
		for index := 1; index < length; index++ {
			// 不交换的情况
			if dfs(i1, i2, index) == 1 && dfs(i1 + index, i2 + index, length - index) == 1 {
				return 1
			}
			// 交换的情况
			if dfs(i1, i2 + length - index, index) == 1 && dfs(i1 + index, i2, length - index) == 1{
				return 1
			}
		}
		//  如果以上都不满足，则返回false
		return 0
	}

	return dfs(0, 0, len(s1)) == 1
}

func getFrequency(var1, var2 string) bool {
	// 获取字符串中每个字符的频率
	frequency := make(map[uint8]int)
	for i := 0; i < len(var1); i++ {
		frequency[var1[i]] += 1
		frequency[var2[i]] -= 1
	}
	// 如果此时的map中存在一个key的value不为0，则代表存在一个字符串，在s1和s2中出现的次数不同
	for key, _ := range frequency{
		if frequency[key] != 0{
			return false
		}
	}
	return true
}
