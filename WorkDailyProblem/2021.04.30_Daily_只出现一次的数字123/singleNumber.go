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
	nums := []int{2,2,1}
	fmt.Println(singleNumber(nums))
	// 12345 -> 11000000111001
	nums2 := []int{2,2, 2, 1}
	fmt.Println(singleNumber2(nums2))
	nums3 := []int{1,2,1,3,2,5}
	fmt.Println(singleNumber3(nums3))
}


func singleNumber(nums []int) int {
	// 只出现一次的数字-i，除了目标值外，其他值出现了两次
	// 由于除了目标值外，其他值均出现了两次，那么可以根据二进制对应位数相加，最后只有目标值会在该位上为1
	//   1 0 0 1    7
	//   1 0 0 1    7
	//   0 0 0 1    1
	//   2 0 0 3
	res := int32(0)
	for i := 0; i < 32; i++ {
		digitTotal := int32(0)
		for _, num := range nums{
			// 获取当前位的所有数的总和
			digitTotal += int32(num) >> i & 1
		}

		// 判断当前位是否能被2整除，因为除目标值外，其他值都是2个，所以不考虑目标值，则当前位一定是2的倍数，如果不符合，则当前位一定有目标值的影响
		// 通过1<<i获取当前位的基础值，由于二进制某一位不为0则一定为1,所以直接按位或即可,相当有加上当前位的基础值
		if digitTotal % 2 != 0 {
			res |= 1 << i
		}
	}
	return int(res)
}

func singleNumber2(nums []int) int {
	// 只出现一次的数字-ii，除了目标值外，其他值出现了三次
	// 由于除了目标值外，其他值均出现了三次，那么可以根据二进制对应位数相加，最后的值一定是3的倍数 + 目标值在当前位上的值
	//   1 0 0 1    7
	//   1 0 0 1    7
	//   0 0 0 1    1
	//   2 0 0 3
	res := int32(0)
	for i := 0; i < 32; i++ {
		digitTotal := int32(0)
		for _, num := range nums{
			// 获取当前位的所有数的总和
			digitTotal += int32(num) >> i & 1
		}

		// 判断当前位是否能被2整除，因为除目标值外，其他值都是2个，所以不考虑目标值，则当前位一定是2的倍数，如果不符合，则当前位一定有目标值的影响
		// 通过1<<i获取当前位的基础值，由于二进制某一位不为0则一定为1,所以直接按位或即可,相当有加上当前位的基础值
		if digitTotal % 2 != 0 {
			res |= 1 << i
		}
	}
	return int(res)
}


func singleNumber3(nums []int) []int {
	// 只出现一次的数字-iii，除了两个目标值外，其他值出现了两次
	// 分组异或，通过将两个目标值分到两个组，保证每个组中除了目标值外的数都是成对存在的，这样问题就转变为了问题1
	// 对nums中所有数进行异或操作，由于相同数的异或为0,那么最终结果就是两个目标值a，b的异或
	res, div := 0, 1
	for _, num := range nums{
		res = res ^ num
	}
	// 此时对于res二进制数的每一位xi，如果xi为1,则代表a和b对应位的值ai和bi相同，否则ai和bi不同
	// 为了区分出a和b，那么只需要取res中某一位为0的值即可，根据该位是否相同来进行分组
	for div & res == 0{
		// div: 01  10  100  1000
		// div   1   2   4   8
		div <<= 1
	}
	// 此时找到了从低位往高位数的第一个为0的位数div
	// 此处就不再存储两个数组了，直接用  a和b  和 本应存储a和b的数组的所有值进行异或即可
	a, b := 0, 0
	for _, num := range nums{
		if num & div == 0{
			a ^= num
		}else {
			b ^= num
		}
	}
	return []int{a, b}
}