# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         394_decodeString
# Description:  394. 字符串解码
# Author:       skymoon9406@gmail.com
# Date:         2020/8/8
# -------------------------------------------------------------------------------


class Solution:
    def decodeString2(self, s: str) -> str:
        """
        （1）思路：栈
        （2）复杂度：
            - 时间复杂度：O（N）
            - 空间复杂度：O（N）
        """
        stack, res, multi = [], "", 0
        for c in s:
            if '0' <= c <= '9':
                # 如果该元素是数字的话
                # 这里考虑了多位数的情况，即数字连续的情况，比如"23[a"， "23"会转换成 23
                multi = multi * 10 + int(c)
            elif c == '[':
                # 如果元素是"["，
                # 记录此 [ 前的临时结果 res 至栈，用于发现对应 ] 后的拼接操作
                # 记录此 [ 前的倍数 multi 至栈，用于发现对应 ] 后，获取 multi × [...] 字符串。
                stack.append([multi, res])
                # res 和 multi 重新记录。
                res, multi = "", 0
            elif c == ']':
                # stack 出栈，拼接字符串 res = last_res + cur_multi * res，
                # last_res是上个 [ 到当前 [ 的字符串，例如 "3[a2[c]]" 中的 a
                # cur_multi是当前 [ 到 ] 内字符串的重复倍数，例如 "3[a2[c]]" 中的 2
                # res 是当前[  到 [ 内的字符串， 例如 "3[a2[c]]" 中的 c
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            else:
                # 当该元素是字母时候，直接添加在res末尾
                res += c
        return res

    def decodeString(self, s: str) -> str:
        # 初始化一个栈用于辅助运算
        stack = []
        # 遍历字符串
        for tempStr in s:
            if tempStr != ']':
                # 如果不是 ] 则可以直接入栈
                stack.append(tempStr)
            else:
                # 如果是 [ ，则要从栈中pop 出待复制的字母和待复制的次数
                # pop出待复制的字符串
                copy_str = ""
                while stack[-1] != '[' and len(stack) > 0:
                    copy_str = stack.pop() + copy_str
                # pop掉不需要的 [
                stack.pop(-1)
                # pop 出待复制的次数
                copy_num = ""
                while len(stack) > 0 and "0" <= stack[-1] <= "9":
                    copy_num = stack.pop() + copy_num
                # 待复制的次数转为数值型
                copy_num = int(copy_num)
                # 字符串复制指定次数后入栈
                after_str = copy_str * copy_num
                for t in after_str:
                    stack.append(t)
        # 栈中的字母pop出来形成字符串
        res = ""
        while len(stack) > 0:
            res = res + stack.pop(0)
        return res


if __name__ == '__main__':
    sa = "3[a2[c]]"
    print(Solution().decodeString(sa))