# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         1047_removeDuplicates
# Description:  1047. 删除字符串中的所有相邻重复项
# Author:       skymoon9406@gmail.com
# Date:         2020/8/8
# -------------------------------------------------------------------------------


class Solution:
    def removeDuplicates(self, S: str) -> str:
        # 初始化一个栈
        stack = []
        for temp in S:
            if len(stack) == 0 or temp != stack[-1]:
                stack.append(temp)
            else:
                stack.pop()
        return "".join(stack)


if __name__ == '__main__':
    a = "abbaca"
    print(Solution().removeDuplicates(a))
