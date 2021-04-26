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
	weights := []int{3,3,3,3,3,3}
fmt.Println(shipWithinDays(weights, 2))
}

func shipWithinDays(weights []int, D int) int {
	// 由于需要保证运输的顺序，所以获取前n项和方便计算
	weightsSum, sumVal := make([]int, len(weights) + 1), 0
	// 同时获取包裹的重量的最大值和所有包裹的总和
	maxWeight := weights[0]
	for k, num := range weights {
		weightsSum[k + 1] = sumVal + num
		sumVal = sumVal + num
		if maxWeight <= num{
			maxWeight = num
		}
	}
	l, r := maxWeight, weightsSum[len(weights)]
	helper(weightsSum, D, 9)
	// 利用二分法来判断每日的最低限重
	for l < r{
		mid := l + (r - l) / 2
		// 判断此时的mid作为最低限重能否在D天内完成
		status := helper(weightsSum, D, mid)
		if status {
			// 如果可以，那么缩小最低限重，如果不行，则扩大最低限重
			r = mid
		} else {
			l = mid + 1
		}
	}
	return l
}

func helper(weightsSum []int, D int, limit int) bool {
	day := 0
	start := 0
	for k, val := range weightsSum{
		if val - weightsSum[start] > limit{
			start = k - 1
			day ++
		}else if val - weightsSum[start] == limit{
			start = k
			day ++
		}
	}
	// 如果此时的start不在末尾，那么代表最后还有需要运输的包裹
	if start < len(weightsSum) - 1{
		day ++
	}
	if day <= D {
		return true
	} else {
		return false
	}
}



