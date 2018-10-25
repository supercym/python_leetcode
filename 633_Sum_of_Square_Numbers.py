# Author: cym

class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        from math import sqrt
        i, j = 0, int(sqrt(c))+1
        res = False
        while i <= j:
            product = i*i + j*j
            if product < c:
                i += 1
            elif product > c:
                j -= 1
            else:
                res = True
                break
        return res

