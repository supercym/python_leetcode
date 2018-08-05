# Author: cym
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        pre = []
        for i in range(len(strs)-1):
            if i == 0:
                pre = self.commonprefix(strs[i], strs[i+1])
            else:
                pre_tmp = self.commonprefix(strs[i], strs[i+1])
                if ("".join(pre)) in ("".join(pre_tmp)):
                    continue
                elif ("".join(pre_tmp)) in ("".join(pre)):
                    pre = pre_tmp
                else:
                    break
        return "".join(pre)

    def commonprefix(self, str1, str2):
        pre = []
        list1 = list(str1)
        list2 = list(str2)
        for i in range(min(len(list1), len(list2))):
            if list1[i] == list2[i]:
                pre.append(list1[i])
            else:
                break
        return pre
