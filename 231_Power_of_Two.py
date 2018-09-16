# Author: cym

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mask = 1
        for i in range(32):
            if (n ^ mask) == 0:
                return True
            mask <<= 1
        return False
