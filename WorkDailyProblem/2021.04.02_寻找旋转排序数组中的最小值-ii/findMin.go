/* *****************************************************
 * @File Name   : test
 * @Author      : SkyMoon
 * @Email       : skymoon9406@gmail.com
 * @Create Date : 2021/4/1
 * @Description :
 * *****************************************************/
package main

import "fmt"

func main() {
	nums := []int{10,1,10,10,10}
	fmt.Println(findMin(nums))
}

func findMin(nums []int) int {
	numsLength := len(nums)
	if numsLength == 1 {
		return nums[0]
	}
	left := 0
	right := numsLength - 1
	for left<right {
		mid := left + (right - left) / 2
		if nums[mid] < nums[right]{
			right = mid
		}else if nums[mid] > nums[right]{
			left = mid + 1
		}else {
			right -= 1
		}
	}
	return nums[left]
}
