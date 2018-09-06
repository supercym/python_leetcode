# Author: cym

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        mask = 1
        count = 0
        for i in range(32):
            if (n & mask) >> i == 1:
                count += 1
            mask <<= 1
        return count
