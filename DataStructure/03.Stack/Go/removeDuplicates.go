package main

func removeDuplicates(S string) string {
	var stack []string
	for i:=0; i< len(S); i++{
		char := S[i]
		if len(stack) == 0 || string(char) != stack[len(stack)-1]{
			stack = append(stack, string(char))
		} else {
			stack = stack[:len(stack)-1]
		}
	}
	res := ""
	for _, ch := range stack{
		res = res + string(ch)
	}
	return res
}

func main() {
	a := "abbaca"
	removeDuplicates(a)
}
