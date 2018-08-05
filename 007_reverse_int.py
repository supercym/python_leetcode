# Author: cym
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        if x < 0:
            x = -x
            flag = -1
        c = [str(n) for n in list(str(x))]
        c = c[::-1]
        s = int("".join(c))*flag
        if (s < -(1 << 31)) or (s > (1 << 31)-1):
            return 0
        else:
            return s
