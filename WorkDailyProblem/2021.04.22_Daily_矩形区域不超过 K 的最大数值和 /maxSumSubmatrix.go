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
	matrix := [][]int{{1,0,1}, {0, -2, 3}}
	fmt.Println(maxSumSubmatrix3(matrix, 2))

	matrix2 := []int{4, 3, -1, -7, -9, 6, 2, -7}
	fmt.Println(dpmax(matrix2, 2))
}

func maxSumSubmatrix3(matrix [][]int, k int) int{
	row, col, max := len(matrix), len(matrix[0]),  math.MinInt32
	for l := 0; l < col; l++ {
		// 固定左边界l，移动右边界r，然后利用rowSum数组记录左右边界的每一行的和
		rowSum := make([]int, row)
		for r := l; r < col; r++ {
			for i := 0; i < row; i++ {
				rowSum[i] += matrix[i][r]
			}
			// 求 rowSum 连续子数组 的 和, 且保证和尽量大，但不大于 k
			max = maxValue(max, dpmax(rowSum, k))
		}
	}
	return max
}

func dpmax(rowSum []int, k int) int {
	// 用于返回一唯数组连续的不大于k的最大子数组的和
	sum, max := rowSum[0], rowSum[0]
	for i := 1; i < len(rowSum); i++ {
		sum = maxValue(sum + rowSum[i], rowSum[i])
		if sum > max {
			max = sum
		}
	}
	if max <= k {
		return max
	} else {
		max = math.MinInt32
		for l := 0; l < len(rowSum); l++ {
			sum = 0
			for r := l; r < len(rowSum); r++ {
				sum += rowSum[r]
				if sum > max && sum <= k{
					max = sum
				}
				if max == k {
					return k
				}
			}
		}
		return max
	}
}

func maxValue(val1, val2 int) int {
	if val1 < val2{
		return val2
	}else {
		return val1
	}
}

func maxSumSubmatrix2(matrix [][]int, k int) int{
	// 根据maxSumSubmatrix1发现实际上遍历到下一个(i1,j1)时和上一个的dp[i1-1][j1-1]无关，所以只需要存储右下角dp即可
	row, col, max := len(matrix), len(matrix[0]),  math.MinInt32
	// 遍历dp数组，填充dp数组
	for i1 := 1; i1 <= row; i1++ {
		for j1 := 1; j1 <= col; j1++ {
			// 相较于maxSumSubmatrix1,在此处初始化dp数组，只保存右下角的值
			dp := make([][]int, row + 1)
			for i := range dp{
				dp[i] = make([]int, col + 1)
			}

			dp[i1][j1] = matrix[i1-1][j1-1]
			for i2 := i1; i2 <= row; i2++ {
				for j2 := j1; j2 <= col; j2++ {
					dp[i2][j2] = dp[i2-1][j2] + dp[i2][j2 - 1] - dp[i2-1][j2-1] + matrix[i2-1][j2-1]
					if dp[i2][j2] <= k && dp[i2][j2] > max {
						max = dp[i2][j2]
					}
				}
			}
		}
	}
	return max
}


func maxSumSubmatrix1(matrix [][]int, k int) int {
	// 利用dp[][][][]四维数组来存储左上角（i1,j1）到右下角（i2,j2）之间矩形的值的和
	row, col, max := len(matrix), len(matrix[0]),  math.MinInt32
	// 初始化dp数组
	dp := make([][][][]int, row + 1)
	for i := range dp{
		dp[i] = make([][][]int, col + 1)
		for j := range dp[i]{
			dp[i][j] = make([][]int, row + 1)
			for m := range dp[i][j]{
				dp[i][j][m] = make([]int, col + 1)
			}
		}
	}
	// 遍历dp数组，填充dp数组
	for i1 := 1; i1 <= row; i1++ {
		for j1 := 1; j1 <= col; j1++ {
			dp[i1][j1][i1][j1] = matrix[i1 - 1][j1 - 1]
			for i2 := i1; i2 <= row; i2++ {
				for j2 := j1; j2 <= col; j2++ {
					dp[i1][j1][i2][j2] = dp[i1][j1][i2-1][j2] + dp[i1][j1][i2][j2 - 1] - dp[i1][j1][i2-1][j2-1] + matrix[i2-1][j2-1]
					if dp[i1][j1][i2][j2] <= k && dp[i1][j1][i2][j2] > max {
						max = dp[i1][j1][i2][j2]
					}
				}
			}
		}
	}
	return max
}


