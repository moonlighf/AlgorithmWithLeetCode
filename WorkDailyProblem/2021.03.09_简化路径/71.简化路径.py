#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        # 根据规范，将文件路径根据斜杠进行分割
        path_list = path.split("/")
        # 用于存储结果数组
        res = []
        # 遍历分割后的路径数组
        for index in range(0, len(path_list)):
            # 如果该元素是 空，代表是连续的 / , 直接跳过，如果是 . 代表是当前目录，也是直接跳过
            if path_list[index] == "" or path_list[index] == ".":
                pass
            # 如果该元素是 ..  代表是返回到上层，即把res数组中pop个出来
            elif path_list[index] == "..":
                # 如果已经在根目录，则不能返回到上层
                if len(res) != 0:
                    res.pop()
            # 如果都不是，则是正常路径，压入数组即可
            else:
                res.append(path_list[index])
        return "/" + "/".join(res)
# @lc code=end

