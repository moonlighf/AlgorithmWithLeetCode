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
	height := []int{0,1,0,2,1,0,1,3,2,1,2,1}
	fmt.Println(trap(height))
}
func trap(height []int) int {
	// 利用双指针来边移动边计算左右两边的最值，这样可以省去trap2中的备忘录的空间复杂度
	res := 0
	heightLength := len(height)
	if heightLength == 0{
		return res
	}
	leftPoint := 0
	rightPoint := heightLength - 1
	leftMax := height[0]
	rightMax := height[heightLength - 1]
	for leftPoint < rightPoint{
		leftMax = max(leftMax, height[leftPoint])
		rightMax = max(rightMax, height[rightPoint])

		if leftMax < rightMax {
			res += leftMax - height[leftPoint]
			leftPoint++
		} else {
			res += rightMax - height[rightPoint]
			rightPoint--
		}
	}
	return res
}



func trap2(height []int) int {
	// 同样是trap中的方法，此时利用备忘录来优化，从而减少时间复杂度，也就是利用两个数组来存储某个位置左右两边的最高值
	res := 0
	heightLength := len(height)
	if heightLength == 0{
		return res
	}
	leftMaxAry := make([]int, heightLength)
	rightMaxAry := make([]int, heightLength)
	// 0位置的左边最大值和末尾位置的右边最大值均是其本身
	leftMaxAry[0] = height[0]
	rightMaxAry[heightLength-1] = height[heightLength - 1]
	// 初始化每个位置的左右最大值
	for i := 1; i < len(height); i++ {
		leftMaxAry[i] = max(leftMaxAry[i-1], height[i])
	}
	for i := heightLength - 2 ; i >= 0; i-- {
		rightMaxAry[i] = max(height[i], rightMaxAry[i+1])
	}
	// 然后根据已知的每个位置的左右最值来计算
	for index :=1; index<len(height) - 1; index ++ {
		res += min(leftMaxAry[index], rightMaxAry[index]) - height[index]
	}
	return res
}


func trap1(height []int) int {
	// 主要思路是针对每个位置，判断该位置最多能储存的雨水数量
	// 例如height[5]此处能储存的雨水量应该等于其左右两边最大值中的较小值和该位置的值的差
	// 公式表示即为 water[5] = min(max[...:5], max[5:...]) - height[5]
	res := 0
	for index :=1; index<len(height) - 1; index ++ {
		leftMax := 0
		rightMax := 0
		// 找到index左边的最大值和右边的最大值
		for i := index; i < len(height); i++ {
			rightMax = max(height[i], rightMax)
		}
		for i := index; i >= 0; i-- {
			leftMax = max(height[i], leftMax)
		}
		res += min(leftMax, rightMax) - height[index]
	}
	return res
}

func max(nums...int) int {
	var maxNum int = -9223372036854775807
	for _, num := range nums {
		if num > maxNum {
			maxNum = num
		}
	}
	return maxNum
}

func min(nums ...int) int {
	var minNum int = 9223372036854775807
	for _, num := range nums {
		if num < minNum {
			minNum = num
		}
	}
	return minNum
}