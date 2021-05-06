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
	nums := []int{1,2,3}
	first := 1
	fmt.Println(decode(nums, first))

}

func decode(encoded []int, first int) []int {
	// 根据异或的性质 a ^ b = c   ===>  a = c ^ b
	// 那么只需要遍历结果数组进行异或即可
	var res []int
	for _, num := range encoded {
		res = append(res, first)
		first = num ^ first
	}
	// 最后一个结果没有加入到res数组中去
	res = append(res, first)
	return res
}










/*
未知 整数数组 arr 由 n 个非负整数组成。

经编码后变为长度为 n - 1 的另一个整数数组 encoded ，其中 encoded[i] = arr[i] XOR arr[i + 1] 。例如，arr = [1,0,2,1] 经编码后得到 encoded = [1,2,3] 。

给你编码后的数组 encoded 和原数组 arr 的第一个元素 first（arr[0]）。

请解码返回原数组 arr 。可以证明答案存在并且是唯一的。

 

示例 1：

输入：encoded = [1,2,3], first = 1
输出：[1,0,2,1]
解释：若 arr = [1,0,2,1] ，那么 first = 1 且 encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
示例 2：

输入：encoded = [6,2,7,3], first = 4
输出：[4,2,0,7,4]
*/