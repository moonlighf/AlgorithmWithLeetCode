# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         20_isValid
# Description:  20. 有效的括号
# Author:       skymoon9406@gmail.com
# Date:         2020/7/19
# -------------------------------------------------------------------------------

class Solution:
    def isValid(self, s: str) -> bool:
        """
        利用一个栈，不断地往里压左括号，一旦遇上了一个右括号，我们就把栈顶的左括号弹出来，
        表示这是一个合法的组合，以此类推，直到最后判断栈里还有没有左括号剩余
        """
        # 处理特殊情况，如果是奇数个括号，肯定是不可以的
        str_num = len(s)
        if str_num % 2 != 0:
            return False
        # 初始化一个栈（后进先出），此处用列表实现，也可以使用queue实现
        stack = []
        # 遍历括号字符串，不断压入左括号，匹配右括号
        brackets = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        for temp_str in s:
            # 如果是左括号则压入栈
            if temp_str in brackets.keys():
                stack.append(temp_str)
            # 如果是右括号则弹出栈顶左括号（-1）
            elif len(stack) > 0:
                top_str = stack.pop()
                # 如果两者匹配则继续，否则就终止
                # 由于需要按照顺序，所以不存在 ([)] 的情况
                if brackets[top_str] != temp_str:
                    return False
            else:
                return False
        return True if len(stack) == 0 else False


if __name__ == '__main__':
    print(Solution().isValid("){"))
