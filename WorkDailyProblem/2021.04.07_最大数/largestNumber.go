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
	"strconv"
	"strings"
)

func main() {
	height := []int{3,30,34,5,9}
	fmt.Println(largestNumber(height))
}

func largestNumber(nums []int) string {
	// 将数组数字转换为字符串
	numsStr := make([]string, len(nums))
	for i := 0; i < len(nums); i++ {
		numsStr[i] = strconv.Itoa(nums[i])
	}
	// 将字符串数组进行排序
	sort.Slice(numsStr, func(x, y int) bool {
		return numsStr[x]+numsStr[y] >= numsStr[y]+numsStr[x]
	})
	res := strings.Join(numsStr, "")
	if res[0] == '0' {
		return "0"
	}
	return res
}