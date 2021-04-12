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