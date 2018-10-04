# Author: cym

class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 1
        while n > digit*9*10**(digit - 1):
            n -= digit*9*10**(digit - 1)
            digit += 1
        a = int((n - 1)/digit)
        b = int((n - 1) % digit)
        num = 10**(digit - 1) + a
        res = list(str(num))[b:b+1]
        return int("".join(res))


