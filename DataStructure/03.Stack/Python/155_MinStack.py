# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         155_MinStack
# Description:  155. 最小栈
# Author:       skymoon9406@gmail.com
# Date:         2020/7/26
# -------------------------------------------------------------------------------


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 用于储存真正的栈
        self.real_stack = []
        # 用于辅助存储最小值于栈顶，方便能在常数时间内找到最小值
        self.help_stack = []

    def push(self, x: int) -> None:
        # 原栈push进一个元素，就是正常操作
        self.real_stack.append(x)
        # 此时辅助栈则需要判断待入栈的元素和此时的栈顶元素的大小关系
        if len(self.help_stack) == 0 or self.help_stack[-1] > x:
            # 如果此时辅助栈为空，或者栈顶元素大于待入栈元素，则待入栈元素入栈
            self.help_stack.append(x)
        else:
            # 如果栈顶元素小于待入栈元素，则直接重复入栈顶元素一次，这样保证和原栈的长度相同
            # 在进行pop操作的时候不会出现辅助栈先为空的情况，同时当pop操作后，辅助栈顶仍然是原栈的最小值
            self.help_stack.append(self.help_stack[-1])

    def pop(self) -> None:
        # 对于不为空的栈，直接pop出去栈顶元素即可
        if len(self.real_stack) > 0:
            self.help_stack.pop(-1)
            return self.real_stack.pop(-1)

    def top(self) -> int:
        # 直接返回原栈的栈顶元素即可
        if len(self.real_stack) > 0:
            return self.real_stack[-1]

    def getMin(self) -> int:
        # 直接返回辅助栈的栈顶元素即可
        if len(self.help_stack) > 0:
            return self.help_stack[-1]


if __name__ == '__main__':
    obj = MinStack()
    obj.push(6)
    obj.push(5)
    obj.push(3)
    obj.push(4)
    obj.push(7)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()

    c = 3
