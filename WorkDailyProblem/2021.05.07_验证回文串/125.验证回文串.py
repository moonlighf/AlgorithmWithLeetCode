#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """判断一个字符串是否是回文串"""
        str_length = len(s)
        if str_length == 0:
            return False
        left, right = 0, str_length - 1
        while left < right:
            # 如果当前字符不是数字和字母指针移动
            if not (48 <= ord(s[left]) <= 57 or 65 <= ord(s[left]) <= 90 or 97 <= ord(s[left]) <= 122):
                left += 1
                continue
            if not (48 <= ord(s[right]) <= 57 or 65 <= ord(s[right]) <= 90 or 97 <= ord(s[right]) <= 122):
                right -= 1
                continue

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True
# @lc code=end
