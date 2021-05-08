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
	"math"
	"math/bits"
)

func main() {
	jobs := []int{2,9,17,6}
	k := 2
	fmt.Println(minimumTimeRequired(jobs, k))
}


func minimumTimeRequired(jobs []int, k int) int {
	n := len(jobs)
	// 利用sum数组存储工作总量，即sum[i]表示以i的二进制表示的工作集合的工作总量
	// 例如 sum[5] = sum(101)= jobs[0] + jobs[2] = 19
	// m用以表示n个工作状态的最大整数，即如果有4个工作，那么 m = 1111 = 15
	m := 1 << n
	sum := make([]int, m)
	for i := 1; i < m; i++ {
		x := bits.TrailingZeros(uint(i))
		y := i ^ 1<<x
		sum[i] = sum[y] + jobs[x]
	}
	// 动态规划，利用dp[i][j]表示给前 i 个人分配工作，工作的分配情况为 j 时，完成所有工作的最短时间
	// 这里的j是一个二进制数表示的十进制数，比如工作情况是1010（表示jobs[1]和jobs[3]工作被分配），那么j为10
	dp := make([][]int, k)
	for i := range dp {
		dp[i] = make([]int, m)
	}
	// 初始化dp数组的边界值，即分配给前1个工人i的工作时，其耗费的最短时间就是对应的sum的值，因为只有一个工人，所以时间就是这个人所有工作的耗时
	for i, s := range sum {
		dp[0][i] = s
	}
	// 遍历分配给所有员工所有的分配方案以填充dp数组
	for i := 1; i < k; i++ {
		for j := 0; j < m; j++ {
			minn := math.MaxInt64
			for x := j; x > 0; x = (x - 1) & j {
				// dp[i][j]表示假设工作分配给i个人，按照j集合分配工作时的最短时间
				minn = min(minn, max(dp[i-1][j-x], sum[x]))
			}
			dp[i][j] = minn
		}
	}

	return dp[k-1][m-1]
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}








/*
给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。

请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。

返回分配方案中尽可能 最小 的 最大工作时间 。

示例 1：

输入：jobs = [3,2,3], k = 3
输出：3
解释：给每位工人分配一项工作，最大工作时间是 3 。
示例 2：

输入：jobs = [1,2,4,7,8], k = 2
输出：11
解释：按下述方式分配工作：
1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
2 号工人：4、7（工作时间 = 4 + 7 = 11）
最大工作时间是 11 。
*/