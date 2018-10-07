# Author: cym

class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        if num < 0:
            num = -num
            num = ~num
            num += 1
        n = []
        for i in range(8):
            mask = 15
            tmp = mask & num
            n.append(tmp)
            num >>= 4
        n = n[::-1]
        d = {}
        for i, v in enumerate("0123456789abcdef"):
            d[i] = v
        ans = [d[x] for x in n]
        for i in range(len(ans)):
            if ans[i] == "0":
                ans[i] = ""
            else:
                break
        return "".join(ans)

