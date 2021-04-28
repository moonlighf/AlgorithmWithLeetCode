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
)

func main() {
	fmt.Println(judgeSquareSum2(11))
}





func judgeSquareSum3(c int) bool {
	// 双指针，O(n)时间复杂度遍历小于c的所有值进行测试，但是会超时
	for i, j := 0, c; i <= j; {
		if i * i + j * j < c{
			i ++
		}else if i * i + j * j > c{
			j --
		} else {
			return true
		}
	}
	return false
}

func judgeSquareSum2(c int) bool {
	// 双指针优化，j的初始值从c^(1/2)开始
	for i, j := 0, int(math.Sqrt(float64(c))); i <= j; {
		if i * i + j * j < c{
			i ++
		}else if i * i + j * j > c{
			j --
		} else {
			return true
		}
	}
	return false
}

func judgeSquareSum(c int) bool {
	// 如果要满足a^2 + b^2 = c，那么当我们确定一个a后，只需要判断b=(c-a^2)^(1/2)是否是整数即可
	for a := 0; a*a <= c; a++ {
		rt := math.Sqrt(float64(c - a*a))
		if rt == math.Floor(rt) {
			return true
		}
	}
	return false
}


