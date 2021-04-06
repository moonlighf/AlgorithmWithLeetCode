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
	height := []int{0,0,1,1,1,1,2,3,3}
	fmt.Println(removeDuplicates(height))
}

func removeDuplicates(nums []int) int {
	count := 1
	j := 1
	for i := 1; i < len(nums); i++ {
		// 判断是否和前一个数相同，如果相同则计数加1
		if nums[i] == nums[i - 1]{
			count +=1
		}else {
			// 如果不相同代表是遇到了新的数，此时计数重置
			count = 1
		}
		// j用于存储新数已经存储的位置。如果超出了2，则不会被按j的顺序存储
		if count <= 2{
			nums[j] = nums[i]
			j ++
		}
	}
	return j
}