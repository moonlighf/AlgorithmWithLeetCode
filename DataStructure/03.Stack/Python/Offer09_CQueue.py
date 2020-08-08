# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         Offer09_CQueue
# Description:  剑指 Offer 09. 用两个栈实现队列
# Author:       skymoon9406@gmail.com
# Date:         2020/8/8
# -------------------------------------------------------------------------------


class CQueue:

    def __init__(self):
        # 初始化两个栈，分别维护入队列和出队列的操作
        # 队列是先进先出，只能在头部删除出队列，在尾部入队列
        self.res_stack, self.help_stack = [], []

    def appendTail(self, value: int) -> None:
        self.help_stack.append(value)

    def deleteHead(self) -> int:
        # res_stack为空，则将help栈中的元素pop然后入栈到res栈，这样res栈中的元素顺序和原help中的元素相反，符合队列
        # 的特征
        if len(self.res_stack) == 0:
            while len(self.help_stack) > 0:
                self.res_stack.append(self.help_stack.pop())

        # 如果此时的res栈仍然为空，代表help栈为空，所以直接返回-1
        if len(self.res_stack) == 0:
            return -1
        else:
            # 否则从新的res栈中pop出栈顶元素，即为队列的队尾元素
            return self.res_stack.pop()


# Your CQueue object will be instantiated and called as such:
obj = CQueue()

obj.appendTail(1)
obj.appendTail(2)
obj.appendTail(3)
param_1 = obj.deleteHead()
param_2 = obj.deleteHead()
param_3 = obj.deleteHead()
obj.appendTail(4)
obj.appendTail(5)
param_4 = obj.deleteHead()
print(param_1)
print(param_2)
