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
	nums := []int{3,2,2,3, 1, 2, 4}
	fmt.Println(removeElement(nums, 3))
}


func removeElement(nums []int, val int) int {
	// 整体思路：遍历整个数组，对于符合要求的数值，和数组末尾进行交换
	cnt, index := len(nums) - 1, 0
	for index <= cnt {
		// 如果找到符合要求的值，则和数组末尾进行交换
		if nums[index] == val{
			nums[index], nums[cnt] = nums[cnt], nums[index]
			// 然后记录数组末尾的值向前移动一位
			cnt --
			// 同时index的值不增，保证继续判断交换到前面的来的值不是目标值
		}else {
			// 如果不符合要求的值，那么index则前移一位
			index ++
		}
	}
	// 最终cnt移动的位置即为非目标值的元素的个数
	return cnt + 1
}
