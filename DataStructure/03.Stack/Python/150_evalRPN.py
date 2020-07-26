# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         150_evalRPN
# Description:  150. 逆波兰表达式求值
# Author:       skymoon9406@gmail.com
# Date:         2020/7/26
# -------------------------------------------------------------------------------
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中，方便之后的运算符运算
        """
        tokens_length = len(tokens)
        # 初始化一个栈用于存储数字
        stack = []
        # 存储运算符
        char_list = ["+", "-", "*", "/"]
        # 遍历含有数字和运算符的列表
        for i in range(tokens_length):
            # 如果是数字直接入栈
            if tokens[i] not in char_list:
                # 这里需要判断字符是否在列表（数组）中，时间复杂度应该是O（N），但运算符数组是常数，这里的时间复杂度
                # 应该还是常数级别
                stack.append(tokens[i])
            else:
                # 如果是运算符，则从栈顶pop两个数字进行计算
                num1 = stack.pop(-1)
                num2 = stack.pop(-1)
                # Python中的eval函数可以将字符串转换为可以执行的方法
                # 但是我觉得这样可能更好理解，用字典处理，键是操作符，值是匿名函数，然后通过键调用即可
                """
                maps = {
                    '+': lambda a, b: a + b, 
                    '-': lambda a, b: a - b, 
                    '*': lambda a, b: a * b, 
                    '/': lambda a, b: a / b
                }
                """
                result = (str(int(eval(num2+tokens[i]+num1))))
                stack.append(result)
        # 最后输出栈顶元素即可
        return int(stack[-1])


if __name__ == '__main__':
    a = ["2", "1", "+", "3", "*"]
    print(Solution().evalRPN(a))
