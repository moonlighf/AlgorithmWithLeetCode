#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        ses = [""] * 4

        def back_track(ses_index, start_index):
            # 如果已经找到了4段，并且已经遍历末尾，那么则可以认为是一个合理的答案
            if ses_index == 4:
                if start_index == len(s):
                    res.append(".".join(ses))
                # 如果是没有遍历到末尾，那么继续回溯
                return

            # 如果已经遍历完了字符串，但是仍然没有达到4段
            if start_index == len(s):
                if ses_index != 4:
                    return

            # 如果当前数字是0，那么该段只能为0
            if s[start_index] == "0":
                ses[ses_index] = "0"
                back_track(ses_index + 1, start_index + 1)


            address = ""
            for end_index in range(start_index, len(s)):
                address = address + s[end_index]
                if 0 < int(address) <= 255:
                    ses[ses_index] = address
                    back_track(ses_index + 1, end_index + 1)
                else:
                    # 如果已经大于了255，再加上后面的数字只会更大，所以直接剪枝
                    break

        back_track(0, 0)
        return res
# @lc code=end

