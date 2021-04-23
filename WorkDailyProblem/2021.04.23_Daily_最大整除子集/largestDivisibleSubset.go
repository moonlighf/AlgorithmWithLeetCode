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
	"sort"
)

func main() {
	matrix := []int{4, 8, 10, 240}
	fmt.Println(largestDivisibleSubset(matrix))
}


func largestDivisibleSubset(nums []int) []int {
	// 动态规划。利用dp[i]表示以nums[i]为最大值的升序数组子集的长度
	numsLength, res := len(nums), make([]int, 0)
	// 处理特殊情况
	if numsLength == 0 {
		return res
	}
	// 数组排序，以方便进行遍历比较
	sort.Ints(nums)
	// 初始化dp数组用以存储升序数组整除子集的长度
	dp := make([]int, numsLength)
	for i := 0; i < numsLength; i++ {
		dp[i] = 1
	}
	dp[0] = 1
	// 遍历，填充dp数组
	maxSize, maxVal := 1, 1
	for i := 1; i < numsLength; i++ {
		// dp[i]表示以nums[i]为最大值的子集的长度
		// 由于已经排序，所以nums[i]一定大于nums[i-1]，如果nums[i]是nums[i-1]的倍数，那么一定是dp[i-1]所包含的其他值的倍数，
		// 那么dp[i]即可在dp[i-1]的基础上+1 ，同理，继续往前遍历，找到其他是否能整除的dp，否则就只能是本身，所以最开始dp数组全初始化为1
		for k, v := range nums[:i]{
			if nums[i] % v == 0 && dp[k]+1 > dp[i]{
				dp[i] = dp[k] + 1
			}
			if dp[i] > maxSize {
				maxSize, maxVal = dp[i], nums[i]
			}
		}
	}
	if maxSize == 1 {
		return []int{nums[0]}
	}
	// 此时已经得到了以maxVal为最大值的子集最大的长度maxSize，接着需要从nums数组中还原出对应的子集
	for i := numsLength - 1; i >= 0 && maxSize > 0; i-- {
		// 不断缩减maxSize的大小，且保证新的子集的最大值maxVal能被之前的maxVal整除 例如
		//nums	2	4	7	8	9	12	16	20
		//dp	1	2	1	3	1	3   4	3
		// 根据dp 的计算结果，maxSize=4 maxSize=4, 因此大小为 4 的最大整除子集包含的最大整数为 16；
		// 然后查找大小为 3 的最大整除子集，我们看到 8 和 12 对应的状态值都是 3，最大整除子集一定包含 8，这是因为 8 能被16整除
		// 然后查找大小为 2 的最大整除子集，我们看到 4 对应的状态值是 2，最大整除子集一定包含 4；
		// 然后查找大小为 1 的最大整除子集，我们看到 2/7/9 对应的状态值是 1，最大整除子集一定包含 2，因为2能被4整除 。
		if dp[i] == maxSize && maxVal % nums[i] == 0 {
			res = append(res, nums[i])
			maxVal = nums[i]
			maxSize--
		}
	}
	return res
}


