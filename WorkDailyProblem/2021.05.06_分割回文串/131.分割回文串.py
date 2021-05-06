#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
            获取所有子串，然后判断每个子串是否是回文串
        """
        str_length = len(s)
        temp_res, res = [], []

        def back_tracking(str_index):
            # 当满足遍历完字符串时，将temp_res写入到res
            if str_index >= str_length:
                res.append(temp_res[:])
                return

            for index in range(str_index, str_length):
                # 如果是回文串则，则将该字符串写入到temp_res中
                if self.helper(s[str_index:index + 1]):
                    temp_res.append(s[str_index:index + 1])
                    # 回溯继续做选择
                    back_tracking(index + 1)
                    # 撤销选择
                    temp_res.pop()

        back_tracking(0)
        return res

    def helper(self, temp: str) -> bool:
        """判断一个字符串是否是回文串"""
        str_length = len(temp)
        if str_length == 0:
            return False
        left, right = 0, str_length - 1
        while left < right:
            if temp[left] == temp[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
# @lc code=end

