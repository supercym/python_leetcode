# Author: cym

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0 and len(t) == 0:
            return True
        return self.string2int(s) == self.string2int(t)


    def string2int(self, s):
        d = {}
        index = 0
        sint = []
        for c in s:
            if c not in d.keys():
                d[c] = index
                sint.append(index)
                index += 1
            else:
                sint.append(d[c])
        return sint
