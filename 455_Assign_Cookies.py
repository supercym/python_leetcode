# Author: cym

class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        res = 0
        for v in g:
            index = 0
            sLength = len(s)
            while index < len(s):
                if s[index] >= v:
                    res += 1
                    del s[index]
                    break
                else:
                    index += 1
            if len(s) == 0 or index == sLength:
                return res
        return res
