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
	nums := []int{2,3,2}
	fmt.Println(rob(nums))
}

func rob(nums []int) int {
	// 动态规划，利用dp[i]数组表示数组前i个房间能偷到的做大值
	numsLen := len(nums)
	// 处理特殊情况
	if numsLen == 0{
		return 0
	}else if numsLen == 1{
		return nums[0]
	}else if numsLen == 2 {
		return max(nums[0], nums[1])
	}
	// 考虑题意，第一间和最后一间不能同时抢劫，那么就存在两种情况，
	// (1)抢劫第一家，那么res1 = rob(0, n-2)
	// (2)不抢劫第一家，那么res2 = rob(1, n-1)
	// 最终结果即为两者中的较大值  res = max(res1, res2)
	return max(dpHandle(0, numsLen - 2, nums), dpHandle(1, numsLen -1, nums))
}

func dpHandle(start, end int, nums []int) int {
	// 用于处理nums数组的[start, end]区间的抢劫的最大值
	// 由于dp[i]（前i个房间抢劫的最大值）只和dp[i-1]有关，这里放弃dp数组存储，只保留变量存储前一个值
	first, second :=nums[start], max(nums[start], nums[start + 1])
	for i := start + 2; i < end + 1; i++ {
		first, second = second, max(first + nums[i], second)
	}
	return second
}

func max(val1, val2 int) int {
	if val1 < val2{
		return val2
	}else {
		return val1
	}
}
