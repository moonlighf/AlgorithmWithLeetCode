# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         739_dailyTemperatures
# Description:  739. 每日温度
# Author:       skymoon9406@gmail.com
# Date:         2020/7/19
# -------------------------------------------------------------------------------
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        可以运用一个堆栈 stack 来快速地知道需要经过多少天就能等到温度升高。
        从头到尾扫描一遍给定的数组 T，如果当天的温度比堆栈 stack 顶端所记录的那天温度还要高，那么就能得到结果。
        """
        # 处理特殊情况
        days = len(T)
        if days == 0 or T is None:
            return []
        # 初始化一个栈，用于暂存每天的温度和其下标，为了方便，第一天的温度和下标直接入栈
        stack = [(0, T[0])]
        # 初始化结果数组
        result = [0] * days
        # 遍历温度列表
        for index in range(1, days):
            # 如果小于栈顶元素，那么此时的温度入栈
            if T[index] <= stack[-1][1]:
                stack.append((index, T[index]))
            else:
                # 否则从栈顶pop出元素（此时pop出的元素一定小于待入栈元素），直到找到比待入栈元素大的
                while len(stack) > 0 and stack[-1][1] < T[index]:
                    current_top = stack.pop()
                    # 计算所需要的天数
                    result[current_top[0]] = index - current_top[0]
                    # 继续和栈顶元素做判断
            # 当找不到栈中比该元素小的后，将该元素入栈
            stack.append((index, T[index]))
        return result

