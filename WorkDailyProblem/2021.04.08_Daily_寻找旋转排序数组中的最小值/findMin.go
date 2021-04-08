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
	height := []int{3,1,2}
	fmt.Println(findMin(height))
}

func findMin(nums []int) int {
	start, end := 0, len(nums) - 1
	for start < end {
		mid := start + (end - start) / 2
		if nums[mid] < nums[end]{
			end = mid
		}else {
			start = mid + 1
		}
	}
	return nums[start]
}